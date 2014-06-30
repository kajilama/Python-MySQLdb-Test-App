__author__ = 'kaji'

import requests
import re
from sqlalchemy import *
import MySQLdb as mdb
from MySQLdb.cursors import DictCursor
import sys

con = mdb.connect('localhost', 'root', 'yolmo', 'test');
cur = con.cursor()

URLString = open("url.txt").read()
print "*" * 100
print URLString
print "*" * 100

URL_list = URLString.split(',')
print URL_list

contents = open("pages.txt", 'w') ### opening pages.txt in write mode
for eachURL in URL_list:
    r = requests.get(eachURL)
    #print r.text
    string = r.text.encode('utf-8')
    contents.write(string+ "\n\n\n"+"*" * 150+"\n\n\n")


content = open("pages.txt").read() ### content (HTML) of all webpages
#print content

### We can now search (and count) for tags in the variable - string: "content"

tags = open("tags.txt").read()
tags_List = tags.split(',')
print "List of Tags: ", tags_List

# def countTag(xxx):
#     qty = len(re.findall(xxx, content))
#     return qty


for eachTag in tags_List:
    print "Count of occurences of %s : " % eachTag, content.count(eachTag)
   # sql = """insert into counter_tbl(tag, count) values (eachTag, content.count(eachTag))"""
    #cur.execute(sql)
    #ver = cur.fetchone()
    #print "Count of occurences of %s : " % eachTag, countTag(eachTag)



#Setting up MySQL-SQLAlchemy connection
# engine = create_engine('mysql://root:yolmo@localhost/test?charset=utf8&use_unicode=0', pool_recycle=3600)
# connection = engine.connect()
#
# for eachTag in tags_List:
#     insert = engine.execute("insert into counter_tbl(tag, count) values (eachTag, content.count(eachTag))")

# def connect_db():
#     """new database connection """
#     connect = MySQLdb.connect(user='root', passwd='yolmo',
#                                 db='kaji_db', host='localhost')
#     return connect








