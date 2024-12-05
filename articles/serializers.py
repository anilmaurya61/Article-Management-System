# articles/serializers.py
from rest_framework import serializers
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'image', 'tags', 'category', 'publish_date', 'status']
        read_only_fields = ['author']

    def validate(self, data):
        """
        Ensure that the article status is either draft, pending, approved, or published.
        """
        if data.get('status') and data['status'] not in dict(Article.STATUS_CHOICES):
            raise serializers.ValidationError("Invalid status")
        return data
