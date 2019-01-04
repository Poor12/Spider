import re
# content='''Hello 123 4567 world_this
# is a regex demo'''
# print(len(content))

# result=re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
# print(result)
# print(result.group())
# print(result.span())

# 括号对应一个分组
# result1=re.match('^Hello\s(\d+)\s',content)
# print(result1.group(0))
# result2=re.match('^Hello.*demo$',content)
# print(result2.group())

#非贪婪匹配
# result=re.match('^He.*?(\d+\s\d+).*demo$',content)
# print(result.group(1))

# 修饰符 re.S匹配换行符 re.I对大小写不敏感
# result=re.match('^He.*?(\d+\s\d+).*demo$',content,re.S)
# print(result.group())

# 转义匹配
# content='(百度)www.baidu.com'
# result=re.match('\(百度\)\w+\.\w+\.\w+',content)
# print(result.group())

#search搜索第一个结果，findall搜索所有结果
# content='Extra strings hello 12345678 world_this is a regex demo extra stings'
# result=re.search('he.*?\d+\s',content,re.S)
# print(result.group())

#sub替换字符
# content='54adsadw343ald4342'
# content=re.sub('\d+','',content)
# print(content)

# content1='2016-12-15 12:00'
# content2='2016-12-16 12:55'
# pattern=re.compile('\d+:\d+')
# result1=re.sub(pattern,'',content1)
# result2=re.sub(pattern,'',content2)
# print(result1,result2)