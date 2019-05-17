_author_='CQC'
#-*-coding:utf-8 -*-
import urllib
import re
#3.6没有urllib2
class BDTB:
    #初始化，传入基地址，是否只看楼主的参数
    def _init_(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.baseLZ = '?see_lz='+str(seeLZ)
        #传入页码，获取该贴子的代码
        def getPage(self,pageNum):
            try:
                url = self.baseURL+self.seeLZ+'&pn='+str(pageNum)
                request = urllib.Request.Request(url)
                response = urllib.Request.urlopen(request)
                print (response.read().decode('utf-8'))
                return response
            except urllib.error.HTTPError as e:
                print(e.code)  
                print(e.read().decode("utf-8")) 
                return None
                baseURL = 'https://tieba.baidu.com/p/5219126313'
            bdtb = BDTB(baseURL,1)
            bdtb.getPage(1)
