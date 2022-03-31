#!/usr/bin/env python
# gbk
# @Project : pythonProject
# File     : log.py
# @Time    : 2022/3/28 21:53
# @Author  : lilu

import logging.config
import os

project_basic_path = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
logging.config.fileConfig(os.path.join(project_basic_path, 'config', 'logging.ini'), encoding='utf-8')
# 获取记录器
console = logging.getLogger('root')
filelog = logging.getLogger('file')
file_and_console = logging.getLogger('fileAndConsole')

#     # print(project_basic_path)  ==>#D:\pythonProject\test_api
#     # logger_conf_path = os.path.join(project_basic_path, 'config', 'logging.ini')
#     # print(logger_conf_path)   #===>D:\pythonProject\test_api\config\logging.ini
