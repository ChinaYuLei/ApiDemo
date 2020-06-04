#coding:utf-8
import unittest
from src.test.util_test.riskAreas import RiskAreas
from src.test.util_test.tankAreas import Test
from src.test.util import HTMLTestRunner
from src.test.util.send_mail import SendEmail

class Runmain():
    def __init__(self):
        self.send_mail = SendEmail()

    def run_case(self):
        suite = unittest.TestSuite()

        # 2种用法：第一种suite.addTest()
        # suite.addTest(Case('test_case01'))
        # suite.addTest(Case('test_case02'))
        # suite.addTest(Test('test_01'))
        # suite.addTest(Test('test_02'))

        #2种用法：第二种suite.addTests()
        suite.addTests(map(Test, ["tankAreas_add"]))
        suite.addTests(map(RiskAreas, ["riskAreasAdd"]))

        # # 输出结果：测试结果直接输出在控制台
        # unittest.TextTestRunner().run(suite)

        # 输出结果：将测试结果以report.html形式生成
        st = open('../report/report.html', 'wb')
        HTMLTestRunner.HTMLTestRunner(stream=st, title=u'接口自动化测试报告', description=u'测试者：yl').run(suite)

        # #发送邮件带测试报告附件
        self.send_mail.send_main()

if __name__ == '__main__':
    run = Runmain()
    run.run_case()
