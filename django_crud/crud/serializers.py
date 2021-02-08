from rest_framework import serializers
from .models import PostInfo


class PostInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostInfo
        fields = ('question', 'answer', 'isActive')

