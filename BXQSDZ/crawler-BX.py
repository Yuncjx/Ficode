# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import thread
import time

class QSBKcrawler:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64)'
        self.headers = {'User-Agent':self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/hot/page/'+str(pageIndex)
            request = urllib2.Request(url,headers=self.headers)
            respone = urllib2.urlopen(request)
            pageCode = respone.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败,错误原因",e.reason
                return None

    def getPageItems(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败```"
            return None
        pattern = re.compile('<div.*?author clearfix">.*?<a.*?<img.*?>.*?</a>.*?<a.*?>.*?<h2>(.*?)</h2>.*?content">' +
                         '(.*?)<!--(.*?)-->.*?</div>(.*?)<div class="stats">.*?number">(.*?)</i>.*?number">(.*?)</i>',re.S)
        items = re.findall(pattern,pageCode)
        pageStories = []
        for item in items:
            havImg = re.search("img",item[3])
            if not havImg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR,"\n",item[1])
                pageStories.append([item[0].strip(),text.strip(),item[4].strip()])
        return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.stories)< 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex +=1

    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input =="Q":
                self.enable = False
                return
            print u"第%d页\t发布人:%s\t赞:%s\n%s" %(page,story[0],story[2],story[1])

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBKcrawler()
spider.start()








