# articles/serializers.py

from rest_framework import serializers
from .models import Article
from users.models import User


class ArticleSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'image', 'tags', 'category', 'publish_date', 'status']
        read_only_fields = ['author', 'publish_date']

    def validate(self, data):
        if data.get('status') == 'published' and not data.get('publish_date'):
            raise serializers.ValidationError('Published articles must have a publish date.')
        return data
