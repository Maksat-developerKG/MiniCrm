from django.db import models
from django.contrib.auth.models import User



class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
    
    

class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey('tasks.Task', on_delete=models.CASCADE)
    deal = models.ForeignKey('deals.Deal', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class ActionLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestep = models.DateTimeField(auto_now_add=True)

    

