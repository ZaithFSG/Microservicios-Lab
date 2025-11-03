from rest_framework import generics, permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Category
from .serializers import CategorySerializer


@method_decorator(cache_page(60), name="dispatch")
class CategoryListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(is_active=True)