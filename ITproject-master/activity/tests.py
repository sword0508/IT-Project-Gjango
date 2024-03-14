import json
from django.http import response
from django.test import TestCase, Client
from django.urls import reverse
from users.models import User
from activity.models import Activity


class ActivityListTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('activity:list')  # 根据您的URL配置进行修改
        self.username = "TR"
        self.password = "123"

    def test_activity_list_get(self):
        # 使用测试用户登录
        self.client.login(username=self.username, password=self.password)

        # 创建测试活动
        activity = Activity.objects.create(title='Test Activity', date='2022-01-01', time='10:00', peo_num=10,
                                           coasts=100)

        # 发送 GET 请求
        response = self.client.get(self.url)

        # 断言响应状态码为 200
        self.assertEqual(response.status_code, 200)

        # 断言活动标题在响应内容中
        self.assertContains(response, 'Test Activity')

    def test_activity_list_post(self):
        # 使用测试用户登录
        self.client.login(username=self.username, password=self.password)

        # 发送 POST 请求
        data = {
            'title': 'New Activity',
            'date': '2022-01-01',
            'time': '10:00',
            'peo_num': 10,
            'coasts': 100
        }
        response = self.client.post(self.url, data, content_type="application/json")

        # 断言响应状态码为 201
        self.assertEqual(response.status_code, 201)

        # 断言活动成功创建
        self.assertEqual(Activity.objects.count(), 1)
        activity = Activity.objects.first()
        self.assertEqual(activity.title, 'New Activity')

        # 断言响应内容中包含成功信息
        response_data = json.loads(response.content)
        self.assertEqual(response_data['status'], 201)
        self.assertEqual(response_data['msg'], 'SUCCESS!')

    def tearDown(self):
        # 清理测试数据
        User.objects.all().delete()
        Activity.objects.all().delete()