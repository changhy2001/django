from django.db import models
from django.contrib.auth.models import User

class UserMeta(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="meta_info")
    questions = models.JSONField(default=list, blank=True)  # Store a list of text questions
    credentials = models.JSONField(default=dict, blank=True)  # Store credentials in JSON format
    session_info = models.TextField(blank=True, null=True)  # Store session metadata
    user_logs = models.JSONField(default=list, blank=True)  # Store user activity logs
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp when updated

    def __str__(self):
        return f"Meta Info for {self.user.username}"
