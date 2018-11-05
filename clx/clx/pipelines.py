# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.contrib.exporter import CsvItemExporter


class ClxPipeline(object):
    '''
    would likew to output to any format or any place, write here by pipline, 
    '''
    # def __init__(self):
    #     self.file = open("D:\repositories\pyqt5\crawl_result.csv", 'w+b')

    #  def spider_opened(self, spider):
    #     # self.file = open('output.csv', 'w+b')
    #     self.exporter = CsvItemExporter(self.file)
    #     self.exporter.start_exporting()

    # def spider_closed(self, spider):
    #     self.exporter.finish_exporting()
    #     self.file.close()

    # def process_item(self, item, spider):
    #     self.exporter.export_item(item)
    #     return item
    def process_item(self, item, spider):
        return item
