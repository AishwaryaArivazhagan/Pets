"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from . views import *
from app import views

urlpatterns = [
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('login/',login,name='login'),
    path('logout/',views.logout,name="logout"),
    path('product/<int:id>',views.product,name="product"),
    path('beagle/',views.beagle,name='beagle'),
    path('shop_details/<int:id>/',views.shop_detail,name="shop_detail"),
    path('cart/<int:id>/',views.cart,name="cart"),
    path('viewcart/',views.view_cart,name='viewcart'),
    path('decrement/<str:id>',views.decre,name="decrement"),
    path('incre/<str:id>',views.incre,name="incre"),
    path('shop_details/view_cart/delete/<str:id>',views.remove_cart,name='deletecartoneitem'),


     

]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)

