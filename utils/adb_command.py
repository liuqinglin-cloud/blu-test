import os
import re
import subprocess


def filter_logcat(keyword_reg):
    """
    匹配日志
    :param keyword_reg: 正则表达式
    :return: 日志
    """
    p_obj = subprocess.Popen(
        args="adb logcat -v threadtime",
        stdin=None, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, shell=False)
    with p_obj:
        for line in p_obj.stdout:
            if re.match(keyword_reg, line.decode("utf-8")):
                break
        return line.decode("utf-8")



if __name__ == '__main__':
    pass

