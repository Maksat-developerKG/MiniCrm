
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('clients/', include('crm.urls')), 
    path('deals/', include('deals.urls')),
    path('tasks/', include('tasks.urls')),
    path('comments/', include('comments.urls')),
]
