import unittest
from ddt import ddt, file_data, unpack
from test_api.common.httprequest import RequestHandler
from test_api.common.getdatapath import *
from test_api.common.readconf import *


@ddt
class TestLogin(unittest.TestCase):

    @file_data(getpath(testcasedata_path, 'login.yaml'))
    @unpack
    def test_login(self, **kwargs):
        url = test_url + kwargs.get("url")
        data = kwargs.get("data", {})
        headers = kwargs.get("headers", {})
        expect = kwargs.get("expect", {})
        res = RequestHandler().httprequest('post', url, data=data, headers=headers)
        self.assertIn(expect, res.text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
