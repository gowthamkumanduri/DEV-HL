import mysql.connector as md

conn = md.connect(user = 'root', password = 'password', host = 'localhost', database = 'testdb')

cursor = conn.cursor()

cursor.execute('INSERT INTO user_profile VALUES(1,"gowtham","raghava","k.gowthamraghava@gmail.com","male","1111","2222")')
cursor.execute('INSERT INTO user_profile VALUES(2,"bobby","bonthu","b.bobby@gmail.com","male","1111","2222")')
cursor.execute('INSERT INTO user_profile VALUES(3,"sri","sai","s.sri@gmail.com","female","1111","2222")')
conn.commit()

cursor.execute("SELECT * FROM user_profile")
print (cursor.fetchall())


cursor.close()
conn.close()