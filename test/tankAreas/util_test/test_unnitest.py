#coding:utf-8
import unittest
import requests

class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def tankAreas_add(self):
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
        url1 = "http://api-fat.tsingyun.net/base/add/tank_areas"
        data1 = {"tanks":[],"orgCode":"CZ1912110","tankAreaName":"储罐区1","fireHazardCode":"101311","riskRatingCode":"102312","cofferdam":0,"area":"10","firePassage":0,"minimumDistance":"10","handlingMode":"装卸方式","geo":{"request3d":null,"request2d":"{\"parts\":[3],\"type\":\"REGION\",\"points\":[{\"x\":117.64065448782824,\"y\":38.36419284738692},{\"x\":117.64278440348698,\"y\":38.364087326755666},{\"x\":117.64275893748034,\"y\":38.363714591258365},{\"x\":117.64052679110641,\"y\":38.36371264129769},{\"x\":117.64065448782824,\"y\":38.36419284738692}]}"},"tankIds":[],"submitStatus":false}
        r = requests.post(url=url1, data=json.dumps(data1), headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')