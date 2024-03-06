from rest_framework import serializers

from activity.models import Activity
from comment.serializers import CommentSerializer
from users.serializers import UserSerializers, UserDescSerializer


class ActivityListSerializer(serializers.ModelSerializer):
    user = UserDescSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name="activity:detail")
    class Meta:
        model = Activity
        fields = [
            'id',
            'url',
            'user',
            'text',
            'created',
            'likes'
        ]


class ActivityDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    user = UserDescSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'user',
            'text',
            'created',
            'likes',
            'comments',
        ]

