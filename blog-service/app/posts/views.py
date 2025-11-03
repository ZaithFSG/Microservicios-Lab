from rest_framework import viewsets, mixins, filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer

@method_decorator(cache_page(60), name="retrieve")  # cache detail 60s
class PostViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Post.objects.filter(status="published").select_related("author","category").order_by("-published_at")
    serializer_class = PostListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title","body"]

    def get_serializer_class(self):
        return PostDetailSerializer if self.action == "retrieve" else PostListSerializer