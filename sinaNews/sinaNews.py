# coding:utf-8
#天善智能 Python网络爬虫实战
from bs4 import BeautifulSoup
from datetime import datetime
from pip._vendor import requests
from future.types.newbytes import unicode


res = requests.get('http://news.sina.com.cn/china/')
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text,'html.parser')

#lesson 8 
for news in soup.select('.news-item'):
    if len(news.select('h2'))>0:
        h2 = news.select('h2')[0].text
        time = news.select('.time')[0].text
        a = news.select('a')[0]['href']
#         print (','.join([time,h2,a]))
#上面这个是为实现列表的所有元素都实现中文输出，否则即使所有元素都是utf-8格式也没有办法保证列表形式下的输出


#lesson 9-10-11 抓取新闻内文页面
res = requests.get("http://news.sina.com.cn/c/gat/2016-09-06/doc-ifxvqctu6364150.shtml")
res.encoding = unicode
soup = BeautifulSoup(res.text,"html.parser")
h1 = soup.select("#artibodyTitle")[0].text
# .time-source下内容还包括了内容来源，需要筛选
# 如果输出中有//, 添加strip()来去除
# 注意encode()函数不改变对象自身编码，只返回一个指定编码的对象
timesource = soup.select(".time-source")[0].contents[0].strip().encode('utf-8')  
# 内容来源
textsource = soup.select(".time-source span a")[0].text
# from datetime import datetime
# dt = datetime.strptime(timesource,'%Y年%m月%m日%H:%M')
# dt.strftime('%Y-%m-%d') 

#获取文章内文
article = []
#[:-1]将最后的编辑的部分去掉,strip移除左右空白/u3000
for p in soup.select("#artibody p")[:-1]:
    article.append(p.text.strip())
# import uniout  #针对list中的中文显示
print(article)
#\n来分隔list中的各个元素, 也可以用空格等符号隔开
print (','.join(article))

#取得编辑名称
#strip 去掉前缀
editor = soup.select('.article-editor')[0].text.encode('utf-8').strip('责任编辑：')
print (editor)

#取得评论数
#如下方式得到内容为[<span id='commentCount1'></span>]
commentCount = soup.select('#commentCount1')
print (commentCount)
#地毯式搜索，发现在JS的info?文件中
#观察这个url，可以发现newsid即是新闻界面url中的数字。
#再者，后面的jsvar存储了时间戳，我们可以去掉试试
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fxvqctu6364150&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20&jsvar=loader_1473149812798_72440978')
comments = requests.get('http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fxvqctu6364150&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20')
import json
jd = json.loads(comments.text.strip('var data='))
count = jd['result']['count']['total']
print(count)

#剖析新闻标识
#观察url http://news.sina.com.cn/c/gat/2016-09-06/doc-ifxvqctu6364150.shtml
newsurl='http://news.sina.com.cn/c/gat/2016-09-06/doc-ifxvqctu6364150.shtml'
newsid = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
print (newsid)
#或使用正规表达式
import re
m = re.search('doc-i(.+).shtml',newsurl)
print (m)
print (m.group(0))
print (m.group(1))

#将抓取评论数方法整理成一函式
#url的格式
commentURL= 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=gn&newsid=comos-fxvqctu6364150&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
commentURL.format(newsid)

import re
def getCommentCounts(newsurl):
    m = re.search('doc-i(.+).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commentURL.format(newsid))
    jd  = json.loads(comments.text.strip('var data='))
    return jd['result']['count']['total']
    
news  = 'http://news.sina.com.cn/c/gat/2016-09-06/doc-ifxvqctu6364150.shtml'
count = getCommentCounts(news)
print(count)

##############################################
#将抓取内文信息方法整理成一函式
from pip._vendor import requests
from bs4 import BeautifulSoup

def getNewsDetail(newsurl):
    result = {}
    res = requests.get(newsurl)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text,'html.parser')
    result['title'] = soup.select('#artibodyTitle')[0].text.encode('utf-8')
    result['newssource'] = soup.select('.time-source span a')[0].text.encode('utf-8')
    timesource = soup.select('.time-source')[0].contents[0].strip().encode('utf-8')
    result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
    result['article'] = '\n'.join([p.text.encode('utf-8').strip() for p in soup.select('#artibody p')[:-1]])
    result['editor'] = soup.select('.article-editor')[0].text.encode('utf-8').strip('责任编辑：')
    result['comments'] =getCommentCounts(newsurl)
    return result

detail = getNewsDetail('http://news.sina.com.cn/c/gat/2016-09-06/doc-ifxvqctu6364150.shtml')    
for key in detail:
    print (key,detail[key]) 