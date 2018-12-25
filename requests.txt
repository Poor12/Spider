import requests
import re
# i=requests.get("https://www.baidu.com/") #response对象
# print(type(i)) #类型
# print(i.status_code) #状态码
# print(type(i.text)) #响应体的类型
# print(i.text) #内容
# print(i.cookies) #cookies
#i=requests.post("http://httpbin.org/post')

#带参数的get请求
# data={
#     'name':'germey',
#     'age':22
# }
# i=requests.get("http://httpbin.org/get",params=data)
# print(i.text)
#print(r.json()) json转化为字典

#知乎话题搜索
# headers={
#     'User-Agent':'Mozilla/5.0'
# }
# r=requests.get("https://www.zhihu.com/explore",headers=headers)
# pattern=re.compile('explore-feed.*?question_link.*?>(.*?)</a>',re.S)
# titles=re.findall(pattern,r.text)
# print(titles)

#图片，视频抓取二进制，再写入文件
# r=requests.get("https://github.com/favicon.ico")
# print(r.text)#字符串
# print(r.content)#二进制
# with open('favicon.ico','wb') as f:#向文件中写入二进制
#     f.write(r.content)

# post请求
# data={'name':'germey','age':'22'}
# r=requests.post("http://httpbin.org/post",data=data)
# print(r.text)

# r=requests.get('http://www.jianshu.com/')
# exit() if not r.status_code==requests.codes.ok else print('request successfully')

# 文件上传
# files={'file':open('favicon.ico','rb')}
# r=requests.post("http://httpbin.org/post",files=files)
# print(r.text)

#获取cookies
# r=requests.get("https://www.baidu.com")
# print(r.cookies)
# for key,value in r.cookies.items():
#     print(key+'='+value)

# headers={
#     'Cookie':'d_c0="AGCmvFqfrQ2PTqcw9KoTLjEhLTjVKq8sSgI=|1527769906"; _zap=a18ccbf0-a11e-4dd1-9fff-600b00c68851; _xsrf=01ux1GugbtEfoj5t50N4IY58oeqiFwVg; l_n_c=1; q_c1=26aead210f9b41b8893e27ef09bb975e|1545657960000|1527769906000; r_cap_id="OGFkYjE1OGVhNjkwNGY4MDkwYTY4ZjJiZThkNDAwZTA=|1545657960|9245970a2005448ded1b6ee224789539122c5c2f"; cap_id="NTZhZDc4NmQ5ZTU2NDYzMmEwNWI0ZjVjZDU3NTIxZGE=|1545657960|91708ace9cf16274618355b89d095dd45e660c61"; l_cap_id="ODJhYTYxOTk5Zjg5NGIxYWJiZjQyM2ZjODY4NjUzZTY=|1545657960|054d264efc417f3928184dad087d6a8dcc4b66c7"; n_c=1; tgw_l7_route=156dfd931a77f9586c0da07030f2df36; capsion_ticket="2|1:0|10:1545660119|14:capsion_ticket|44:YmY4OTIwZGZkOTdkNDBlMWEwNDhjMWJiZjAxMzUyMzU=|b212a9f76aaac7bd9913e662cd833b96434e26b19d5e4b0230477aee27ad2344"; z_c0="2|1:0|10:1545660179|4:z_c0|92:Mi4xOG5ZWEFnQUFBQUFBWUthOFdwLXREU1lBQUFCZ0FsVk5FelVPWFFCNlpSc1Y2R0YtOGtPSC1KSXpHUGlpU1I2aHVn|948d62a1869da671987ced0364e263684a116ff7a81415cfe9f4842463d23aae"; unlock_ticket="ABBKNOTNsggmAAAAYAJVTRvuIFxjSJacqUljmsyjfQMWGGUrHhCM0w=="; __utma=51854390.737906000.1545657964.1545657964.1545660183.2; __utmb=51854390.0.10.1545660183; __utmc=51854390; __utmz=51854390.1545660183.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signin; __utmv=51854390.100--|2=registration_date=20150914=1^3=entry_date=20150914=1',
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0'
# }
# r=requests.get('https://www.zhihu.com',headers=headers)
# print(r.text)

