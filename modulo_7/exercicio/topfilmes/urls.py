from django.urls import path
from django.urls.resolvers import URLPattern
from . import views


app_name = 'topfilmes'

urlpatterns = [
    path('', views.home, name='home')
]