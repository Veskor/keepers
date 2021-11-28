from .models import Bookmark
from rest_framework import serializers


class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'title', 'url', 'public', 'owner', 'created_at')
        read_only_fields = ('owner',)

    def validate(self, attrs):
        attrs['owner'] = self.context['request'].user
        return attrs
