import psycopg2

conn = psycopg2.connect(user = 'postgres', password = 'test123', host = 'localhost', database = 'postgres')

cursor = conn.cursor()

cursor.execute("UPDATE user_profile SET firstname='sai',lastname='sri',gender='female' WHERE id ='3' ")
conn.commit()
cursor.close()
conn.close()