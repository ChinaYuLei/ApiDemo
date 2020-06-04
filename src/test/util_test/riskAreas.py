#coding:utf-8
import unittest
import requests

class RiskAreas(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def riskAreasAdd(self):
        url = 'http://api-fat.tsingyun.net/open/auth/authorize'
        data = {'loginName': '园区', 'password': '111111'}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=data, headers=headers)
        s = r.json()["data"]["token"]
        return (r.json()["data"]["token"])
        a = "Bearer"
        b = " "
        c = s
        params = a + b + c
        headers1 = {'Authorization': params,
                    'Content-Type': 'application/json'}
        url1 = "http://api-fat.tsingyun.net/base/add/draft/risk/areas"
        data1 = {"deptCode":"146848581318344704","areaName":"区域名称2","orgCode":"CZ1912135","poiList":[],"submitStatus":false}
        r = requests.post(url=url1, data=json.dumps(data1), headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')