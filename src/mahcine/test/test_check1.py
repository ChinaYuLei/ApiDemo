import requests
import json
import unittest
class test_check1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_check1(self):
        url = 'http://api-fat.tsingyun.net/open/auth/authorize'
        data = {'loginName': 'l', 'password': '111111'}
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
        url1 = "http://api-fat.tsingyun.net/machine/add/machine_overhaul"
        data1 = {
            {"checkPeriod":"0",
             "checkContent": "级",
             "checkerId": "123970679505682432",
             "transfiniteDate": "2020-04-28",
             "checkTime": "2020-04-27 18:51:18",
             "machineStatus": 0,
             "checkDepartmentCode": "214"}
           }
        r= requests.post(url=url1, data=json.dumps(data1), headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')
if __name__ == '__main__':
    unittest.main()
