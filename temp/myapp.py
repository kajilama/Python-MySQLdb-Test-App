__author__ = 'kaji'

from urllib import urlopen
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","yolmo","test" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Funciton to create a list from a text file
def createList(filename):
    f = open(filename).read()
    list = f.split(',')
    print " List for %s: %s" % (filename, list)
    return list

# Fetch web page contents using the URLs from text file
def fetchURL(url):
    html = urlopen(url).read()
    return html

print # blank line

#create URL list from text file - "URLS.TXT"
URL_list = createList("urls.txt")

#create tags list from text file - "TAGS.TXT"
tags_List = createList("tags.txt")

text = " \n "
for eachURL in URL_list:
    text = text + fetchURL(eachURL)
#print text

print #blank line

#Find out & display the count of tags.
for eachTag in tags_List:
    tag1 = eachTag
    count = text.count(eachTag)
    print "Count of occurences of '%s' : " % tag1, count

# function to insert tags-count data into the DB table
def ins(tag1, counter):
    cursor.execute("insert into counter_tbl(tag, count) values (%s,%s)", (tag1, counter))

###### Delete all records and reset the AUTO_INCREMENT COUNTER ######
#cursor.execute("truncate table counter_tbl")

# Inserting data into table
for eachTag in tags_List:
    ins(eachTag, text.count(eachTag))
print "\nData successfully inserted into teh Database."
db.commit()
db.close()

