"""concierge URL Configuration

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
from django.urls import path

from django.views.generic import TemplateView

from .views import health_check, index, api_serializer, KeyTransferView, \
    key_transfer_created

urlpatterns = [
    path('admin/', admin.site.urls),
    path('healthcheck/', health_check, name='health_check'),
    path('api/<str:model_type>/<int:object_id>', api_serializer, name='api'),
    path('key-transfer/', KeyTransferView.as_view(), name='key_transfer'),
    path('thanks/', key_transfer_created, name='key_transfer_created'),
    path('', index, name='index')

]
