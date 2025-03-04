from rest_framework import serializers
from .models import UserMeta

class UserMetaSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = UserMeta
        fields = [
            'id', 'username', 'questions', 'credentials', 'session_info', 
            'user_logs', 'created_at', 'updated_at'
        ]