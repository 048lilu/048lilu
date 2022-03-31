#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pythonProject
# File     : httprequest.py
# @Time    : 2022/3/29 21:50
# @Author  : lilu


import unittest
import requests
from test_api.common.log import console, file_and_console, filelog


class RequestHandler:
    def __init__(self):
        """
        session管理器
        """
        self.session = requests.session()

    def httprequest(self, method, url, params=None, data=None, json=None, headers=None, **keyword):
        """
        请求处理
        :param method:
        :param url:
        :param params:
        :param data:
        :param json:
        :param headers:
        :param keyword:
        :return:
        """
        # 对异常进行捕获
        try:
            """
            封装request请求
            """
            method = method.lower()
            res = self.session.request(method, url, params=params, data=data, json=json, headers=headers, **keyword)
            file_and_console.debug(f'请求方式：{method},请求url：{url},请求参数：{res.request.body},服务器返回结果：{res.text}')
            return res
        except Exception as e:
            file_and_console.exception(e)


# if __name__ == '__main__':
#     # 以下是测试代码
#     # post请求接口
#     url = 'http://119.3.41.185:8012/woniusales/user/login'
#     payload = {
#         "username": "admin",
#         "password": "admin123",
#         "verifycode": "0000"}
#     req = RequestHandler()
#     req.httprequest('post', url, data=payload)