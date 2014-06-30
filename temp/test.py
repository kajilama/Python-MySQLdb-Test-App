__author__ = 'kaji'

from urllib import urlopen
import MySQLdb
import MySQLdb.cursors
import sys

class MyList(object):

    def __init__(self, filename):
        self.filename = filename


    def createList(self):
        try:
            f = open(self.filename).read()
            list = f.split(',')
            print " List for %s: %s" % (self.filename, list)
            return list
        except:
            #print e
            print "File '%s' not found! Exiting !!!" % self.filename
            sys.exit(1)


    def fetchURL(self):
        text = " \n "
        try:
            for eachURL in URL_list:
                html = urlopen(eachURL).read()
                text = text + html
            #print text
            return text
        except Exception, e:
            print e
            print "Error Processing the URL List"
            sys.exit(1)

    def createTable(self):
        try:
            cursor.execute ("DROP TABLE IF EXISTS counter_tbl")
            cursor.execute(""" CREATE TABLE counter_tbl(
                id INT(5) NOT NULL AUTO_INCREMENT,
                tag VARCHAR(30) NOT NULL,
                count INT(5) NOT NULL,
                PRIMARY KEY(id)
                )
            """)
        except Exception, e:
            print e


    def ins(self, tag1, counter):
        try:
           # Execute the SQL command
           cursor.execute("insert into counter_tbl(tag, count) values (%s,%s)", (tag1, counter))
           # Commit your changes in the database
           db.commit()
           print "Data inserted into the Database successfully for '%s'" % tag1
        except Exception, e:
           # Rollback in case there is any error
            db.rollback()
            print e
            print "Error: Data cannot be inserted for '%s'" % tag1
            sys.exit(1)


# Open database connection
#db = MySQLdb.connect("localhost","root","yolmo","test" )

try:
    db = MySQLdb.connect(host = "localhost",
                             user = "root",
                             passwd = "yolmo",
                             db = 'test')
except MySQLdb.Error, e:
    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

# prepare a cursor object using cursor() method
cursor = db.cursor(MySQLdb.cursors.DictCursor)

#DROP DATABASE IF EXISTS : AND CREATE NEW DB : DID NOT WORK #######
# try:
#     cursor.execute('DROP DATABASE IF EXISTS `test`')
#     #print "Affected: %d" % cursor.rowcount
# except MySQLdb.Error, e:
#     print "Error occurred: %s " % e.args[0]
#     print e
#
#
# cursor.execute("CREATE DATABASE 'test'")
# cursor.execute("USE DATABASE 'test")


print #blank line
#creating new instances of MyList Class
list1 = MyList("urls.txt")
list2 = MyList("tags.txt")

# creating lists using text files
URL_list = list1.createList()
tags_List = list2.createList()

#Fecthing and storing Web pages from the URLs into the string - "text"
text = list1.fetchURL()
print "\n\n\n Web Contents: %s\n\n\n" % text

# Drop existing and Create new Table
list1.createTable()

###### Delete all records and reset the AUTO_INCREMENT COUNTER ######
#cursor.execute("truncate table counter_tbl")

print "Inserting Data in the Database Now..."
for eachTag in tags_List:
    list1.ins(eachTag, text.count(eachTag))


print "\nList of tags and their count of occurences:"
cursor.execute("select tag, count from counter_tbl")

# # Enable this to Fetch only one row of data at a time
# counter = cursor.fetchone()
# print counter['tag'], counter['count']

# Fetch more than one rows of data at a time
counter = cursor.fetchall()
desc = cursor.description
print "Data queried from the Database:"
print "*" *31
print "%-17s  ==> %8s" % (desc[0][0], desc[1][0])
print "*" *31
for eachRow in counter:
    print "%-17s  ==> %8s" % (eachRow['tag'], eachRow['count'])

db.commit()
db.close()

