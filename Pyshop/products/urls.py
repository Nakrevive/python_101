from django.urls import path
from . import views

views.index
#/products
#/products/1/detail
#/products/new

urlpatterns = [
    path('',views.index),
    path('new', views.new)
    
]