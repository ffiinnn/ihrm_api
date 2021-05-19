import unittest
import requests
from utils import common_assert
from api.employee import employeeAPI

# 添加员工测试类
class TestEmployee(unittest.TestCase):
    # 定义类变量employee_id
    # 类变量是所有对象共有，其中一个对象将它值改变，其他对象得到的就是改变后的结果；而实例变量self则属对象私有，某一个对象将其值改变，不影响其他对象
    employee_id = None

    # 前置处理，初始化动作
    def setUp(self):
        self.employee_api = employeeAPI()

    # 添加员工
    def test01_add_employee(self):
        # 定义json数据
        add_employee_data = {"username":"finntest16", "mobile":"13900000116", "workNumber":"072116"}
        # 发送请求，接收响应
        response = self.employee_api.req_add_employee(add_employee_data=add_employee_data)
        print(response.json())
        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))
        # 使用封装好的断言方法
        common_assert(self, response, 200, 10000, "操作成功")
        # common_assert(self, response)

        # 提取员工id
        TestEmployee.employee_id = response.json().get("data").get("id")
        print(TestEmployee.employee_id)

    # 修改员工
    def test02_update_employee(self):
        # 定义json数据，修改用户名
        update_employee_data = {"username":"finntest"}
        # 发送请求,传入employee_id和json数据
        response = self.employee_api.req_update_employee(TestEmployee.employee_id, update_employee_data=update_employee_data)
        print(response.json())
        # 使用封装好的断言方法
        # common_assert(self, response, 200, 10000, "操作成功")
        common_assert(self, response)

    # 查询员工
    def test03_get_employee(self):
        # 通过实例化对象调用类中的查询员工接口，传入指定员工id
        response = self.employee_api.req_get_employee(TestEmployee.employee_id)
        print(response.json())
        # 使用封装好的断言方法
        # common_assert(self, response, 200, 10000, "操作成功")
        common_assert(self, response)

    # 删除员工
    def test04_delete_employee(self):
        response = self.employee_api.req_delete_employee(TestEmployee.employee_id)
        print(response.json())
        # 使用封装好的断言方法
        # common_assert(self, response, 200, 10000, "操作成功")
        common_assert(self, response)




