#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pythonProject
# File     : getdatapath.py
# @Time    : 2022/3/30 20:57
# @Author  : lilu

import os

# 项目基本路径
project_path = os.path.split(os.path.dirname(__file__))[0]  # D:\pythonProject\test_api
# 公共类路径
common_path = os.path.dirname(__file__)  # 当面文件的目录路径D:\pythonProject\test_api\common
# 报告路径
report_path = os.path.join(project_path, 'report')  # D:\pythonProject\test_api\report
# 测试用例路径
testcase_path = os.path.join(project_path, 'testcase')  # D:\pythonProject\test_api\testcase
# 测试用例数据路径
testcasedata_path = os.path.join(project_path, 'testcasedata')  # D:\pythonProject\test_api\testcasedata
# 日志存放路径
log_path = os.path.join(project_path, 'log')  # D:\pythonProject\test_api\log
# 配置文件路径
config_path = os.path.join(project_path, 'config')  # D:\pythonProject\test_api\config


def getpath(basepath, path):
    path = os.path.join(basepath, path)
    # print(data_path)
    return path
