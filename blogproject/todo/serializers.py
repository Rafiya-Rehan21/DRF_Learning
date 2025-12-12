# todo/serializers.py
from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'completed', 'likes_count', 'created_at']

    def get_likes_count(self, obj):
        return obj.likes.count()