# Cookie='d_c0="AGCmvFqfrQ2PTqcw9KoTLjEhLTjVKq8sSgI=|1527769906"; _zap=a18ccbf0-a11e-4dd1-9fff-600b00c68851; _xsrf=01ux1GugbtEfoj5t50N4IY58oeqiFwVg; l_n_c=1; q_c1=26aead210f9b41b8893e27ef09bb975e|1545657960000|1527769906000; r_cap_id="OGFkYjE1OGVhNjkwNGY4MDkwYTY4ZjJiZThkNDAwZTA=|1545657960|9245970a2005448ded1b6ee224789539122c5c2f"; cap_id="NTZhZDc4NmQ5ZTU2NDYzMmEwNWI0ZjVjZDU3NTIxZGE=|1545657960|91708ace9cf16274618355b89d095dd45e660c61"; l_cap_id="ODJhYTYxOTk5Zjg5NGIxYWJiZjQyM2ZjODY4NjUzZTY=|1545657960|054d264efc417f3928184dad087d6a8dcc4b66c7"; n_c=1; tgw_l7_route=156dfd931a77f9586c0da07030f2df36; capsion_ticket="2|1:0|10:1545660119|14:capsion_ticket|44:YmY4OTIwZGZkOTdkNDBlMWEwNDhjMWJiZjAxMzUyMzU=|b212a9f76aaac7bd9913e662cd833b96434e26b19d5e4b0230477aee27ad2344"; z_c0="2|1:0|10:1545660179|4:z_c0|92:Mi4xOG5ZWEFnQUFBQUFBWUthOFdwLXREU1lBQUFCZ0FsVk5FelVPWFFCNlpSc1Y2R0YtOGtPSC1KSXpHUGlpU1I2aHVn|948d62a1869da671987ced0364e263684a116ff7a81415cfe9f4842463d23aae"; unlock_ticket="ABBKNOTNsggmAAAAYAJVTRvuIFxjSJacqUljmsyjfQMWGGUrHhCM0w=="; __utma=51854390.737906000.1545657964.1545657964.1545660183.2; __utmb=51854390.0.10.1545660183; __utmc=51854390; __utmz=51854390.1545660183.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/signin; __utmv=51854390.100--|2=registration_date=20150914=1^3=entry_date=20150914=1'
# jar=requests.cookies.RequestsCookieJar()
# headers={
#     'Host':'www.zhihu.com',
#     'User-Agent':'Mozilla/5.0'
# }
# for cookie in Cookie.split(';'):
#     key,value=cookie.split('=',1)
#     jar.set(key,value)
# r=requests.get("http://www.zhihu.com",cookies=jar,headers=headers)
# print(r.text)

# 无法获取cookie
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r=requests.get('http://httpbin.org/cookies')
# print(r.text)

# 会话维持
# s=requests.session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r=s.get('http://httpbin.org/cookies')
# print(r.text)

# 忽略警告或捕获到日志
# from requests.packages import urllib3
# urllib3.disable_warnings()
# import logging
# logging.captureWarnings(True)
# reponse=requests.get('https://www.12306.cn',verify=False)
# print(reponse.status_code)

#指定一个本地证书
# response=requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))

#http代理和socks代理
# proxies={
#     "http":"http://10.10.1.10:3128",
#     "https":"http://10.10.1.10:1080",
# }
# requests.get("https://www.taobao.com",proxies=proxies)

#超时设置
#r=requests.get("https://www.taobao.com",timeout=1)

#身份验证
# from requests.auth import HTTPBasicAuth
# r=requests.get('http://localhost:5000',auth=HTTPBasicAuth('username','password'))
# print(r.status_code)
# from requests_oauthlib import OAuth1

# from requests import Request,Session
# url='http://httpbin.org/post'
# data={
#     'name':'germy'
# }
# headers={
#     'User-Agent':'Mozilla/5.0'
# }
# s=Session()
# req=Request('POST',url,data=data,headers=headers)
# prepped=s.prepare_request(req)
# r=s.send(prepped)
# print(r.text)

