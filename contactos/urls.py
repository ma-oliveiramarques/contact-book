from django import views
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'contactos'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('edit/<int:contactos_id>', views.edit, name='edit'),
    path('delete/<int:contactos_id>', views.delete, name='delete'),
    path('groups/', views.groups, name='groups'),
]
