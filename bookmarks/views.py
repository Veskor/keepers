
from .serializers import BookmarkSerializer
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from django.contrib.auth.models import AnonymousUser
# Create your views here.


class BookmarkViewSet(viewsets.ModelViewSet):
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    serializer_class = BookmarkSerializer
    queryset = serializer_class.Meta.model.objects.all()

    def get_queryset(self):
        public_bookmarks = self.queryset.filter(public=True)

        if not isinstance(self.request.user, AnonymousUser):
            return self.queryset.filter(owner=self.request.user) | \
                    self.queryset.filter(public=True)
        else:
            return public_bookmarks

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
