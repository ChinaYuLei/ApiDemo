import time
import unittest
from HTMLTestRunner import  HTMLTestRunner

from src.mahcine.test import test_add1
from src.mahcine.test import test_del1
from src.mahcine.test import test_select1
from src.mahcine.test import test_check1
from src.mahcine.test import test_update1
from src.mahcine.test import test_list1
info_type = 1
def test_text_write():
        fp = open("./log/log.txt", "a+")
        # 获取系统当前的运行时间（这行代码的运行时间）
        e_t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # 获取当前函数名称
        f_n = test_text_write.__name__

        # 模拟信息类型的判断

        type = "info"

        if info_type == 0:
            type = "info"
        elif info_type == 1:
            type = "warning"
        elif info_type == 2:
            type = "error"
        else:
            type = "exception"

        # 组合一条信息
        info = "[" + e_t + "]" + "[" + type + "]" + f_n + "\n"
        print(info)

        # 将info 记录到log中
        fp.write(info)
        # 关闭文件
        fp.close()
test_text_write()
if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(test_add1.test_add1('test_add1'))
    suite.addTest(test_del1.testdel1('test_del1'))
    suite.addTest(test_select1.testselect1('test_select1'))
    suite.addTest(test_check1.test_check1('test_check1'))
    suite.addTest(test_update1.test_update1('test_update1'))
    suite.addTest(test_list1.test_list1('test_list1'))
    res_name = './result/' + str(time.strftime("%Y-%m-%d %H_%M_%S")) + '.html'
    fp = open(res_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title="测试报告", description="用例执行情况:")
    runner.run(suite)
    fp.close()
    test_text_write()
