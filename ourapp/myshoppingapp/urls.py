from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('shop/', views.shop_page, name='shop')
]