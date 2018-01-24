import mysql.connector as md

conn = md.connect(user = 'root', password = 'password', host = 'localhost', database = 'testdb')
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS USER")
cursor.execute("CREATE TABLE USER(userid INT PRIMARY KEY ,first_name VARCHAR(30) UNIQUE,last_name VARCHAR(30),email VARCHAR(40) UNIQUE)")

cursor.execute("DROP TABLE IF EXISTS APPLICATION")
cursor.execute("CREATE TABLE APPLICATION(userid INT,applicationid INT PRIMARY KEY ,age INT ,address1 VARCHAR(40),address2 VARCHAR(40),salary VARCHAR(30),company_name VARCHAR(30), FOREIGN KEY(userid) REFERENCES USER (userid))")


cursor.close()
conn.close()
