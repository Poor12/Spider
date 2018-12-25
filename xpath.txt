from lxml import etree
text='''
<div>
<ul>
<li class="item-0" name="aaa"><a href="link1.html">first item</a></li>
<li class="item-1 item-3"><a href="link2.html">second item</a>
</ul>
</div>
'''
html=etree.HTML(text)
#html=etree.parse()
result=etree.tostring(html)
result1=html.xpath('//*')
result2=html.xpath('//li/a')#直接子节点
result3=html.xpath('//li//a')#子孙子节点
result4=html.xpath('//a[@href="link1.html"]/../@class')
result5=html.xpath('//a[@href="link1.html"]/parent::*/@class')
result6=html.xpath('//li/a/text()')
result7=html.xpath('//li//text()')
result8=html.xpath('//li/a/@href')
result9=html.xpath('//li[contains(@class,"item-1")]/a/text()')
result10=html.xpath('//li[@class="item-0" and @name="aaa"]/a/text()')
result11=html.xpath('//li[last()-1]/a/text()')
result12=html.xpath('//li[1]/descendant::span')#节点轴选择
print(result11)
# print(result.decode('utf-8'))

