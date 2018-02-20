import mysql.connector as md
conn = md.connect(user ="root", password = "password",database = "testdb")
cursor = conn.cursor()

dict1 = {}

sql = "SELECT * FROM user1"
cursor.execute(sql)
result = cursor.fetchall()
print result
