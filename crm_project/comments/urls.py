from django.urls import path
from . import views 


urlpatterns = [
    path('tasks/<int:task_id>/comment/', views.add_comment, name='add_comment_to_task'),
    path('deals/<int:deal_id>/comment/', views.add_comment, name='add_comment_to_deal'),
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('deals/<int:pk>/', views.deal_detail, name='deal_detail')

]