from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


# Create your models here.
class User(AbstractUser):

    email = models.EmailField(
        ('email address'),

        max_length=100,
        unique=True,
    )
    first_name = models.CharField(max_length=100, default=" ")
    last_name = models.CharField(max_length=100, default=" ")
    is_email_verified = models.BooleanField(verbose_name="邮箱是否验证", default=False)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'User'


class email_reset(models.Model):
    email_address = models.EmailField(null=False,unique=True) #邮箱地址唯一的
    vc_code = models.CharField(max_length=64,null=False) #随机验证码
    send_time = models.DateTimeField(auto_now=True)  #邮箱发送时间


