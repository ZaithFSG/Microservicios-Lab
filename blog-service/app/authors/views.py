from rest_framework import generics, permissions
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from .models import Author
from .serializers import AuthorSerializer

@method_decorator(cache_page(60), name="dispatch")
class AuthorListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
