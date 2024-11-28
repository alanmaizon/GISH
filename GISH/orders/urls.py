from django.urls import path
from django.contrib.auth.views import LogoutView, PasswordChangeView, PasswordChangeDoneView
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='orders/logout.html'), name='logout'),
    path('product/create/', views.create_product, name='product_form'),
    path('orders/', views.user_orders, name='user_orders'),
    path('inbox/', views.inbox, name='inbox'),
    path('order_summary/', views.create_product, name='order_summary'),
    path('change-password/', PasswordChangeView.as_view(template_name='orders/change_password.html'), name='change_password'),
    path('change-password/done/', PasswordChangeDoneView.as_view(template_name='orders/change_password_done.html'), name='password_change_done'),
    path('email_change/', views.change_email, name='email_change'),
    path('email_change/done/', views.email_change_done, name='email_change_done'),
]
