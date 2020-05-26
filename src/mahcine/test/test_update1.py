import requests
import json
import unittest
class test_update1(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_update1(self):
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
        url1 = "http://api-fat.tsingyun.net/machine/update/machine_overhaul/133406978700476416"
        data1 = {
            {{"id":"133406978700476416",
              "orgCode":"CZ1912112",
              "orgName":"沧州大化",
              "machineNo":"231",
              "machineName":"45",
              "machineTypeCode":"5",
              "machineTypeName":"制药用水设备",
              "checkPeriod":0,
              "nextCheckDate":"2020-04-26",
              "machineStatus":0,
              "transfiniteStatus":0,
              "checkStatus":0,
              "urgeStatus":0,
              "listUrgeStatus":0,
              "manufactureDate":"2020-04-26",
              "transfiniteDate":"2020-05-03",
              "daysRemaining":7,
              "transfiniteDays":0,
              "contactDepartmentCode":"296",
              "contactDepartmentName":"机构1",
              "contactPersonId":"123970679505682432",
              "contactPersonName":"王方亮",
              "updateDepartmentCode":"212",
              "updateDepartmentName":"维修部",
              "updatePersonId":"123970679505682432",
              "updatePersonName":"王方亮",
              "contactPersonTel":"13688888888",
              "remark":"",
              "utime":"2020-04-27 19:11:21",
              "attachmentList":[],
              "ctime":"2020-04-26 14:33:24"}

            }
           }
        r= requests.post(url=url1, data=json.dumps(data1), headers=headers1)
        print(r.json())
        assertEqual(results['msg'], 'ok')
if __name__ == '__main__':
    unittest.main()
