import requests
import json
import unittest
class test_add1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_add1(self):
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
            "daysRemaining": "",
            "transfiniteDays": "",
            "machineStatus": '0',
            "machineTypeCode": "6",
            "urgeStatus": "",
            "transfiniteDate": "2020-04-29",
            "nextCheckDate": "",
            "remark": "",
            "contactPersonTel": "13688888888",
            "machineName": "1肉肉肉",
            "checkStatus": "",
            "attachmentList": [],
            "contactPersonId": "123970679505682433",
            "transfiniteStatus": "",
            "orgCode": "CZ1912112"
            , "checkPeriod": "0",
            "manufactureDate": "2020-04-21",
            "machineNo": "232432224444",
            "utime": "2020-04-26 12:57:21",
            "updatePersonId": "123970679505682432",
            "updateDepartmentCode": "212",
            "contactDepartmentCode": "214"}
        r= requests.post(url=url1, data=json.dumps(data1), headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')
if __name__ == '__main__':
    unittest.main()
