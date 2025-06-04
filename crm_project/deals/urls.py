from django.urls import path
from . import views 

urlpatterns = [
    path('deals_list/', views.deal_list, name='deal_list'),
    path('deals/add/', views.deal_create, name='deal_create'),
    path('deals/edit/<int:pk>/', views.deal_edit, name='deal_edit'),
    path('deals/delete/<int:pk>/', views.deal_delete, name='deal_delete'),
]