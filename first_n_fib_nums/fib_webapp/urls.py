from django.urls import path
from . import views

urlpatterns = [
    path('fib-num/', views.fib_nums, name='url1')
]