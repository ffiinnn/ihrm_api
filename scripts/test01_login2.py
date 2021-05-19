import json
import unittest
import requests
from api.login2 import loginAPI2
from parameterized import parameterized
import configure

def params_data():
    # 定义空列表存放读取到的数据
    test_data = []
    # 指定json数据文件地址
    file = configure.BASE_DIR + "/data/LoginData.json"
    # 打开文件
    with open(file, encoding="utf-8") as f:
        # 加载文件中的json数据
        json_data = json.load(f)
        # 变量循环加载的json数据，用get方法获取key
        for case_data in json_data:
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            message = case_data.get("message")
            test_data.append((mobile, password, status_code, code, message))
            print(test_data)
    return test_data

class LoginTest_tryagain(unittest.TestCase):
    def setUp(self):
        # 实例化loginAPI接口类
        self.login_api = loginAPI2()
        # 实例化session
        self.session = requests.session()

    def tearDown(self):
        # 用完后，关闭session
        if self.session:
            self.session.close()

    # 参数化修饰
    @parameterized.expand(params_data())
    def testcase_login(self, mobile, password, status_code, code, message):
        # 发送请求
        # 前面setUp方法实例化了login_api，调用login_api的req_login2方法
        response = self.login_api.req_login2(self.session, mobile, password)
        # 接收响应
        print(response.json())
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))
