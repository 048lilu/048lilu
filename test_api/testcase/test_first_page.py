import unittest
import requests
from ddt import ddt, data, file_data, idata, unpack
import re

@ddt
class TestFirstPage(unittest.TestCase):
    @file_data("../testcasedata/firstpage.yaml")
    def test_first_page(self, title):
        res = requests.get('http://119.3.41.185:8012/woniusales')
        pattern = re.compile(r'<title>(.+?)</title>')
        actual_result = pattern.findall(res.text)
        self.assertEqual(actual_result[0], title)