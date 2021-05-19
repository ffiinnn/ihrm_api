import requests

class loginAPI2:
    # 定义初始化url方法
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def req_login2(self, session, mobile, password):
        login_data = {"mobile":mobile, "password":password}
        return session.post(url=self.login_url, json=login_data)
