from bs4 import BeautifulSoup
html='''
<p><a href="http://example.com/lacie" class="sister" id="link2">lacie<p name="cc">999</p></a><c></c></p>
'''
soup=BeautifulSoup(html,'lxml')
print(soup.prettify())
print(soup.a)
print(soup.a.string)
print(soup.p.contents)
print(soup.a['class'])
print(soup.p.a.string)
for i,child in enumerate(soup.p.children):
    print(i,child)
for i,child in enumerate(soup.p.descendants):
    print(i,child)
print(soup.a.parent)
print(list(enumerate(soup.a.parents)))
print('next sibling',soup.a.next_sibling)
print(soup.find_all(id='link2'))
print(soup.find_all(attrs={'id':'link2'}))
for a in soup.find_all(id='link2'):
    for p in a.find_all(name='p'):
        print(p.string)
print(soup.find_all(text='999'))
print(soup.find(text='999'))
print(soup.select('.sister p'))
print(soup.select('.sister p')[0].get_text())