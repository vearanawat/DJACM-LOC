from django.contrib import admin
from django.urls import path, include
from website import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('/chatbot', views.chatbot, name='chatbot'),
]
