from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('programs/create/', views.program_create, name='program_create'),
    path('clients/register/', views.client_register, name='client_register'),
    path('clients/', views.client_list, name='client_list'),
    path('clients/<int:client_id>/', views.client_profile, name='client_profile'),
    path('api/clients/<int:id>/', views.ClientAPIView.as_view(), name='client_api'),
    
]