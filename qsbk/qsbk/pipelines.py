# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class QsbkPipeline(object):
    def __init__(self):
        self.fp=open("content.json",'w',encoding="utf-8")

    def open_spider(self,spider):
        print("程序开始执行")

    def process_item(self, item, spider):
        item_json=json.dumps(dict(item),ensure_ascii=False)
        self.fp.write(item_json+'\n')
        return item
    def close_spider(self,spider):
        self.fp.close()
        print("程序执行结束")
