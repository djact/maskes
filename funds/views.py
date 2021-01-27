from django.utils import timezone
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from .serializers import ReimbursementSerializer, DonationSerializer, DonationListSerializer
from .models import Reimbursement, Donation
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.decorators import action, permission_classes, parser_classes
from django.contrib.auth import get_user_model
from supports.models import Request
import os
import json
import stripe

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
User = get_user_model()


class ReimbursementViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ReimbursementSerializer
    queryset = Reimbursement.objects.all().order_by('-created_date')


class DonationViewSet(ModelViewSet):
    permission_classes = [AllowAny, ]
    serializer_class = DonationSerializer
    queryset = Donation.objects.all().order_by('-created_date')

    def perform_create(self, serializer):
        serializer.save(donator=self.request.user)

    def perform_update(self, serializer):
        instance = serializer.save()
        instance.updated_date = timezone.now()
        instance.save()

    @action(methods=['GET'], detail=False, url_path='public-key')
    def public_key(self, request):
        return Response({
            'publicKey': os.getenv('STRIPE_PUBLISHABLE_KEY')
        })

    @action(methods=['POST'], detail=False, url_path='create-checkout-session')
    def create_checkout_session(self, request):

        try:
            amount = int(request.data['amount'])
            if (amount/100 < 1):
                return Response({'error': 'Donation amount should be at least $1'}, status=HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Invalid input amount'}, status=HTTP_400_BAD_REQUEST)

        requestId = request.data['requestId']

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': 'Donation',
                    },
                    'unit_amount': amount,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url="http://localhost:3000/donation/success",
            cancel_url='http://localhost:3000/volunteer/{}'.format(requestId),
            metadata={
                'requestId': requestId
            },
            customer_email=self.request.user.email,
            client_reference_id=self.request.user.id

        )

        return Response({'id': session.id, 'amount': amount})

    @action(methods=['POST'], detail=False, url_path='webhook')
    def webhook_received(self, request):
        # You can use webhooks to receive information about asynchronous payment events.
        # For more about our webhook events check out https://stripe.com/docs/webhooks.
        webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

        # Note: this need to be the raw request body (str) before parsing

        payload = request.body
        sig_header = request.META['HTTP_STRIPE_SIGNATURE']
        event = None

        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, webhook_secret
            )
        except ValueError as e:

            return Response({'Error': 'Invalid payload'}, status=HTTP_400_BAD_REQUEST)
        except stripe.error.SignatureVerificationError as e:

            return Response({'Error': 'Invalid signature'}, status=HTTP_400_BAD_REQUEST)

        if event['type'] == 'checkout.session.completed':
            print("💰 Checkout completed!")
            session = event['data']['object']
            donation = self.create_donation(session)

            if session.payment_status == "paid":

                self.fulfill_donation(session, donation)

        elif event['type'] == 'checkout.session.async_payment_succeeded':
            session = event['data']['object']
            donation = self.create_donation(session)

            self.fulfill_donation(session, donation)

        elif event['type'] == 'checkout.session.async_payment_failed':
            session = event['data']['object']

            self.email_customer_about_failed_payment(session)

        return Response({'status': 'Checkout Success'}, status=HTTP_200_OK)

    def fulfill_donation(self, session, donation):
        donation.status = session["payment_status"]

    def create_donation(self, session):
        amount = int(session["amount_total"])/100
        status = session["payment_status"]
        donator = User.objects.get(id=session["client_reference_id"])
        request = Request.objects.get(id=session["metadata"]["requestId"])
        paymentId = session["payment_intent"]
        donation = Donation.objects.create(
            amount=amount, status=status, request=request, donator=donator, payment_id=paymentId)
        return donation

    def email_customer_about_failed_payment(self, session):
        print("Emailing customer: ", session["customer_email"])


class ListDonationForSignleRequest(ListAPIView):
    serializer_class = DonationListSerializer
    permission_classes = [AllowAny, ]

    def get_queryset(self, *args, **kwargs):
        return Donation.objects.filter(request_id=self.kwargs.get('uid'))

    def list(self, request, uid):
        queryset = self.get_queryset(uid)
        serializer = DonationListSerializer(queryset, many=True)
        return Response(serializer.data)
