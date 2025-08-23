import configparser
import os.path


project_path = os.path.dirname(os.path.dirname(__file__))
test_user_path = os.path.join(project_path,"config\\test_user.ini")
translation_path = os.path.join(project_path,"config\\translation.ini")
local_element_android_path = os.path.join(project_path,"config\\local_element_android.ini")
local_element_ios_path = os.path.join(project_path,"config\\local_element_ios.ini")
device_path = os.path.join(project_path,"config\\device.ini")
environment_path = os.path.join(project_path,"config\\environment.ini")


class HandleIni:

    def __init__(self,file_path):
        self.path = file_path

    def load_ini(self):
        """
        加载文件
        :return:
        """
        try:
            cf = configparser.ConfigParser()
            cf.read(self.path, encoding="utf-8-sig")
            return cf
        except:
            print("文件有误")

    def get_value(self,section,key):
        """
        获取文件数据
        :param section:section
        :param key:key
        :return:
        """
        cf = self.load_ini()
        try:
            data = cf.get(section, key)
        except Exception:
            print("没有获取到ini文件value值")
            data = None
        return data


test_user_ini = HandleIni(test_user_path)
translation_ini = HandleIni(translation_path)
local_element_android_ini = HandleIni(local_element_android_path)
local_element_ios_ini = HandleIni(local_element_ios_path)
device_ini = HandleIni(device_path)
environment_ini = HandleIni(environment_path)

if __name__ == '__main__':
    print(local_element_ios_path)
    pass