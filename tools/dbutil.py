# 导入pymysql包
import pymysql
# 创建数据库工具类dbutil
class DBUtil:
    # 初始化类属性
    __conn = None
    __cursor = None

# 1、创建连接(私有类方法)
    @classmethod
    def __get_conn(cls):
        # 如果连接对象不存在或者为空
        if cls.__conn is None:
            # 创建连接对象（赋值）
            cls.__conn = pymysql.connect(host="localhost",
                                         port=3306,
                                         user="root",
                                         password="root",
                                         database="books")
        # 返回连接对象的值
        return cls.__conn

# 2、创建游标(私有类方法)
    @classmethod
    def __get_cursor(cls):
        # 如果游标不存在或者为空
        if cls.__cursor is None:
            # 创建游标。（调用cls.__get_conn()返回的是连接对象的值）
            cls.__cursor = cls.__get_conn().cursor()
        # 返回游标
        return cls.__cursor

# 3、执行sql
    @classmethod
    # 定义执行方法(公有类方法)，设置形参sql
    def execute_sql(cls, sql):
        # try没有异常就执行
        try:
            # 获取游标对象,cls.__get_cursor()方法返回游标的值
            cursor = cls.__get_cursor()
            # 调用游标对象的execute(sql)方法
            cursor.execute(sql)
            # 判断如果sql是select
            # sql.split()[0].lower() 先对字符串sql进行切片（默认按空格），取第一个元素，把元素转成小写字母
            if sql.split()[0].lower() == "select":
                # 返回所有数据
                return cursor.fetchall()
            # 如果不是select
            else:
                # 提交事务
                # 调用连接对象的commit方法
                cls.__conn.commit()
                # 返回受影响的行数
                return cursor.rowcount

        # except如果捕捉到异常
        except Exception as e:
            # 事务回滚
            # 调用连接对象的rollback方法
            cls.__conn.rollback()
            # 打印异常信息
            print(e)

        # finally始终执行
        finally:
            # 关闭游标,调用关闭游标方法
            cls.__close_cursor()
            # 关闭连接,调用关闭连接方法
            cls.__close_conn()

# 4、关闭游标(私有类方法)
    @classmethod
    def __close_cursor(cls):
        # 如果游标存在
        if cls.__cursor:
            # 关闭游标
            cls.__cursor.close()
            # 重置游标
            cls.__cursor = None

# 5、关闭连接(私有类方法)
    @classmethod
    def __close_conn(cls):
        # 如果连接存在
        if cls.__conn:
            # 关闭连接
            cls.__conn.close()
            # 重置连接
            cls.__cursor = None
