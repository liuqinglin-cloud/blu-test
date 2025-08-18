import redis
from utils.handle_ini import environment_ini

class HandleRedis:

    def __init__(self, environment,db=0):
        """
        连接数据库
        :param environment:环境，如test_hk
        :param db:db
        """
        host = environment_ini.get_value("redis",environment)
        self.__redis = redis.StrictRedis(host=host, port=6379, password='12345678',db=db, decode_responses=True)

    def count_prefix(self,prefix):
        """
        统计符合前缀的key数量
        :param prefix: 前缀，比如'BluUc:GROUP:USERS*'
        :return: 符合前缀的key数量
        """
        cursor = 0
        # 使用 SCAN 命令遍历 Keys
        keys = []
        while True:
            cursor, found_keys = self.__redis.scan(cursor, match=prefix)
            keys.extend(found_keys)
            if cursor == 0:
                break
        count = len(keys)
        return count

    def __del__(self):
        """
        销毁对象时close
        :return:
        """
        self.__redis.close()

    def close(self):
        """
        关闭
        :return:
        """
        self.__del__()


if __name__ == '__main__':
    redis = HandleRedis("test_hk")
    data = redis.count_prefix('BluUc:GROUP:USERS*')
    print(data)
