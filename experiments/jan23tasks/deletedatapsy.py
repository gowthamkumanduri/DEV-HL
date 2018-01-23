import psycopg2

conn = psycopg2.connect(user = 'postgres', password = 'test123', host = 'localhost', database = 'postgres')

cursor = conn.cursor()

cursor.execute("DELETE FROM user_profile WHERE id= '3' ")
conn.commit()
cursor.close()
conn.close()