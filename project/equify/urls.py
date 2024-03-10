from django.urls import path
from equify.views import input_form

urlpatterns = [
    path('input', input_form, name='input_form'),
]

