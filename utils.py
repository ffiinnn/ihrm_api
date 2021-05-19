# 封装公共断言方法
# 给参数加缺省值
def common_assert(case, response, status_code=200, code=10000, message="操作成功"):
    case.assertEqual(status_code, response.status_code)
    case.assertEqual(code, response.json().get("code"))
    case.assertIn(message, response.json().get("message"))
