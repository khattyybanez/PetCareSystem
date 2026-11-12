from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('pets/', views.pet_list, name='pets'),
    path('pets/add/', views.pet_create, name='pet_create'),
    path('pets/<int:pk>/edit/', views.pet_update, name='pet_update'),
    path('pets/<int:pk>/delete/', views.pet_delete, name='pet_delete'),
    path('services/', views.services, name='services'),
    path('tips/', views.tips, name='tips'),
    path('contact/', views.contact, name='contact'),
]