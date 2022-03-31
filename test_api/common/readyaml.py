#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pythonProject
# File     : readyaml.py
# @Time    : 2022/3/30 22:53
# @Author  : lilu

import yaml
from test_api.common.getdatapath import *
"""
读取yaml配置文件
"""


class ReadYaml:
    """读取yaml配置文件"""

    def __init__(self, file_name):
        """
        初始化,并设置实例属性路径名字
        :param file_name:
        """
        self.file_name = file_name

    def read_yaml(self):
        """
        读取yaml文件,返回数据
        :return:
        """
        with open(self.file_name, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)

        return data

    def return_data(self, data_name=None):
        """
        返回数据,如果属性名字为空,则默认返回所有数据
        :param data_name:属性名字
        :return:
        """
        data_ret = self.read_yaml()

        if data_name is None:
            return data_ret
        else:

            return data_ret[data_name]


yaml_data = ReadYaml(file_name=testcasedata)
if __name__ == '__main__':
    data = yaml_data.return_data()
    print(data)
