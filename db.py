import os, psycopg2, csv

DATABASE_URL = "postgresql://postgres:daisy@localhost:5432/book_lib1"
conn = psycopg2.connect(host="localhost",database="book_lib1", user="postgres", password="daisy")

csvfile = open("books.csv") 
reader = csv.reader(csvfile,delimiter=',')
print("Creating books table!")

cur = conn.cursor()



cur.execute("CREATE TABLE IF NOT EXISTS books ( id SERIAL PRIMARY KEY, \
								   isbn VARCHAR NOT NULL, \
								   title VARCHAR NOT NULL, \
								   author VARCHAR NOT NULL, \
								   year VARCHAR NOT NULL );")

cur.execute("CREATE TABLE IF NOT EXISTS users ( id SERIAL PRIMARY KEY, \
                                    username VARCHAR UNIQUE NOT  NULL, \
                                    password VARCHAR NOT NULL,  \
                                    email VARCHAR NOT NULL);")

cur.execute("CREATE TABLE IF NOT EXISTS reviews ( id SERIAL PRIMARY KEY, \
                                    user_id INTEGER REFERENCES users, \
                                    book_id INTEGER REFERENCES books, \
                                    review VARCHAR NOT NULL, \
                                    rating INTEGER NOT NULL CHECK(rating>=1 and rating<=5));")
print("Created!")
2
print("Adding values to table.")


for isbn, title, author, year in reader:
	cur.execute("INSERT INTO books (isbn, title, author, year) VALUES (%s, %s, %s, %s)",(isbn,title,author,year))

conn.commit()
print("Insert Completed!")