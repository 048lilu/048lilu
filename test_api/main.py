"""
运行整个testcase所有用咧
"""

import unittest

from test_api.testcase.test_login import TestLogin
from BeautifulReport import BeautifulReport


def allTests():
    """
    执行所有的测试用例
    :return:
    """
    suite = unittest.TestSuite()  # 创建测试套件
    loader = unittest.TestLoader()  # 创建加载器
    alltests = loader.discover(start_dir='testcase')  # 找到该地址下的所有用列
    suite.addTests(alltests)  # 找到测试用例添加到测试用例集中
    return suite


# def smokeTest():
#     """
#     挑选特定的用例执行
#     :return:
#     """
#     suite = unittest.TestSuite()
#     loader = unittest.TestLoader()
#     suite.addTest(TestLogin("test_login_2"))  # 添加单个的测试用例
#     allTest = loader.loadTestsFromTestCase(TestLoginDDT)  # 添加一个目录下的测试用例
#     suite.addTests(allTest)
#     return suite


if __name__ == '__main__':
    # runner = unittest.TextTestRunner(verbosity=2)  # 创建用例执行机
    # runner.run(allTests())
    # runner.run(smokeTest())

    '''添加报告'''
    runner = BeautifulReport(allTests())
    runner.report(description='testapi', report_dir='report')
