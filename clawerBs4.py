# coding:utf-8
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc,'html.parser',from_encoding='utf-8') 

print('获取所有的链接')
links = soup.find_all('a')
for link in links:
    print(link.name, link['href'], link.get_text())

print('获取lacie的链接')
link_node= soup.find('a',href  = 'http://example.com/lacie')
print (link_node.name, link_node['href'], link_node.get_text())

print ('正则表达')
link_node= soup.find('a',href=re.compile(r'ill'))
print (link_node.name, link_node['href'], link_node.get_text())

print ('获取p段落文字')
p_node= soup.find('p',class_="title")
print (p_node.name, p_node.get_text())

print  ('使用select 方法找出含有p标签的元素')
factor1 = soup.select('p') 
print (factor1)
print (factor1[0])
print (factor1[0].text)

print  ('使用select 方法找出含有a标签的元素')
factor2= soup.select('a') 
print (factor2)
print (factor2[0])
print (factor2[0].text)

print ('取得含有特定CSS属性的元素')

print ('找出全部id = title 的元素')
alinks = soup.select('#title')
print (alinks)

print ('找出全部class = sister 的元素')
alinks = soup.select('.sister')
for link in alinks:
    print (link)

print ('找出所有a tag 的href 连结')
alinks = soup.select('a')
for link in alinks:
    print (link['href'])

a=('<a href= "#" qoo=123 abc=456> i am a link</a>')
soup2 = BeautifulSoup(a,'html.parser')
print(soup2.select('a')[0]['href'])


