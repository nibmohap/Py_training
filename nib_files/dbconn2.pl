import MySQLdb
db=MySQLdb.connect("localhost","root","root","test")

cursor=db.cursor()

#cursor.execute("drop table if exists employee")
sql="""CREATE TABLE EMPLOYEE(FIRST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),AGE NUMBER,SEX CHAR(20),
        INCOME NUMBER)"""
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close
