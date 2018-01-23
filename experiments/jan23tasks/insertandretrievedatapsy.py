import psycopg2

conn = psycopg2.connect(user = 'postgres', password = 'test123', host = 'localhost', database = 'postgres')

cursor = conn.cursor()

cursor.execute("INSERT INTO user_profile VALUES ('1','gowtham','raghava','male'),('2','sunny','sarath','male'),(3,'raja','vinod','male')")
conn.commit()
cursor.close()
conn.close()