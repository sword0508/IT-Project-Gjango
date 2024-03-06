
from rest_framework import serializers

from comment.models import Comment
from users.serializers import UserSerializers, UserDescSerializer


class CommentChildrenSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            'parent',
            'activity'
        ]

class CommentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='comment-detail')
    author = UserDescSerializer(read_only=True)

    activity = serializers.HyperlinkedRelatedField(view_name='activity:activity-detail', read_only=True)
    activity_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)

    parent = CommentChildrenSerializer(read_only=True)
    parent_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    def update(self, instance, validated_data):
        validated_data.pop('parent_id', None)
        validated_data.pop('activity_id', None)
        return super().update(instance, validated_data)

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'created': {'read_only': True}}