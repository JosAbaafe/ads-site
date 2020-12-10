from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SearchProductView.as_view(), name='query'),

]
