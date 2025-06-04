from django.db import models
from crm.models import Client
from django.contrib.auth.models import User

# Create your models here.
class Deal(models.Model):
    STATUS_CHOICE = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('won', 'won'),
        ('lost', 'Lost'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title