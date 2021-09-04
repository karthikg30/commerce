from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('product/', views.product, name = 'Product'),
    path("customer/<str:pk_test>/", views.customer_vw, name = 'customers'),
    path('create_order/<str:pk>/', views.create_order, name = 'create_order'),
    path('update_order/<str:pk>/', views.update_order, name = 'update_order'),
    path('delete_order/<str:pk_del>/', views.delete_order, name = 'delete_order'),
    path('create_cust/', views.create_cust, name = 'create_cust'),
    path('update_cust/<str:pk_up>/', views.update_cust, name = 'update_cust'),
    path('register/', views.register, name = 'register'),
    path('login/', views.loginpage, name = 'login'),
    path('logout/', views.logoutpage, name = 'logout'),
    path('user/', views.userpage, name = 'userpage'),
    ]