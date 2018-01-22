import mysql.connector as md

conn = md.connect(user = 'root', password= 'password', host= 'localhost', database= 'testdb')
cursor = conn.cursor()

cursor.execute("UPDATE user_profile SET firstname='raghu',lastname='chitturi' WHERE Id = 2")
conn.commit()

cursor.close()
conn.close()
