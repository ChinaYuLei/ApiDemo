import requests
import json
import unittest
class testdel1(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

    def test_del1(self):
        url = 'http://api-fat.tsingyun.net/open/auth/authorize'
        data = {'loginName': 'l', 'password': '111111'}
        headers = {'Content-Type': 'application/json'}
        r = requests.post(url, json=data, headers=headers)
        s = r.json()["data"]["token"]
        return (r.json()["data"]["token"])
        a = "Bearer"
        b = " "
        c = s
        params= a + b + c
        headers1 = {'Authorization' : params }
        url1= "http://api-fat.tsingyun.net/machine/delete/machine_overhaul/132714975356518400"
        data1 = {'machineId', '132714975356518400'}
        r = requests.post(url=url1,params = {params:data1},headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')
if __name__ == '__main__':
    unittest.main()