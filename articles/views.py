# articles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsJournalist, IsEditorOrAdmin


class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category', 'tags']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


class ArticlePublishView(APIView):
    """
    Allow Editors and Admins to approve and publish articles.
    """
    permission_classes = [IsEditorOrAdmin]

    def post(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            article.status = 'published'
            article.publish_date = timezone.now()
            article.save()
            return Response({'message': 'Article published successfully'}, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)


class ArticleApproveView(APIView):
    """
    Allow Editors and Admins to approve articles.
    """
    permission_classes = [IsEditorOrAdmin]

    def post(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            article.status = 'approved'
            article.save()
            return Response({'message': 'Article approved successfully'}, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)


class ArticleRejectView(APIView):
    """
    Allow Editors and Admins to reject articles.
    """
    permission_classes = [IsEditorOrAdmin]

    def post(self, request, pk):
        try:
            article = Article.objects.get(id=pk)
            article.status = 'pending'
            article.save()
            return Response({'message': 'Article rejected successfully'}, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
