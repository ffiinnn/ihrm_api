# 被测试接口的封装
# 导包
import requests
# 定义类
class loginAPI:
    # 类执行的时候主动被调用的方法
    def __init__(self):
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    # 登录方法
    def login(self, session, mobile, password):
        # 定义请求体中的json文件，由外部文件传实参
        login_data = {
                        "mobile":mobile,
                        "password":password
                      }
        # 发送请求
        return session.post(url=self.login_url, json=login_data)
