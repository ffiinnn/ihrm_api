import os
from api.login import loginAPI
# 定义项目的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

# 定义项目基础url地址
BASE_URL = "http://ihrm-test.itheima.net"

# 定义token
TOKEN = None
# 存放头部信息
headers_data = {"Content-Type":"application/json",
                "Authorization":"Bearer a7e165f5-f330-477b-9739-044cf44f603a"
                }

