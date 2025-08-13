import json
import os.path


project_path = os.path.dirname(os.path.dirname(__file__))
header_path = os.path.join(project_path,"config\\header.json")

class ReadJson:

    def __init__(self,file_path):
        self.path = file_path

    def read_json_file(self):
        """
        读取json文件
        :return:
        """
        with open(self.path, encoding="utf-8") as f:
            data = json.load(f)
        return data

    def get_json_by_key(self,key):
        """
        获取json里key对应的值
        :param key:
        :return:
        """
        data = self.read_json_file()
        return data.get(key)

    def write_value(self,data):
        """
        写入json文件
        :param data: 数据
        :return:
        """
        data_value = json.dumps(data)
        with open(self.path,"w") as f:
            f.write(data_value)


header_json = ReadJson(header_path)

if __name__ == "__main__":
    pass

