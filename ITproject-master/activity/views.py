import time

from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.



import os

from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
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



from django.shortcuts import render

@api_view(['GET', 'POST'])

def activity_list(request):
    if request.method == 'GET':
        activity = Activity.objects.all()
        serializer_context = {
            'request': request,
        }
        serializer = ActivityListSerializer(activity, context=serializer_context, many=True)
        data = serializer.data
        return render(request, 'application.html', {'activity': data})
    elif request.method == 'POST':

        activity = Activity()
        user = request.user
        activity.user = user
        activity.title = request.data.get('title')
        activity.date = request.data.get('date')
        activity.time = request.data.get('time')
        activity.peo_num = request.data.get('peo_num')
        activity.coasts = request.data.get('coasts')
        activity.save()
        serializer_context = {
            'request': request,
        }
        serializer = ActivityDetailSerializer(activity, context=serializer_context)
        data = serializer.data
        return  Response({
        'status': 201,
        'msg': 'SUCCESS!',

    })



class ActivityDeleteView(DeleteView):
    model = Activity
    success_url = reverse_lazy('application')  # 成功删除后重定向的 URL

    def get_object(self, queryset=None):
        # 使用传递的 pk 获取要删除的对象
        pk = self.kwargs.get(self.pk_url_kwarg)
        obj = self.model.objects.get(pk=pk)
        return obj

    def delete(self, request, *args, **kwargs):
        # 在这里执行您的自定义删除操作，例如记录日志等
        return super().delete(request, *args, **kwargs)