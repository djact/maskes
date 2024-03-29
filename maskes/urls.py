"""maskes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static

admin.site.site_header = "MASKES Admin"
admin.site.site_title = "MASKES Admin Portal"
admin.site.index_title = "Welcome to Mutual Aid South King County & East Side Portal"

INDEX = 'index.html'
if settings.DEBUG:
    INDEX = 'home.html'

urlpatterns = [
    path('', TemplateView.as_view(template_name=INDEX)),
    path('admin/', admin.site.urls),
    path('', include('users.urls', namespace='user')),
    # path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('requests/', include('supports.urls', namespace='request')),
    path('funds/', include('funds.urls', namespace='fund')),
    path('connect/', include('connect.urls', namespace='connection')),
    path('events/',include('events.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name=INDEX))]
