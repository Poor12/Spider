# import urllib.parse
# import urllib.request
# from urllib import error
# response=urllib.request.urlopen('https://www.python.org')
# print(type(response))
# print(response.getheader('Server'))
#
# data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
# response=urllib.request.urlopen('http://httpbin.org/post',data=data)
# print(response.read())

# 超时
# import urllib.error
# import socket
# try:
#     response=urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('time out')

# 参数
# from urllib import parse,request
# url='http://httpbin.org/post'
# headers={
#     'User-Agent':'Mozilla/4.0',
#     'Host':'httpbin.org'
# }
# dict={
#     'name':'Germey'
# }
# data=bytes(parse.urlencode(dict),encoding='utf8')
# req=request.request(url=url,data=data,headers=headers,method='POST')
# response=request.urlopen(req)
# print(response.read().decode('utf-8'))

#验证
# from urllib.request import HTTPBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm,build_opener
# from urllib.error import URLError
# username='username'
# password='password'
# url='http://localhost:5000/'
# p=HTTPPasswordMgrWithDefaultRealm()
# p.add_password(None,url,username,password)
# auth_handler=HTTPBasicAuthHandler(p)
# opener=build_opener(auth_handler)
# try:
#     result=opener.open(url)
#     html=result.read().decode('utf-8')
#     print(html)
# except URLError as e:
#     print(e.reason)

# from urllib.request import ProxyHandler
# proxy_handler=ProxyHandler({
#     'http':'http://127.0.0.1:9743',
#     'https':'https://127.0.0.1:9743'
# })
# opener=build_opener(proxy_handler)
# try:
#     response=opener.open('https://www.baidu.com')
#     print(response.read().decode('utf-8'))
# except URLError as e:
#     print(e.reason)

import http.cookiejar
# cookie=http.cookiejar.CookieJar()
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)

# cookies存储
# filename='cookies.txt'
# cookie=http.cookiejar.MozillaCookieJar(filename)
# handler=urllib.request.HTTPCookieProcessor(cookie)
# opener=urllib.request.build_opener(handler)
# response=opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

#cookie读取
#cookie.load('cookies.txt',ignore_discard=True,ignore_expires=True)

# try:
#     response=urllib.request.urlopen('http://cuiqingcai.com/index.htm')
# except error.HTTPError as e:
#     print(e.reason,e.code,e.headers,sep='\n')
# except error.URLError as e:
#     print(e.reason)
# else:
#     print('Request Successfully')
#
# from urllib.parse import urlparse
# result=urlparse('http://www.baidu.com/index.html;user?id=5#comment',scheme='http',allow_fragments=False)
# print(type(result),result)
#
# from urllib.request import urlopen
# from urllib.robotparser import RobotFileParser
# rp=RobotFileParser()
# rp.parse(urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
# # rp.set_url('http://www.jianshu.com/robots.txt')
# # rp.read()
# print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
# print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))