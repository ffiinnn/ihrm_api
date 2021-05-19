# 运行测试集
# 导入unittest包和测试用例
import time
import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from scripts.test01_login import TestLogin
from scripts.test02_login_params import TestLogin2
# from scripts.test03_login_db import TestLogin3
# from scripts.test01_login2 import LoginTest_tryagain
from scripts.test04_employee import TestEmployee
import configure

# 封装测试套件
# 实例化suite对象
suite = unittest.TestSuite()

# 往套件中加测试用例
# 登录接口测试用例
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestLogin2))
# 员工管理测试用例
# 添加登录类下的指定的测试用例，获取Authorization，解决接口依赖
suite.addTest(TestLogin("test01_success"))
suite.addTest(unittest.makeSuite(TestEmployee))

# 指定文件路径
# format格式化{}内的内容，按时间格式存储
report = configure.BASE_DIR + "/report/report-{}.html".format(time.strftime("%Y%m%d-%H%M%S"))

# 打开文件流
with open(report, "wb") as f:
    # 创建HTMLTestRunner运行器,需要指明文件
    runner = HTMLTestRunner(f, title="接口测试报告")
    # 运行测试套件
    runner.run(suite)
