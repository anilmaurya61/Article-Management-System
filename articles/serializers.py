from django.template.defaulttags import now
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'subtitle', 'content', 'tags', 'category', 'publish_date', 'author', 'image']
        read_only_fields = ['id']

    def validate_title(self, value):
        """Ensure the title is at least 10 characters long."""
        if len(value) < 10:
            raise serializers.ValidationError("The title must be at least 10 characters long.")
        return value

    def validate_publish_date(self, value):
        """Ensure the publish date is in the future."""
        if value <= now().date():
            raise serializers.ValidationError("The publish date must be in the future.")
        return value


class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'subtitle', 'content', 'tags', 'category', 'publish_date', 'author', 'status', 'image']
        read_only_fields = ['id']
