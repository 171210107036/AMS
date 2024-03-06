from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
    datatime = models.DateTimeField(null=False)
    title = models.CharField(max_length=255)
    detail = models.TextField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True, default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)
