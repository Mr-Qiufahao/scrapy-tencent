# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import urllib2

class TiebalPipeline(object):


    def process_item(self, item, spider):
        filename = item['image_list'][-10:]
        image= urllib2.urlopen(item['image_list']).read()
        with open(filename, "wb") as f:
            f.write(image)
            print "已经成功下载" + filename
        return item
