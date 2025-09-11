import paramiko
from handle_ini import environment_ini


class Linux:

    def __init__(self, server_name, environment="test_hk"):
        """
        连接服务器
        :param server_name: 服务名字
        :param environment: 环境，默认test_hk
        """
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname = environment_ini.get_value(environment, server_name)
        self.ssh.connect(hostname, 22, "cloudapp", "admin")

    def __del__(self):
        """
        销毁对象时close
        """
        self.ssh.close()

    def close(self):
        """
        关闭
        """
        self.__del__()

    def execute(self,command):
        """
        执行命令
        :param command: 命令
        :return: 结果
        """
        stdin, stdout, stderr = self.ssh.exec_command(command)
        result = stdout.read().decode()
        return result

if __name__ == '__main__':
    linux = Linux("营销")
    data = linux.execute("ls")
    print(data)
