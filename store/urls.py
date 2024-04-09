from django.urls import path
from django.urls import re_path
from django.views.generic import RedirectView
from.import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('process_order/', views.processOrder, name = "process_order"),
    path('register/', views.RegisterPage, name = "register"),
    path('login/', views.LoginPage, name = "login"),
    path('logout/', views.LogoutPage, name='logout'),
    path('add_product/', views.AddProduct, name='add_product'),
    path('profile/', views.ProfilePage, name = "profile"),
    
    
    
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    
]