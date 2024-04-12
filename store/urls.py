from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('', views.store, name = "store"),
    path('cart/', views.cart, name = "cart"),
    path('checkout/', views.checkout, name = "checkout"),
    path('update_item/', views.updateItem, name = "update_item"),
    path('process_order/', views.processOrder, name = "process_order"),
    path('register/', views.RegisterPage, name = "register"),
    path('accounts/login/', views.LoginPage, name = "login"),
    path('logout/', views.LogoutPage, name='logout'),
    path('add_product/', views.AddProduct, name='add_product'),
    path('profile/', views.ProfilePage, name = "profile"),
    path('search/', views.search_filter, name='search'),
    
    
    path('reset_password/',
        auth_views.PasswordResetView.as_view(template_name = 'accounts/password_reset.html'), 
        name='password_reset'),
    
    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'accounts/password_reset_sent.html'),
        name='password_reset_done'),
    
    path('reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/password_reset_form.html'),
        name='password_reset_confirm'),
    
    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'accounts/password_reset_complete.html'),
        name='password_reset_complete'),
    
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
]