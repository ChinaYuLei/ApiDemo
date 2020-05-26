import requests
import json
import unittest
class testselect1(unittest.TestCase):
    def setUp(self):
        pass


    def test_select1(self):
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
        headers1 = {'Authorization': params,
                    'Content-Type': 'application/json'}
        url1= "http://api-fat.tsingyun.net/machine/page/machine_overhaul"
        data1 = {
            'machineName':'a',
            'transfiniteStatus':'',
            'checkStatus':'',
            'listUrgeStatus':'',
            'machineStatus':'',
            'page': 1,
            'size':15
        }
        r = requests.get(url=url1,params={params:data1},headers=headers1)
        print(r.json()['msg'])
        assertEqual(results['msg'],'ok')
    def tearDown(self):
        pass
if __name__ == '__main__':

 unittest.main()
