#coding:utf-8
import unittest
import requests
from src.test.util_test.login import TestLogin

class RiskAreas(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_login(self):
        result = self.TestLogin.login()
        print(result)
        print(type(result))
        print(result['msg'])
        self.assertEqual(result['msg'], 'ok')
    def riskAreasAdd(self):
        test = TestLogin()
        test.login()
        headers = {'Authorization': '',
                    'Content-Type': 'application/json'}
        url = "http://api-fat.tsingyun.net/base/add/draft/risk/areas"
        data = {"deptCode":"146848581318344704","areaName":"区域名称2","orgCode":"CZ1912135","poiList":[],"submitStatus":false}
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        print(r.json())
        assertEqual(results['msg'], 'ok')