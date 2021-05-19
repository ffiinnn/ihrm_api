# 定义参数化接口测试用例

# 导包
import unittest
import requests
from api.login import loginAPI
from parameterized import parameterized
from tools.dbutil import DBUtil

# 构造参数化测试数据方法
def build_data():
    # 查找t_login表里面的全部数据
    sql = "select * from t_login"
    # 执行sql,定义一个变量db_data来存放结果
    db_data = DBUtil.execute_sql(sql)
    # 定义一个空列表用来接收返回的读取文件数据
    test_data = []
    for case_data in db_data:
        # db中取数据按下标取
        mobile = case_data[2]
        password = case_data[3]
        status_code = case_data[4]
        code = case_data[5]
        message = case_data[6]
        # 列表中追加数据，每次遍历为一组
        test_data.append((mobile, password, status_code, code, message))
        print(test_data)
    # 数据处理完后返回列表
    return test_data

# 创建测试类
class TestLogin3(unittest.TestCase):
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
