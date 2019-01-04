import requests
from pyquery import PyQuery as pq
import json
import csv
# url='https://www.zhihu.com/explore'
# headers={
#     'User-Agent':'Mozilla/5.0'
# }
# html=requests.get(url,headers=headers).text
# print(html)
# doc=pq(html)
# items=doc('.explore-tab .feed-item').items()
# for item in items:
#     question=item.find('h2').text()
#     author=item.find('.author-link-line').text()
#     answer=pq(item.find('.content').html()).text()
#     # file=open('explore.txt','a',encoding='utf-8')
#     # file.write('\n'.join([question,author,answer]))
#     # file.write('\n'+'='*50+'\n')
#     # file.close()
#     with open('explore.txt','a',encoding='utf-8') as file:
#         file.write('\n'.join([question,author,answer]))
#         file.write('\n'+'='*50+'\n')
# str='''
# [{
#     "name":"Bob",
#     "gender":"male",
#     "birthday":"1992-10-18"
# },{
#     "name":"Selina",
#     "gender":"female",
#     "birthday":"1995-12-12"
# }]
# '''
# print(type(str))
# data=json.loads(str)
# print(data[0]['name'])
# print(type(data))
# print(json.dumps(data))
# with open('data.json','a') as file:
#     file.write(json.dumps(data,indent=2))
# with open('data.csv','w') as csvfile:
#     writer=csv.writer(csvfile,delimiter=' ')
#     writer.writerow(['id','name','age'])
#     writer.writerow(['10001','mike','22'])
# with open('data.csv','w') as csvfile:
#     fieldname=['id','name','age']
#     writer=csv.DictWriter(csvfile,fieldnames=fieldname)
#     writer.writerow({'id':'10005','name':'mike','age':22})
# with open('data.csv','r') as csvfile:
#     reader=csv.reader(csvfile)
#     for row in reader:
#         print(row)
