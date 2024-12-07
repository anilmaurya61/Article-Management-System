from datetime import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer
from .permissions import IsJournalist, IsEditorOrAdmin


class ArticleCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    # permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category', 'tags']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

class ArticlePublishView(APIView):
    """
    Allow Editors and Admins to approve and publish articles, with status as a query parameter.
    """
    permission_classes = [IsEditorOrAdmin]

    def post(self, request, pk):
        status_param = request.data.get('status')  # Use .get() to avoid KeyError
        if not status_param:
            return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure the status is valid (you can customize this list as needed)
        if status_param not in ['reviewed', 'published', 'approved', 'rejected']:
            return Response({'error': 'Invalid status provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            article = Article.objects.get(id=pk)
            article.status = status_param
            if status_param == 'published':
                article.publish_date = timezone.now()
            article.save()
            return Response({'message': f'Article status updated to {status_param} successfully'}, status=status.HTTP_200_OK)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
