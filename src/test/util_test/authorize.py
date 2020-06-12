#coding:utf-8
import requests
import unittest

class TestLogin(unittest.TestCase):



    def login(self):
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
        #post请求：请求正文是application/x-www-form-urlencoded
        # response = requests.post(
        #     url='http://api-fat.tsingyun.net/open/auth/authorize',
        #     data = {'loginName': '园区', 'password': '111111'},
        #     headers={'Content-Type': 'application/json'})
        print()