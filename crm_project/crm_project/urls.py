
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('crm.urls')), 
    path('deals/', include('deals.urls')),
    path('tasks/', include('tasks.urls')),
]
