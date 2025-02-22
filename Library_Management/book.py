import sqlite3

connection = sqlite3.connect('library.db')

cursor = connection.cursor()

def existence_verification(title,author,released_year):
    cursor.execute("SELECT * FROM books where title = ? and author = ? and released_year = ?",(title, author, released_year,))
    finding_one = cursor.fetchall()
    if len(finding_one) == 1:
        #The book is already in the library
        return True
    else:
        return False


def add_to_the_library(title,author,released_year):
    if existence_verification(title,author,released_year):
        # If the book is already in the library we increase its quantity by one
        cursor.execute("UPDATE books SET quantity = quantity + 1 where title = ? and author = ? and released_year = ?", (title, author, released_year,))
        connection.commit()
        print("The book is already referenced, its quantity has been modified")
    else:
        # If not we add it to the library
        cursor.execute("INSERT INTO books(title,author,released_year)VALUES (?,?,?)", (title,author,released_year,))
        connection.commit()
        print("Book added")


def remove_from_library(book_id):
    if search_by_id(book_id):
        # If we find the book, we can remove it
        cursor.execute("DELETE FROM books WHERE book_id = ? ", (book_id,))
        connection.commit()
        print("Book removed from the library")
    else:
        print("The book was not found")


def update(book_id):

    if search_by_id(book_id):
        # If the book is found, we select which part we want to modify
        choice = input("Which of these characteristics you want to modify title/author/year/quantity : ")

        if choice == "title":
            cursor.execute("UPDATE books SET title = ? WHERE  book_id = ? ", (input("New title : "), book_id,))
            connection.commit()
        if choice == "author":
            cursor.execute("UPDATE books SET author = ? WHERE  book_id = ? ", (input("New author : "), book_id,))
            connection.commit()
        if choice == "year":
            cursor.execute("UPDATE books SET released_year = ? WHERE  book_id = ? ", (int(input("New released year : ")), book_id,))
            connection.commit()
        if choice == "quantity":
            cursor.execute("UPDATE books SET quantity = ? WHERE  book_id = ? ", (int(input("New quantity : ")), book_id,))
            connection.commit()
    else:
        print("The book was not found")


def search_by_id(book_id):
    # This query find the book associated with its ID
    cursor.execute("SELECT title, author, released_year FROM books where book_id = ? ", (book_id,))
    search = cursor.fetchone()
    # We print it, if we find it
    if search is not None:
        print(f"The book {book_id} was found,it's {search[0]}, it was written by {search[1]} in {search[2]}")
        # We use the boolean return of this function to reuse it in update function and in the remove_from_library function
        return True
    else:
        print(f"The book {book_id} was not found")
        return False


def print_books():
    # In this query we select all the books
    cursor.execute("SELECT * FROM books")
    # Then we print everything
    for book in cursor.fetchall():
        print(f"{book[0]} : {book[1]} : {book[2]} : {book[3]} : {book[4]}")


def search_by_keyword():
    # We need a key word with this format : %key_word%
    key_word = f"%{input("Entrez votre requête : ")}%"
    # We need to find if a title, an author or a released year correspond
    cursor.execute("SELECT title, author, released_year FROM books where title like ? OR author like ? OR released_year like ?",(key_word, key_word, key_word,))
    # We proint the book find for this query
    for book in cursor.fetchall():
        print(f"{book[0]} : {book[1]} : {book[2]} ")


update(20)