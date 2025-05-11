from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('deposit/', views.deposit_money, name='deposit_money'),
    path('balance/', views.check_balance, name='check_balance'),
    path('logout/', views.logout_view, name='logout'),
]