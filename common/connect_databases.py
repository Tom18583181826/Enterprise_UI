import pymysql
from pymysql import cursors


class ConnectDatabases:
    def __init__(self, host="127.0.0.1", user="root", password="mima=1509957150", database="guest", charset="utf8",
                 port=3306):
        self.connect = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset,
            port=port
        )

    # 查询数据
    def query_data(self, sql, query_type, args=None):
        try:
            with self.connect.cursor() as cursor:
                if query_type == all:
                    cursor.execute(sql, args)
                    all_data = cursor.fetchall()
                    return all_data
                else:
                    cursor.execute(sql, args)
                    one_data = cursor.fetchone()
                    return one_data
        finally:
            self.connect.close()

    # 执行sql语句
    def execute_sql(self, sql, args=None):
        try:
            with self.connect.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
                try:
                    rows = cursor.execute(sql, args)
                    if rows == 0:
                        raise Exception("受影响的行数为0，执行失败")
                    self.connect.commit()
                    return True
                except Exception as e:
                    self.connect.rollback()
                    print("执行失败！", e)
                    return False
        finally:
            self.connect.close()


if __name__ == '__main__':
    sql1 = 'select * from sign_event;'
    test1 = ConnectDatabases().query_data(sql1, all)
    print(test1)
