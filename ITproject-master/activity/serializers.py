from rest_framework import serializers

from activity.models import Activity
from comment.serializers import CommentSerializer
from users.serializers import UserSerializers, UserDescSerializer


class ActivityListSerializer(serializers.ModelSerializer):
    user = UserDescSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'date',
            'user',
            'title',
            'time',
            'peo_num',
            'coasts'
        ]


class ActivityDetailSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    user = UserDescSerializer(read_only=True)

    class Meta:
        model = Activity
        fields = [
            'id',
            'date',
            'user',
            'title',
            'time',
            'peo_num',
            'coasts'
        ]

