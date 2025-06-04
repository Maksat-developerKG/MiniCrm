from django.urls import path
from . import views 

urlpatterns = [
    path('clients_list/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'),
    path('clients/edit/<int:pk>/', views.client_edit, name='client_edit'),
    path('clients/delete/<int:pk>/', views.client_delete, name='client_delete'),
    
]


