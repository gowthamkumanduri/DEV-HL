import mysql.connector as md

conn = md.connect(user = 'root', password = 'password', host = 'localhost', database = 'testdb')
cursor = conn.cursor()

cursor.execute("DELETE FROM user_profile WHERE firstname = 'sri' ")

conn.commit()

cursor.close()
conn.close()