from django.urls import path
from . import views

app_name = 'sendEmail'

urlpatterns = [
    path('', views.sendEmail , name='sendEmail'),
    path('sendmail/', views.sendmail , name='sendmail')
]