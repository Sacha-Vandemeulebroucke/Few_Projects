import sqlite3
import datetime

connection = sqlite3.connect('library.db')

cursor = connection.cursor()

def book_id_available(book_id):
    cursor.execute("SELECT * FROM books where book_id = ?",(book_id,))
    finding_one = cursor.fetchall()

    if len(finding_one) == 1:
        # We verify if it is any input loan with this Book ID with no end duration and with a quantity of 0
        # -> So all the book are loaned, if a book has 10 copy and all of them are loaned, the quantity will be 0
        cursor.execute("SELECT end_duration, quantity FROM loan as l inner join main.books as b on l.book_id = b.book_id where l.book_id = ? AND l.end_duration IS NULL AND quantity = 0",(book_id,))
        finding = cursor.fetchall()

        if len(finding) == 1:
            # If the book remaining quantity is equal to 0 and there are no end duration in the loan table for this book id, meaning that the book is already borrowed by someone else
            print("The book is already loaned")
            return False
        else:
            print("The book is available")
            return True
    else:
        print("The book doesn't exist")
        return False


def user_id_available(user_id, loan_process):
    cursor.execute("SELECT * FROM users where user_id = ?", (user_id,))
    find = cursor.fetchall()
    if len(find) == 1:
        # If one user with the user ID found
        cursor.execute("SELECT loan_id, book_id, start_duration FROM loan where user_id = ? and end_duration IS NULL", (user_id,))
        number_of_active_loan = cursor.fetchall()
        if loan_process == "end_loan":
            # For the end_loan() function we retrieve all the current borrowed books
            return number_of_active_loan
        if len(number_of_active_loan) >= 3 and loan_process == "start_loan":
            # The user can borrow 3 books maximum at the same time
            print("The user can borrow 3 books at the same time maximum. Please give back a book in order to borrow one")
            return False
        else:
            return True
    else:
        print("User doesn't exist")
        return False


def loan():
    user_id = input("Enter your user ID ")
    if user_id_available(user_id, "start_loan"):
        book_id = input("Enter the book ID ")
        if book_id_available(book_id):
            # If the user and the book are available

            # We adjust the quantity by decreasing the number of the book's copy available
            cursor.execute("UPDATE books SET quantity = quantity - 1 WHERE  book_id = ? ", (book_id,))
            connection.commit()

            # Then we add the new input in our loan database
            start_duration = datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute("INSERT INTO loan(book_id,user_id,start_duration)VALUES (?,?,?)",(book_id, user_id, start_duration,))
            connection.commit()

            print("You borrow the book")


def end_loan():

    user_id = input("Enter your user ID ")
    # We retrieve all the books borrowed by the user
    loans = user_id_available(user_id,"end_loan")


    if len(loans) >= 1:
        cursor.execute("select loan_id, title, start_duration from loan as l inner join main.books b on b.book_id = l.book_id where l.user_id = ? and end_duration IS NULL",(user_id,))
        the_loans = cursor.fetchall()

        # In the loan_number we retrieve all the loan id of the books that we have borrowed
        loan_number = []
        finish_one = None

        print("The book you are currently borrowing \n")

        for ln in the_loans:
            print(f"Loan ID : {ln[0]} Title : {ln[1]} You borrow it since : {ln[2]} \n")
            loan_number.append(ln[0])
        print("Reminder : You can borrow a book for 3 weeks maximum ⚠️\n")

        try :
            finish_one = int(input("Enter the loan_id of the book that you want to give back, type an other number to quit "))
        except ValueError:
            print("You must enter an integer")

        if finish_one in loan_number:
            # If the loan ID that we select : finish_one. Is in the loan_number

            # We retrieve the book ID from the loan table
            cursor.execute("select b.book_id from loan as l inner join main.books b on b.book_id = l.book_id where l.loan_id = ?",(finish_one,))

            book_adjust_quantity = cursor.fetchall()

            # The book go back to the library so it's quantity increase by one
            cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE  book_id = ? ", (book_adjust_quantity[0][0],))

            # We add an end duration that close the loan
            end_duration = datetime.datetime.now().strftime("%Y-%m-%d")
            cursor.execute("UPDATE loan SET end_duration = ? where loan_id  = ? ",(end_duration, finish_one,))
            connection.commit()

        elif finish_one not in loan_number and finish_one is int:
            print("You don't give back any book ")
    else:
        print("You don't have any loan")


def print_user_borrowed_books():

    user_id =None

    try:
        user_id = int(input("Enter your user ID "))
    except ValueError:
        print("It must be a integer")

    cursor.execute("select loan_id, title, start_duration, end_duration from loan as l inner join main.books b on b.book_id = l.book_id where l.user_id = ?",(user_id,))
    users_books = cursor.fetchall()

    if len(users_books) >= 1:
        # If the user borrows books then we print them
        for loa in users_books:
            if loa[3] is None:
                print(f"Loan ID : {loa[0]} Title : {loa[1]} You borrow it since : {loa[2]}\n")
            else:
                print(f"Loan ID : {loa[0]} Title : {loa[1]} You borrow it between : {loa[2]} and {loa[3]}\n")
    else:
        print(f"No books borrowed registered for the user ID : {user_id}")


def print_all_the_borrowed_books():
    # We retrieve name,lastname, title, start_duration, end_duration from three tables, then we print everything
    cursor.execute("select loan_id,name_ as name,lastname, title, start_duration, end_duration from loan as l inner join main.books b on b.book_id = l.book_id inner join main.users as u on u.user_id = l.user_id order by lastname")
    for borrowed in cursor.fetchall():

        if borrowed[5] is None:
            print(f"{borrowed[1]} {borrowed[2]} borrows {borrowed[3]} since {borrowed[4]}. Loan ID : {borrowed[0]}\n")
        else:
            print(f"{borrowed[1]} {borrowed[2]} borrows {borrowed[3]} between {borrowed[4]} and {borrowed[5]}. Loan ID : {borrowed[0]}\n")





