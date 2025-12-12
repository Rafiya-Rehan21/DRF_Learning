from rest_framework import serializers
from .models import Post, Comment

# ----- Comment Serializer -----
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']

# ----- Post Serializer (with nested comments + validation) -----
class PostSerializer(serializers.ModelSerializer):
    # Nested comments
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'comments']
        read_only_fields = ['id', 'created_at', 'comments']

    # Field-level validation for unique title
    def validate_title(self, value):
        if Post.objects.filter(title=value).exists():
            raise serializers.ValidationError("This title is already used.")
        return value

    # Object-level validation for minimum content length
    def validate(self, attrs):
        if len(attrs.get('content', '')) < 20:
            raise serializers.ValidationError("Content must be at least 20 characters long.")
        return attrs
