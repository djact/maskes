from django.urls import path
from .views import FAQListView
pp_name = 'faq'

urlpatterns = [
    path('', FAQListView.as_view(), name='faqlist'),
]
