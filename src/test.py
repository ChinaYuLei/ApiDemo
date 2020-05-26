import requests


phpurl = "http://XXXX"
interface = "/api/user/auth/beginSession"
requrl = phpurl + interface

header={"content-type":"application/json"}
reqparams = {'c':'{"cc":1602,"ct":20,"dt":1,"ov":17,"p":14584,"v":"9.1.0"}', 'd': '{}'}
timeout = 10.0

# get request exp
getrep = requests.get(url=requrl,headers=header, params=reqparams,timeout=timeout)
print(getrep.text)
print(getrep.json)

# post request exp
postrep = requests.post(url=requrl,headers=header, params=reqparams,timeout=timeout)
print(postrep.text)