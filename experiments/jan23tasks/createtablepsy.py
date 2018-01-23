import psycopg2

conn = psycopg2.connect(user = 'postgres', password= 'test123', host= 'localhost', database= 'postgres')

cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS user_profile')
cursor.execute('CREATE TABLE user_profile(Id serial PRIMARY KEY,firstname VARCHAR(20),lastname VARCHAR(20),gender VARCHAR(10))')
conn.commit()
cursor.close()
conn.close()
