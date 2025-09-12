import time
import paramiko
import select
from handle_ini import environment_ini


class Ssh:

    def __init__(self, server_name, environment="test_hk"):
        """
        连接服务器
        :param server_name: 服务中文简称
        :param environment: 环境，默认test_hk
        """
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        server_host = environment_ini.get_value(environment, server_name)
        self.server = server_host.split("=")[0]
        host = server_host.split("=")[1]
        self.ssh.connect(host, 22, "cloudapp", "admin")

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

    def execute_channel(self, command):
        """
        执行命令返回结果后关闭
        :param command: 命令
        :return: 结果
        """
        stdin, stdout, stderr = self.ssh.exec_command(command)
        result = stdout.read().decode()
        print(result)
        return result

    def tail_realtime(self, key=None, rows=200):
        """
        tail实时查看日志
        :param key: grep关键字，默认None
        :param rows: 行数，默认200
        """
        transport = self.ssh.get_transport()
        channel = transport.open_session()
        channel.get_pty()
        if key is None:
            command = f"tail -{rows}f /data/logs/{self.server}/{self.server}.log"
        else:
            command = f"tail -{rows}f /data/logs/{self.server}/{self.server}.log | grep '{key}'"
        channel.exec_command(command)
        while True:
            if channel.exit_status_ready():
                break
            try:
                rl, wl, el = select.select([channel], [], [])
                if len(rl) > 0:
                    recv = channel.recv(1024)
                    print(recv.decode('utf-8', 'ignore'))
            except KeyboardInterrupt:
                print("Caught control-C")
                channel.send("\x03")
                channel.close()

    def shell_channel(self):
        """
        交互式shell
        """
        channel = self.ssh.invoke_shell()
        while True:
            try:
                command = input('(输入linux命令)~:')
                channel.send(command + '\n')
                time.sleep(1)
                if channel.recv_ready():
                    output = channel.recv(1024).decode('utf-8')
                    print(output)
            except KeyboardInterrupt:
                print("Caught control-C")
                channel.send("\x03")
                channel.close()

    def cat_grep_log(self, key, rows=200):
        """
        grep日志，执行后close
        :param key: 关键字
        :param rows: 行数，默认200
        :return: 有日志返回True，else False
        """
        command = f"cat /data/logs/{self.server}/{self.server}.log | tail -n {rows} | grep {key}"
        result = self.execute_channel(command)
        return True if result else False


if __name__ == '__main__':
    ssh = Ssh("营销")
    ssh.tail_realtime()
    pass