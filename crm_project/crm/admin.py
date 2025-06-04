from django.contrib import admin
from .models import Client, ActionLog, Comment


admin.site.register(Client)
admin.site.register(ActionLog)
admin.site.register(Comment)

