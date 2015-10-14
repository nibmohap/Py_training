import MySQLdb
db=MySQLdb.connect("localhost","root","root")

cursor=db.cursor()

cursor.execute("SELECT VERSION()")

data=cursor.fetchone()

print "database version :%s" % data

db.close()
