import MySQLdb
db=MySQLdb.connect("localhost","root","root","test")

cursor=db.cursor()

#cursor.execute("drop table if exists employee")
sql="""INSERT INTO EMPLOYEE VALUES('NIBEDITA',
        'MOHAPATRA',25,'F',20000)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close
