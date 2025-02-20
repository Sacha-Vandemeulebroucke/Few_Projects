import sqlite3

connection = sqlite3.connect('library.db')

# Interact with the database
cursor = connection.cursor()

#create books table
command1 = """CREATE TABLE IF NOT EXISTS books(book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, released_year INTEGER, quantity INTEGER DEFAULT 1)"""

cursor.execute(command1)

books = [
    ("1984", "George Orwell", 1949),
    ("Animal Farm", "George Orwell", 1945),
    ("To Kill a Mockingbird", "Harper Lee", 1960),
    ("Pride and Prejudice", "Jane Austen", 1813),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925),
    ("War and Peace", "Leo Tolstoy", 1869),
    ("The Hobbit", "J.R.R. Tolkien", 1937),
    ("Crime and Punishment", "Fyodor Dostoevsky", 1866),
    ("Brave New World", "Aldous Huxley", 1932),
    ("Wuthering Heights", "Emily Brontë", 1847),
    ("Jane Eyre", "Charlotte Brontë", 1847),
    ("The Picture of Dorian Gray", "Oscar Wilde", 1890),
    ("Fahrenheit 451", "Ray Bradbury", 1953),
    ("Don Quixote", "Miguel de Cervantes", 1605),
    ("The Alchemist", "Paulo Coelho", 1988),
    ("One Hundred Years of Solitude", "Gabriel García Márquez", 1967),
    ("Dracula", "Bram Stoker", 1897),
    ("The Kite Runner", "Khaled Hosseini", 2003),
    ("The Brothers Karamazov", "Fyodor Dostoevsky", 1880),
    ("The Adventures of Huckleberry Finn", "Mark Twain", 1884),
    ("Les Misérables", "Victor Hugo", 1862),
    ("The Old Man and the Sea", "Ernest Hemingway", 1952),
    ("A Tale of Two Cities", "Charles Dickens", 1859),
    ("The Catcher in the Rye", "J.D. Salinger", 1951),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("Le Petit Prince", "Antoine de Saint-Exupéry", 1943),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling", 1997),
    ("The Odyssey", "Homer", -800),
    ("The Iliad", "Homer", -800),
    ("The Divine Comedy", "Dante Alighieri", 1320),
    ("Hamlet", "William Shakespeare", 1603),
    ("Moby Dick", "Herman Melville", 1851),
    ("Frankenstein", "Mary Shelley", 1818),
    ("Alice's Adventures in Wonderland", "Lewis Carroll", 1865),
    ("The Count of Monte Cristo", "Alexandre Dumas", 1844),
    ("Madame Bovary", "Gustave Flaubert", 1856),
    ("Anna Karenina", "Leo Tolstoy", 1877),
    ("The Stranger", "Albert Camus", 1942),
    ("The Metamorphosis", "Franz Kafka", 1915),
    ("The Trial", "Franz Kafka", 1925),
    ("The Magic Mountain", "Thomas Mann", 1924),
    ("To the Lighthouse", "Virginia Woolf", 1927),
    ("Ulysses", "James Joyce", 1922),
    ("Lolita", "Vladimir Nabokov", 1955),
    ("Catch-22", "Joseph Heller", 1961),
    ("Slaughterhouse-Five", "Kurt Vonnegut", 1969),
    ("Beloved", "Toni Morrison", 1987),
    ("Midnight's Children", "Salman Rushdie", 1981),
    ("The God of Small Things", "Arundhati Roy", 1997),
    ("Life of Pi", "Yann Martel", 2001),
    ("The Book Thief", "Markus Zusak", 2005),
    ("The Road", "Cormac McCarthy", 2006),
    ("Gone Girl", "Gillian Flynn", 2012),
    ("The Hunger Games", "Suzanne Collins", 2008),
    ("The Girl with the Dragon Tattoo", "Stieg Larsson", 2005),
    ("And Then There Were None", "Agatha Christie", 1939),
    ("The Hound of the Baskervilles", "Arthur Conan Doyle", 1902),
    ("The Da Vinci Code", "Dan Brown", 2003),
    ("The Name of the Rose", "Umberto Eco", 1980),
    ("Perfume: The Story of a Murderer", "Patrick Süskind", 1985),
    ("Memoirs of a Geisha", "Arthur Golden", 1997),
    ("The Shadow of the Wind", "Carlos Ruiz Zafón", 2001),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Like Water for Chocolate", "Laura Esquivel", 1989),
    ("Eat, Pray, Love", "Elizabeth Gilbert", 2006),
    ("The Help", "Kathryn Stockett", 2009),
    ("Where the Crawdads Sing", "Delia Owens", 2018),
    ("Little Women", "Louisa May Alcott", 1868),
    ("Little Women", "Louisa May Alcott", 1868),
    ("Little Women", "Louisa May Alcott", 1868),
    ("Anne of Green Gables", "L.M. Montgomery", 1908),
    ("Anne of Green Gables", "L.M. Montgomery", 1908),
    ("Anne of Green Gables", "L.M. Montgomery", 1908),
    ("Anne of Green Gables", "L.M. Montgomery", 1908)
]


cursor.executemany('''INSERT INTO books(title,author,released_year)
VALUES (?,?,?)''',books)

connection.commit()

def duplicate_management():
    """This function manages the duplicate by deleting them and adjust the book's quantity """
    # We search if there is any duplicate in our database
    cursor.execute("select title, count(*) from books group by title having count(*) > 1")
    twin = cursor.fetchall()
    # While there is at least one duplicate
    while len(twin) > 1:
        # We find the title of the duplicate
        cursor.execute("select title, count(*) from books group by title having count(*) > 1")
        twin = cursor.fetchall()
        # We take the title of the first duplicate in the duplicate list
        duplicate = twin[0][0]

        cursor.execute("SELECT * FROM books where title = ?", (duplicate,))
        twin_book_list = cursor.fetchall()
        # While there is at least one duplicates so 2 elements we do this process
        while len(twin_book_list) != 1:
            # We take the id of the first book in the list
            first_id = twin_book_list[0][0]
            # And the last one book id
            last_id = twin_book_list[len(twin_book_list) - 1][0]
            # We delete the book with the last one id
            cursor.execute("DELETE FROM books WHERE book_id = ? ", (last_id,))
            # And we adjust the book with the first id quantity by adding one to his quantity
            cursor.execute("UPDATE books SET quantity = quantity + 1 WHERE  book_id = ? ", (first_id,))
            # Then we find our new list of the duplicated book
            cursor.execute("SELECT * FROM books where title = ?", (duplicate,))
            twin_book_list = cursor.fetchall()
            # Finally we save modification to the database
            connection.commit()

duplicate_management()

cursor.execute("SELECT * FROM books")

results = cursor.fetchall()

print(results)