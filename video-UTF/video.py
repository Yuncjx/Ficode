#!usr/bin/python
# -*- coding:utf-8 -*-
import re
import urllib
import urllib2
import os

def Schedule(a,b,c):
    '''
    a:已经下载的模块
    b:数据快的大小
    c:远程文件的大小
    '''
    per = 100.0*a*b/c
    if per >100 :
        per = 100
    print '%.1f%%' % per

class CrawlerVideo:

    def __init__(self):
        self.menue = []
        self.https = []
        self.name = ''


    #选择何种视频，并返回链接
    def WhatMp4(self):
        English_China = raw_input( "请选择字幕语言 (E/C): ").upper()
        if English_China == 'E':
            self.name = self.name +'E-'
            Gao_Biao = raw_input("请选择高清还是标清（G/B): ").upper()
            if Gao_Biao == 'G':
                self.name = self.name + 'G'
                f = open('resources/G-E.metalink','r')
                http = self.GetHttp(f)
                f.close()
                return http
            else:
                self.name = self.name + 'B'
                f = open('resources/B-E.metalink','r')
                http = self.GetHttp(f)
                f.close()
                return http
        else:
            self.name = self.name + 'C-'
            Gao_Biao = raw_input("请选择高清还是标清（G/B): ").upper()
            if Gao_Biao == 'G':
                self.name = self.name + 'G'
                f = open('resources/G-C.metalink','r')
                http = self.GetHttp(f)
                f.close()
                return http
            else:
                self.name = self.name + 'B'
                f = open('resources/B-C.metalink','r')
                http = self.GetHttp(f)
                f.close()
                return http

    def GetHttp(self,f):
        author = raw_input("请输入作者：")
        zheng = '<file name="' + author +'.*?-(.*?)mp4">.*?<resources>.*?<ur.*?type="http">(.*?)</url>.*?</resources>'
        pagecode =  f.read().decode('utf-8')
        pattern = re.compile(zheng,re.S)
        items = re.findall(pattern,pagecode)
        for item in items:
            self.menue.append(item[0])
            self.https.append(item[1])
        if len(self.menue) ==0:
            print "没有该作者"
            https = self.WhatMp4()
        elif len(self.menue) > 1:
            print self.menue
            change = int(raw_input("请选择下载序列：")) - 1
            self.name = self.name + self.menue[change]       #下载文件名为self.name
            https = self.https[change]           #下载文件地址为https
        else:
            print self.menue
            self.name = self.name + self.menue[0]
            https = self.https[0]
            deter = raw_input("点击任意确认下载: ")
        return https

    #下载视频
    def Download(self,http):
        local = 'mp4/'+ self.name + 'mp4'
        urllib.urlretrieve(http,local,Schedule)

    def start(self):
        https = self.WhatMp4()
        self.Download(https)
        exit = raw_input("下载完成：")

spider = CrawlerVideo()
spider.start()










