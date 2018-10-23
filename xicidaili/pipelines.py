# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import requests

class XicidailiPipeline(object):
    def __init__(self):
        self.f=open('Goodproxy.csv','w' ,newline="",encoding='utf-8')
        self.write=csv.writer(self.f)
        self.write.writerow(['addr','ip','life','port','speed','timeout','update','ip_port'])
    def process_item(self, item, spider):
        ip=item['ip']+":"+str(item['port'])
        if self.Verip(ip)==True:
            self.write.writerow((item['addr'],item['ip'],item['life'],\
                                     item['port'],item['speed'],item['timeout'],item['update'],ip))
        return item

    def Verip(self,ip):
        flag=False
        try:
            proxies = {'http': ip}
            r = requests.get('http://www.ip.cn/', proxies=proxies, timeout=3)
            if r.status_code == 200:
                flag=True
        except:
            flag=False
        return flag

    def close_spider(self,spider):
        self.f.close()
class XicidailiPipeline2(object):
    def __init__(self):
        self.f=open('proxy.csv','w' ,newline="",encoding='utf-8')
        self.write=csv.writer(self.f)
        self.write.writerow(['addr','ip','life','port','speed','timeout','update','ip_port'])
    def process_item(self, item, spider):
        ip=item['ip']+":"+str(item['port'])
        # if self.Verip(ip)==True:
        self.write.writerow((item['addr'],item['ip'],item['life'],\
                            item['port'],item['speed'],item['timeout'],item['update'],ip))
        return item
    def close_spider(self,spider):
        self.f.close()
