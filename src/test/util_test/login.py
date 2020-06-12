import requests
import unittest

class TestLogin(unittest.TestCase):
    def login(self):
        def get_authorization():
            return base64.b64encode(uae_name + ":" + uae_passwd);
        header = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Authorization": 'Basic {}'.format(get_authorization()),
            "Connection": "keep-alive",
            "Host": "api-fat.tsingyun.net",
            "Origin": "http://beta.biz.tsingyun.net",
            #"Referer": "http://beta.biz.tsingyun.net/admin/login?redirectURL=http%3A%2F%2Fbeta.biz.tsingyun.net%2Fadmin%2Fenterprise%3Fpage%3D1%26size%3D15%26orgCode%3D%26checkStatus%3D",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        body = {"key1": "value1",
             "key2": "value2"}  # 这里账号密码就是抓包的数据
        s = requests.session()
        login_url = "http://api-fat.tsingyun.net/open/auth/authorize"   #　自己找带token网址
        login_ret = s.post(login_url, headers=header, data=body)
        # 这里token在返回的json里，可以直接提取
        token = login_ret.json()[{"Authorization"}]
        # 这是登录后发的一个post请求
        post_url = "http://api-fat.tsingyun.net/open/auth/authorize"
        # 添加token到请求头
        header[{"Authorization"}] = token
        # 如果这个post请求的头部其它参数变了，也可以直接更新
        header["Content-Length"] = ""
        body1 = {
          "key": "value"
          }
        post_ret = s.post(post_url, headers=header, data=body1)
        print(post_ret.content)