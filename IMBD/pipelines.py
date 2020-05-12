# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector

class ImbdPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.con = mysql.connector.connect(
        host='localhost', user='root', passwd='Shivjeet1',
                database='my_database'
            )
        self.curs = self.con.cursor()

    def create_table(self):
        self.curs.execute("""Drop table if exists reviews""")
        self.curs.execute(""" create table reviews(title text,rating
                              float(4,2),storyline text,genre text)""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, items):
        self.curs.execute(""" insert into reviews values (%s,%s,%s)""", (items['title'][0],
                                                                             items['author'][0], items['tag'][0]))
         # we used %s as all data is in string format.
        self.con.commit()
