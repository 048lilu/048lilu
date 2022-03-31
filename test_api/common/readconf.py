#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pythonProject
# File     : readconf.py
# @Time    : 2022/3/30 23:22
# @Author  : lilu


"""
[test_api_url]
url = http://127.0.0.1:8012
[test_db]
db_host = 127.0.0.1
db_port = 3306
db_user = root
db_pass = root
[concurrent]
thread = 10
processor = 20
"""
from test_api.common.getdatapath import *
from configparser import ConfigParser

config = ConfigParser()
config.read(getpath(config_path, 'conf.ini'), encoding="utf-8")
# print(config.sections())  # ['test_api_url', 'test_db', 'concurrent']
# print(config.options("test_api_url")[0])  # url
# print(config.items('test_api_url'))  # [('url', 'http://119.3.41.185:8012')]
test_url = config.items('test_api_url')[0][1]  # http://119.3.41.185:8012