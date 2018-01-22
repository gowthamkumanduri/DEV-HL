import mysql.connector as md

conn = md.connect(host = 'localhost' , user = 'root' , password = 'password' , database = 'testdb' )

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS user_profile")
cursor.execute("CREATE TABLE user_profile(Id INT PRIMARY KEY, firstname VARCHAR(25), lastname VARCHAR(25), email VARCHAR(30), gender VARCHAR(8), likes INT, comments INT)")


cursor.close()
conn.close()