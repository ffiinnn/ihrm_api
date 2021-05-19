# 定义员工管理模块相关类
import requests
import configure

class employeeAPI():
    # 初始化接口地址
    def __init__(self):
        self.url_employee_list = configure.BASE_URL + "/api/sys/user"
        self.url_add_employee = configure.BASE_URL + "/api/sys/user"
        self.url_update_employee = configure.BASE_URL + "/api/sys/user/{}"
        self.url_get_employee = configure.BASE_URL + "/api/sys/user/{}"
        self.url_delete_employee = configure.BASE_URL + "/api/sys/user/{}"

    # 添加员工接口
    def req_add_employee(self, add_employee_data):
        # 发送请求，返回给用例
        return requests.post(url=self.url_add_employee, json=add_employee_data, headers=configure.headers_data)

    # 修改员工接口
    def req_update_employee(self, employee_id, update_employee_data):
        # 拼装url，通过格式化方法传入员工id
        update_url = self.url_update_employee.format(employee_id)
        # 发送请求，返回给用例
        return requests.put(url=update_url, json=update_employee_data, headers=configure.headers_data)

    # 查询员工接口
    def req_get_employee(self, employee_id):
        get_url = self.url_get_employee.format(employee_id)
        return requests.get(url=get_url, headers=configure.headers_data)

    # 删除员工接口
    def req_delete_employee(self, employee_id):
        delete_url = self.url_delete_employee.format(employee_id)
        return requests.delete(url=delete_url, headers=configure.headers_data)

    # 获取员工列表接口
    # def req_employee_list(self, session):
    #     str1 = "page=1&size=10"