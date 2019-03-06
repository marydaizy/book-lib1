# import os,csv

# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

# engine = create_engine('DATABASE_URL')
# db = scoped_session(sessionmaker(bind=engine))


# f = open("books.csv")
# books = csv.reader(f)

# engine.execute("DROP TABLE books CACSAD")
# engine.execute("DROP TABLE users CACSAD")
# engine.execute("DROP TABLE reviews CACSAD")
# engine.execute(
#   """create table books
#     (
#         id serial PRIMARY KEY,
#         isbn VARCAR UNIQUE NOT NULL,
#         title VARCHAR NOT NULL,
#         author VARCHAR NOT NULL,
#         year VARCHAR NOT NULL,
#     )"""
# )

# engine.execute((
#   """create table users
#     (
#         id serial PRIMARY KEY,
#         username VARCHAR UNIQUE NOT  NULL,
#         password VARCHAR NOT NULL,
#         email VARCHAR NOT NULL,
#     )"""
# )

# # engine.execute(
# #   """CREATE TABLE reviews
# #     (
# #         id serial PRIMARY KEY,
# #         user_id INTEGER REFERENCES users,
# #         book_id INTEGER REFERENCES books,
# #         review VARCHAR NOT NULL,
# #         rating INTEGER NOT NULL CHECK(rating>=1 and rating<=5)
# #     )"""
# # )
# for isbn, title, author, year in books:
#     db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",{"isbn"})
#     print(f'Added {title} to database')
#     db.commit() 

# # def main():
# #     f = open("books.csv", "r")  # needs to be opened during reading csv
# #     reader = csv.reader(f)
# #     next(reader)
# #     for isbn, title, author, year in reader:
# #         db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
# #                {"isbn": isbn, "title": title, "author": author, "year": year})
# #         db.commit()
# #         print(f"Added book with ISBN: {isbn} Title: {title}  Author: {author}  Year: {year}")


# # if __name__ == '__main__':
# #     main()