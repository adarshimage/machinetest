"""sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from .import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('',views.index,name='index'),
    path('add_shop_details',views.add_shop_details,name='add_shop_details'),
    path('add_shop_details_action',views.add_shop_details_action,name="add_shop_details_action"),
    path('add_category_details',views.add_category_details,name='add_category_details'),
    path('add_category_details_action',views.add_category_details_action,name='add_category_details_action'),
    path('add_product_details',views.add_product_details,name='add_product_details'),
    path('add_product_action',views.add_product_action,name='add_product_action'),
    path('product_api',csrf_exempt(views.product_api),name="product_api"),
    path('delete_shop_details',views.delete_shop_details,name='delete_shop_details'),
    path('delete_category',views.delete_category,name='delete_category'),
    path('delete_product',views.delete_product,name='delete_product'),

    
]
