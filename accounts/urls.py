from django.urls import path
from . import views

urlpatterns = [
    path('signupaccount/', 'signupaccount.html', name='signupaccount'),
]