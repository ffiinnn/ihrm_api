# 定义参数化接口测试用例

# 导包
import json
import unittest
import requests
from api.login import loginAPI
from parameterized import parameterized
import configure

# 构造参数化测试数据方法
def build_data():
    # # 指定数据文件地址(../代表回到当前文件的上级目录)
    # file = "../data/LoginData.json"
    # 使用绝对路径，指定数据文件地址
    file = configure.BASE_DIR + "/data/LoginData.json"
    # 定义一个空列表用来接收返回的读取文件数据
    test_data = []
    # 通过文件流形式打开文件，默认是"r"
    # with语句来自动调用close()方法
    with open(file, encoding="utf-8") as f:
        # 加载json数据
        json_data = json.load(f)
        # 拼接参数，加到列表中
        for case_data in json_data:
            # json中取文件数据按get(key)来取
            mobile = case_data.get("mobile")
            password = case_data.get("password")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            message = case_data.get("message")
            # 列表中追加数据，每次遍历为一组
            test_data.append((mobile, password, status_code, code, message))
            print(test_data)
    # 数据处理完后返回列表
    return test_data

# 创建测试类
class TestLogin2(unittest.TestCase):
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
    # 参数化
    @parameterized.expand(build_data())
    def testcase_login(self, mobile, password, status_code, code, message):
        # 调用实例化对象的login方法，传递参数,返回响应结果。定义一个对象response来接收
        # response1是登录接口得到的响应数据
        response = self.login_api.login(self.session, mobile, password)
        print(response.json())
        # 断言
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))
