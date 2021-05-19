# 定义接口测试用例
# 使用unittest

# 导包
import unittest
import requests
import configure
from api.login import loginAPI
from utils import common_assert

# 创建测试类
class TestLogin(unittest.TestCase):
    # 前置方法
    def setUp(self):
        # 实例化接口类loginAPI
        self.login_api = loginAPI()
        # 创建session对象
        self.session = requests.session()

    # 后置方法
    def tearDown(self):
        if self.session:
            self.session.close()

    # 创建测试方法
    def test01_success(self):
        # 调用实例化对象的login方法，传递参数,返回响应结果。定义一个对象response来接收
        # response1是登录接口得到的响应数据
        response = self.login_api.login(self.session, "13800000002", "123456")
        print(response.json())
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        # 使用封装好的断言方法
        common_assert(self, response, 200, 10000, "操作成功")

        # 提取response的data信息，对configure文件中的TOKEN进行赋值
        configure.TOKEN = "Bearer " + response.json().get("data")
        # 对configure文件中的headers_data进行追加
        configure.headers_data["Authorization"] = configure.TOKEN
        print(configure.headers_data)

    def test02_fail(self):
        response = self.login_api.login(self.session, "", "123456")
        print(response.json())
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(20001, response.json().get("code"))
        # self.assertIn("用户名或密码错误", response.json().get("message"))
        # 使用封装好的断言方法
        common_assert(self, response, 200, 20001, "用户名或密码错误")

