from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

from rest_framework import viewsets

from comment.models import Comment, CommentLike, ActivityLike
from comment.serializers import CommentSerializer
from comment.permissions import IsOwnerOrReadOnly
from activity.models import Activity

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class IncreaseCommentLikeView(APIView):
    def post(self, request, pk):
        user = request.user
        comment = Comment.objects.get(pk=pk)
        try:
            CommentLike.objects.get(user=user, comment=comment)
        except CommentLike.DoesNotExist:
            comment_like = CommentLike(user=user, comment=comment)
            comment.likes += 1
            comment.save()
            comment_like.save()
            return Response({
                'status': 201,
                'msg': '点赞成功',
            })
        else:
            return Response({
                'status': 201,
                'msg': '这条评论已经被用户点赞过了',
            })

    def delete(self, request, pk):
        user = request.user
        comment = Comment.objects.get(pk=pk)
        try:
            CommentLike.objects.get(user=user, comment=comment)
        except CommentLike.DoesNotExist:
            return Response({
                'status': 201,
                'msg': '没有相关点赞记录',
            })
        else:
            comment_like = CommentLike.objects.get(user=user, comment=comment)
            comment.likes -= 1
            comment.save()
            comment_like.delete()
            return Response({
                'status': 201,
                'msg': '取消赞成功',
            })

class IncreaseActivityLikeView(APIView):
    def post(self, request, pk):
        user = request.user
        activity = Activity.objects.get(pk=pk)
        try:
            ActivityLike.objects.get(user=user, activity=activity)
        except ActivityLike.DoesNotExist:
            activity_like = ActivityLike(user=user, activity=activity)
            activity.likes += 1
            activity.save()
            activity_like.save()
            return Response({
                'status': 201,
                'msg': '点赞成功',
            })
        else:
            return Response({
                'status': 201,
                'msg': '这个主题文章已经被用户点赞过了',
            })

    def delete(self, request, pk):
        user = request.user
        activity = Activity.objects.get(pk=pk)
        try:
            ActivityLike.objects.get(user=user, activity=activity)
        except ActivityLike.DoesNotExist:
            return Response({
                'status': 201,
                'msg': '没有相关点赞记录',
            })
        else:
            activity_like = ActivityLike.objects.get(user=user, activity=activity)
            activity.likes -= 1
            activity.save()
            activity_like.delete()
            return Response({
                'status': 201,
                'msg': '取消赞成功',
            })
