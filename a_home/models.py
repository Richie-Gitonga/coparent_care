from django.db import models
from django.contrib.auth.models import User
from a_users.models import Profile
import datetime

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null =True, blank=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__self(self):
        return self.title
    
    class Meta:
        ordering = ['complete']