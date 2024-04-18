"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from sales_network.apps import SalesNetworkConfig
from sales_network.views import *

urlpatterns = [
    path('seller/create/', SellerCreateApiView.as_view(), name='seller-create'),
    path('seller/retrieve/<int:pk>/', SellerRetrieveApiView.as_view(), name='seller-retrieve'),
    path('seller/update/<int:pk>/', SellerUpdateApiView.as_view(), name='seller-update'),
    path('seller/delete/<int:pk>/', SellerDestroyApiView.as_view(), name='seller-delete'),
    path('seller/list/', SellerListApiView.as_view(), name='seller-list'),
]
