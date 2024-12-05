# articles/views.py

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsJournalist, IsEditor, IsAdmin


class ArticleCreateView(APIView):
    """
    Allow journalists to create articles.
    """
    permission_classes = [IsAuthenticated & IsJournalist]

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Associate article with logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleListView(APIView):
    """
    Allow users to list articles.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    """
    Allow journalists to edit their own articles.
    Editors can approve, reject, or publish articles.
    Admins can manage all articles.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        # Check if the user is the author or an editor/admin
        if not request.user == article.author and not request.user.has_perm('articles.change_article'):
            return Response({'error': 'You do not have permission to edit this article'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        # Only Editors and Admins can approve, reject, or publish articles
        if not request.user.has_perm('articles.change_article'):
            return Response({'error': 'You do not have permission to update this article'}, status=status.HTTP_403_FORBIDDEN)

        if 'status' in request.data:
            article.status = request.data['status']
            article.save()
            return Response({'message': 'Article status updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid data'}, status=status.HTTP_400_BAD_REQUEST)


class ArticleDeleteView(APIView):
    """
    Admin can delete articles.
    """
    permission_classes = [IsAuthenticated & IsAdmin]

    def delete(self, request, pk):
        try:
            article = Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)

        article.delete()
        return Response({'message': 'Article deleted successfully'}, status=status.HTTP_200_OK)
