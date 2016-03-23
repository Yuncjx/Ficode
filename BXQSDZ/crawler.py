# _*_ coding:utf-8 _*_
import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
headers = {'User-Agent': user_agent}
try:
    req = urllib2.Request(url,data=None,headers=headers)
    response = urllib2.urlopen(req,data=None)
    content =  response.read().decode('utf-8')
    pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?content">' +
                         '(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats">.*?number">(.*?)</i>.*?number">(.*?)</i>',re.S )
    items = re.findall(pattern,content)
    print items
    for item in items:
        haveImg = re.search("img",item[3])
        if not haveImg:
            print item[0],item[1],item[4]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason
Sheila Patek