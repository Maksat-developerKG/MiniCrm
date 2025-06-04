from django.contrib import admin
from .models import Client, ActionLog


admin.site.register(Client)
admin.site.register(ActionLog)

