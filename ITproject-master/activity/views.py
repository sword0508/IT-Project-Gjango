import time

from django.shortcuts import render


# Create your views here.



import os

from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from activity.models import Activity
from activity.permissions import IsUserOrReadOnly

from activity.serializers import ActivityListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse

from django.http import Http404
from rest_framework import mixins
from rest_framework import generics

from activity.serializers import ActivityDetailSerializer



@api_view(['GET', 'POST'])
def activity_list(request):
    if request.method == 'GET':
        activity = Activity.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = ActivityListSerializer(activity, context=serializer_context, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        if not request.user.is_active:
            return Response({
                'status': 401,
                'msg': '请先登录',
            })
        activity = Activity()
        user = request.user
        activity.user = user
        activity.text = request.data.get('body')
        activity.save()
        serializer_context = {
            'request': request,
        }
        serializer = ActivityDetailSerializer(activity, context=serializer_context)
        # 返回 Json 数据
        return Response(serializer.data)



class ActivityDetail(APIView):
    """文章详情视图"""

    def get_object(self, pk):
        """获取单个文章对象"""
        try:
            # pk 即主键，默认状态下就是 id
            return Activity.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request, pk):
        activity = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = ActivityDetailSerializer(activity,  context=serializer_context)
        # 返回 Json 数据
        return Response(serializer.data)

    def put(self, request, pk):
        activity = self.get_object(pk)
        serializer_context = {
            'request': request,
        }
        serializer = ActivityDetailSerializer(activity, data=request.data, context=serializer_context)
        # 验证提交的数据是否合法
        # 不合法则返回400
        if serializer.is_valid():
            # 序列化器将持有的数据反序列化后，
            # 保存到数据库中
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        activity = self.get_object(pk)
        activity.delete()
        # 删除成功后返回204
        return Response({'msg': '删除成功'}, status=status.HTTP_204_NO_CONTENT)

    permission_classes = [IsUserOrReadOnly]
