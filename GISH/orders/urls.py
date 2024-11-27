from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('product/create/', views.create_product, name='create_product'),
]
