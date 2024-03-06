from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from users.models import User

class Activity(models.Model):
    user = models.ForeignKey(to=User, related_name='activity', on_delete=models.SET,
                             blank=True, null=True)
    # 标题
    title = models.CharField(max_length=100, default=" ")
    # 正文
    text = models.TextField()
    # 创建时间
    created = models.DateTimeField(default=timezone.now)
    # 点赞数
    likes = models.PositiveIntegerField("喜欢", default=0, editable=False)
    # 图片
    picture = models.FileField(upload_to='media/pic/', default=None)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

