#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project : pythonProject
# File     : readexcel.py
# @Time    : 2022/3/30 22:53
# @Author  : lilu


import openpyxl

"""

读取Excel表格
1.打开表格
2.读取表头
3.读取所有内容

"""
from class_2.common.read_ymal import yaml_data

# file_path = '../config/data.yaml'
filename = yaml_data.return_data()
file_name= filename['filename']
print(file_name)

class ExcelMethod:
    """定义一个类方法,"""

    def __init__(self):
        """路径名字是固定的,所以定义为实例属性"""
        self.filename = file_name

    def open_excel(self, name):
        """
        打开excel表格,
        :param name: 文件sheet名字
        :return:
        """
        wb = openpyxl.load_workbook(self.filename)
        sheet = wb[name]
        return sheet

    def red_title(self, name):
        """
        读取excel表格第一行表头,并返回一个列表
        :param name:
        :return:
        """
        sheet1 = self.open_excel(name)
        row = sheet1[1]
        title_list = []
        for sheet in row:
            # print(sheet)
            title_list.append(sheet.value)
        return title_list

    def red_all(self, name):
        """
        读取excel表格里除了表头以外所有数据,并返回一个列表嵌套字典
        :param name:
        :return:
        """
        row = self.open_excel(name)
        data_row = list(row.rows)
        title = self.red_title(name)
        print(title)
        data_list = []
        for data in data_row[1:]:
            data_dict = []
            for item in data:
                #     data_dict[title[i]] = data_dict[item.value]
                data_dict.append(item.value)
            data_list.append(dict(zip(title, data_dict)))
        return data_list


if __name__ == '__main__':
#     filename = r'F:\cases.xlsx'
    eb = ExcelMethod().red_all('Sheet1')
    print(eb)

