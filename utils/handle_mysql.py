import pymysql.cursors
from utils.handle_ini import environment_ini


class HandleMysql:

    def __init__(self, environment, database):
        """
        连接数据库
        :param environment:环境，如test_hk
        :param database:数据库
        """
        host = environment_ini.get_value("mysql", environment)
        try:
            self.__conn = pymysql.connect(
                host=host,
                user="root",
                passwd="123456",
                db=database,
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor)
            self.connected = True
        except:
            print(f"{environment}环境{database}数据库连接失败")

    def insert(self, table, val_obj):
        """
        插入数据
        :param table:表名
        :param val_obj:插入数据
        :return: 结果
        """
        sql_top = 'INSERT INTO ' + table + ' ('
        sql_tail = ') VALUES ('
        try:
            for key, val in val_obj.items():
                sql_top += key + ','
                sql_tail += val + ','
            sql = sql_top[:-1] + sql_tail[:-1] + ')'
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return self.__conn.insert_id()
        except:
            self.__conn.rollback()
            return False

    def update(self, table, val_obj, range_str):
        """
        更新数据，慎用
        :param table:表名
        :param val_obj:更新数据
        :param range_str:条件
        :return: 结果
        """
        sql = 'UPDATE ' + table + ' SET '
        try:
            for key, val in val_obj.items():
                sql += key + '=' + val + ','
            sql = sql[:-1] + ' WHERE ' + range_str
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except:
            self.__conn.rollback()
            return False

    def delete(self, table, range_str):
        """
        删除数据，慎用
        :param table:表名
        :param range_str:条件
        :return: 结果
        """
        sql = 'DELETE FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.rowcount
        except:
            self.__conn.rollback()
            return False

    def select_one(self, table, factor_str, field='*'):
        """
        查询数据
        :param table:表名
        :param factor_str:条件
        :param field:查询字段，默认所有
        :return: 结果
        """
        sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + factor_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]
        except:
            return False

    def select_more(self, table, range_str, field='*'):
        """
        查询数据
        :param table:表名
        :param range_str:条件
        :param field:查询字段，默认所有
        :return: 结果
        """
        sql = 'SELECT ' + field + ' FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()
        except:
            return False

    def count(self, table, range_str='1'):
        """
        计数
        :param table:表名
        :param range_str:条件
        :return: 结果
        """
        sql = 'SELECT count(*)res FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except:
            return False

    def sum(self, table, field, range_str='1'):
        """
        求和
        :param table:表名
        :param field:字段
        :param range_str:条件
        :return: 结果
        """
        sql = 'SELECT SUM(' + field + ') AS res FROM ' + table + ' WHERE ' + range_str
        try:
            with self.__conn.cursor() as cursor:
                cursor.execute(sql)
            self.__conn.commit()
            return cursor.fetchall()[0]['res']
        except pymysql.Error as e:
            return False

    def __del__(self):
        """
        销毁对象时关闭数据库
        """
        try:
            self.__conn.close()
        except pymysql.Error as e:
            pass

    def close(self):
        """
        关闭数据库
        """
        self.__del__()


if __name__ == '__main__':
    mysql = HandleMysql("test_hk", "blu-user-center")
    data = mysql.count("user", "country = 'US'")
    print(data)
