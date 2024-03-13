"""ITproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from rest_framework import routers
from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
#from users import views
#from rest_framework_jwt.views import obtain_jwt_token
from comment.views import CommentViewSet, IncreaseActivityLikeView, IncreaseCommentLikeView
from django.conf.urls.static import static
from . import views

from users.views import UserViewSet, verify_email, CustomTokenObtainPairView
from activity.views import activity_list
from activity.views import ActivityDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register(r'api/user', UserViewSet)
router.register(r'comment', CommentViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    #path('login/',obtain_jwt_token),
   # path('wx/',views.Login.as_view()),
    path('api/activity/', include('activity.urls', namespace='activity')),
    path('api/', include(router.urls)),
    path('api/like/comment/<int:pk>/', IncreaseCommentLikeView.as_view()),
    path('api/like/activity/<int:pk>/', IncreaseActivityLikeView.as_view()),
    path('api/verify', verify_email, name='verify-email'),
    path('verification-success/', TemplateView.as_view(template_name='verification_success.html'),
         name='verification-success'),
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="profile"),
    path('tour-details/', views.tour_details, name="tour-details"),
    path('application/',activity_list , name="application"),
    path('des/',views.des , name="des"),
    path('tours/',views.tours , name="tours"),
    path('tes/',views.tes , name="tes"),
    path('faq/',views.faq , name="faq"),
    path('about/',views.about , name="about"),
    path('blog/',views.blog , name="blog"),
    path('bd/',views.bd , name="bd"),
    path('cont/',views.cont , name="cont"),
    path('delete_activity/<int:pk>/', ActivityDeleteView.as_view(), name="delete_activity"),
]
urlpatterns += router.urls
