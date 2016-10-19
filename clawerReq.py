# coding:utf-8
from pip._vendor import requests
# from pip._vendor.lockfile.sqlitelockfile import unicode
res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8' # 知晓编码方式是为了后续的解读，也可使用unicode 范围更大
str = res.text
print (str)

print (type(str))



