from rest_framework import routers
from .views import BookViewSet

router = routers.SimpleRouter()
router.register(r'books', BookViewSet, basename='books')

urlpatterns = router.urls