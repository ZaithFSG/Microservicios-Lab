from django.urls import path
from .views import PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', PostViewSet, basename='post')
urlpatterns = router.urls