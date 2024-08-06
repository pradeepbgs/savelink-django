from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Link (models.Model):
    title = models.CharField(max_length=255,blank=True,null=True)
    link = models.URLField(max_length=400)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='links')
    tags = models.JSONField(default=list,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)