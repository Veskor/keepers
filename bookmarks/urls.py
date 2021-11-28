from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet

router = DefaultRouter()

router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    url(r'v1/', include(router.urls))
    ]
