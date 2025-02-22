import sqlite3

connection = sqlite3.connect('library.db')

# Interact with the database
cursor = connection.cursor()

#create books table
command1 = """CREATE TABLE IF NOT EXISTS books(book_id INTEGER PRIMARY KEY, title TEXT, author TEXT, released_year INTEGER, quantity INTEGER DEFAULT 1)"""

cursor.execute(command1)

command2 = """CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY, name_ TEXT, lastname TEXT, mail TEXT, address TEXT, sex TEXT, age INTEGER)"""

cursor.execute(command2)

command3 = """CREATE TABLE IF NOT EXISTS loan(loan_id INTEGER PRIMARY KEY, book_id INTEGER, user_id INTEGER, 
start_duration DATE, end_duration DATE DEFAULT NULL, FOREIGN KEY(book_id) REFERENCES books(book_id),FOREIGN KEY(user_id) REFERENCES users(user_id) )"""

cursor.execute(command3)

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
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
    ("The Lord of the Rings", "J.R.R. Tolkien", 1954),
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
    ("Anne of Green Gables", "L.M. Montgomery", 1908),
    ("The Lord of the Flies", "William Golding", 1954),
    ("The Handmaid's Tale", "Margaret Atwood", 1985),
    ("The Color Purple", "Alice Walker", 1982),
    ("The Remains of the Day", "Kazuo Ishiguro", 1989),
    ("A Passage to India", "E.M. Forster", 1924),
    ("The Sound and the Fury", "William Faulkner", 1929),
    ("As I Lay Dying", "William Faulkner", 1930),
    ("Absalom, Absalom!", "William Faulkner", 1936),
    ("For Whom the Bell Tolls", "Ernest Hemingway", 1940),
    ("The Sun Also Rises", "Ernest Hemingway", 1926),
    ("A Farewell to Arms", "Ernest Hemingway", 1929),
    ("Of Mice and Men", "John Steinbeck", 1937),
    ("The Grapes of Wrath", "John Steinbeck", 1939),
    ("East of Eden", "John Steinbeck", 1952),
    ("Cannery Row", "John Steinbeck", 1945),
    ("The Pearl", "John Steinbeck", 1947),
    ("Flowers for Algernon", "Daniel Keyes", 1966),
    ("The Martian", "Andy Weir", 2011),
    ("Project Hail Mary", "Andy Weir", 2021),
    ("Ready Player One", "Ernest Cline", 2011),
    ("Dune", "Frank Herbert", 1965),
    ("Dune", "Frank Herbert", 1965),
    ("Dune", "Frank Herbert", 1965),
    ("Dune", "Frank Herbert", 1965),
    ("Foundation", "Isaac Asimov", 1951),
    ("The Left Hand of Darkness", "Ursula K. Le Guin", 1969),
    ("The Dispossessed", "Ursula K. Le Guin", 1974),
    ("Neverwhere", "Neil Gaiman", 1996),
    ("American Gods", "Neil Gaiman", 2001),
    ("Good Omens", "Terry Pratchett & Neil Gaiman", 1990),
    ("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 1979),
    ("The Restaurant at the End of the Universe", "Douglas Adams", 1980),
    ("The Restaurant at the End of the Universe", "Douglas Adams", 1980),
    ("The Restaurant at the End of the Universe", "Douglas Adams", 1980),
    ("The Restaurant at the End of the Universe", "Douglas Adams", 1980),
    ("The Restaurant at the End of the Universe", "Douglas Adams", 1980),
    ("Life, the Universe and Everything", "Douglas Adams", 1982),
    ("So Long, and Thanks for All the Fish", "Douglas Adams", 1984),
    ("Mostly Harmless", "Douglas Adams", 1992),
    ("The Time Machine", "H.G. Wells", 1895),
    ("The War of the Worlds", "H.G. Wells", 1898),
    ("The Invisible Man", "H.G. Wells", 1897),
    ("Journey to the Center of the Earth", "Jules Verne", 1864),
    ("Twenty Thousand Leagues Under the Sea", "Jules Verne", 1870),
    ("Around the World in Eighty Days", "Jules Verne", 1872),
    ("The Three Musketeers", "Alexandre Dumas", 1844),
    ("The Hunchback of Notre-Dame", "Victor Hugo", 1831),
    ("The Scarlet Letter", "Nathaniel Hawthorne", 1850),
    ("Moby-Dick", "Herman Melville", 1851),
    ("Leaves of Grass", "Walt Whitman", 1855),
    ("Uncle Tom's Cabin", "Harriet Beecher Stowe", 1852),
    ("The Call of the Wild", "Jack London", 1903),
    ("White Fang", "Jack London", 1906),
    ("The Age of Innocence", "Edith Wharton", 1920),
    ("A Room with a View", "E.M. Forster", 1908),
    ("Howards End", "E.M. Forster", 1910),
    ("The Secret Garden", "Frances Hodgson Burnett", 1911)
]

users = [
    ('Victor', 'Thompson', 'victor.thompson@test.net', '25 Maple Dr, New York, VT 18442', 'Male', 50),
    ('Elizabeth', 'Thomas', 'elizabeth.thomas@example.com', '79 Maple Dr, Jacksonville, OK 27004', 'Male', 18),
    ('Benjamin', 'Thomas', 'benjamin.thomas@domain.co', '97 Oak Ave, Jacksonville, MD 27096', 'Male', 30),
    ('Mia', 'Walker', 'mia.walker@example.com', '59 Willow Ct, Columbus, MI 48825', 'Other', 19),
    ('Kelly', 'Martinez', 'kelly.martinez@example.com', '86 Birch Pl, Houston, MD 49470', 'Female', 53),
    ('Quinn', 'Davis', 'quinn.davis@domain.co', '38 Maple Dr, San Diego, WI 24334', 'Other', 37),
    ('Alice', 'Clark', 'alice.clark@test.net', '6 Low St, Phoenix, ME 57615', 'Other', 58),
    ('Sophia', 'Moore', 'sophia.moore@mail.org', '90 Low St, Dallas, NJ 15186', 'Male', 48),
    ('Xavier', 'Turner', 'xavier.turner@mail.org', '13 High St, Columbus, AL 81001', 'Other', 28),
    ('Kelly', 'Collins', 'kelly.collins@example.com', '7 River Rd, Austin, MA 22119', 'Male', 51),
    ('Isabella', 'Adams', 'isabella.adams@example.com', '34 Forest Ave, San Jose, NV 66663', 'Male', 54),
    ('Ethan', 'Thompson', 'ethan.thompson@domain.co', '82 Birch Pl, Chicago, SC 13336', 'Other', 26),
    ('Abigail', 'Adams', 'abigail.adams@test.net', '96 Canyon Ct, Houston, WI 39665', 'Male', 48),
    ('Owen', 'Walker', 'owen.walker@test.net', '74 Cedar Rd, Jacksonville, NE 53426', 'Female', 37),
    ('Yara', 'Wright', 'yara.wright@example.com', '53 Willow Ct, New York, VT 69149', 'Other', 45),
    ('Ethan', 'Rodriguez', 'ethan.rodriguez@example.com', '7 Oak Ave, New York, MT 58744', 'Female', 37),
    ('Ethan', 'Smith', 'ethan.smith@domain.co', '31 High St, Houston, PA 67843', 'Female', 64),
    ('Elijah', 'Carter', 'elijah.carter@domain.co', '89 Pine Ln, New York, RI 98970', 'Other', 33),
    ('Victor', 'Adams', 'victor.adams@domain.co', '91 Main St, Phoenix, OH 64906', 'Male', 42),
    ('Peter', 'Collins', 'peter.collins@mail.org', '61 Willow Ct, Houston, NY 68681', 'Other', 29),
    ('Hannah', 'Perez', 'hannah.perez@domain.co', '80 Maple Dr, Houston, MI 16779', 'Other', 64),
    ('William', 'Scott', 'william.scott@test.net', '72 Oak Ave, Dallas, OR 62393', 'Other', 29),
    ('Peter', 'Martin', 'peter.martin@test.net', '4 Cedar Rd, San Diego, TX 84776', 'Other', 45),
    ('Elijah', 'Taylor', 'elijah.taylor@mail.org', '68 High St, San Diego, NJ 19561', 'Other', 42),
    ('Peter', 'Nelson', 'peter.nelson@test.net', '89 Oak Ave, San Jose, MA 19504', 'Male', 48),
    ('Eve', 'Campbell', 'eve.campbell@test.net', '18 Willow Ct, Jacksonville, CT 88608', 'Female', 18),
    ('Zack', 'Young', 'zack.young@mail.org', '15 Summit Rd, Jacksonville, CT 35566', 'Other', 47),
    ('Emily', 'Perez', 'emily.perez@example.com', '6 Low St, Phoenix, LA 82093', 'Female', 47),
    ('Emily', 'Walker', 'emily.walker@example.com', '79 Valley Dr, San Diego, PA 42179', 'Male', 27),
    ('Charlie', 'Nelson', 'charlie.nelson@mail.org', '69 Low St, Chicago, MD 49331', 'Male', 23),
    ('Mason', 'Green', 'mason.green@mail.org', '23 High St, San Jose, GA 11628', 'Male', 42),
    ('Mason', 'Wright', 'mason.wright@test.net', '86 Forest Ave, Phoenix, ID 96987', 'Female', 63),
    ('Elijah', 'Green', 'elijah.green@mail.org', '96 Summit Rd, Houston, RI 91469', 'Female', 54),
    ('Yara', 'Harris', 'yara.harris@test.net', '92 Low St, Austin, AK 54915', 'Other', 51),
    ('Yara', 'Gonzalez', 'yara.gonzalez@test.net', '74 Forest Ave, Phoenix, AZ 56661', 'Other', 31),
    ('Mia', 'Sanchez', 'mia.sanchez@domain.co', '51 Birch Pl, Fort Worth, WA 92471', 'Female', 43),
    ('Peter', 'Anderson', 'peter.anderson@example.com', '46 River Rd, Dallas, AR 56412', 'Other', 42),
    ('Owen', 'Moore', 'owen.moore@test.net', '95 Forest Ave, San Jose, ND 13229', 'Male', 63),
    ('Elijah', 'Smith', 'elijah.smith@test.net', '76 Forest Ave, Austin, NV 50957', 'Other', 38),
    ('Sophia', 'Harris', 'sophia.harris@test.net', '14 Birch Pl, Chicago, AK 16773', 'Female', 44),
    ('Uma', 'Edwards', 'uma.edwards@domain.co', '33 Oak Ave, San Diego, HI 66718', 'Male', 26),
    ('Quinn', 'Evans', 'quinn.evans@mail.org', '6 Pine Ln, Fort Worth, TX 63291', 'Female', 44),
    ('Scarlett', 'Garcia', 'scarlett.garcia@example.com', '62 Cedar Rd, Chicago, NJ 93908', 'Male', 25),
    ('Jack', 'Brown', 'jack.brown@mail.org', '57 Meadow Ln, Houston, IL 66028', 'Other', 41),
    ('Ava', 'Young', 'ava.young@domain.co', '40 Low St, Austin, AR 69598', 'Other', 36),
    ('James', 'Lopez', 'james.lopez@example.com', '46 Low St, San Diego, NJ 36643', 'Male', 24),
    ('Frank', 'King', 'frank.king@example.com', '91 Main St, Philadelphia, ME 40117', 'Female', 44),
    ('Michael', 'Wright', 'michael.wright@mail.org', '56 Birch Pl, Fort Worth, NE 97163', 'Female', 49),
    ('Ethan', 'Sanchez', 'ethan.sanchez@example.com', '100 Birch Pl, New York, MN 51493', 'Female', 36),
    ('James', 'Hernandez', 'james.hernandez@domain.co', '13 Meadow Ln, Indianapolis, ND 99865', 'Female', 63)
]

cursor.executemany('''INSERT INTO books(title,author,released_year)
VALUES (?,?,?)''',books)

cursor.executemany('''INSERT INTO users(name_,lastname,mail, address, sex, age)
VALUES (?,?,?,?,?,?)''',users)

# We save all the new inputs
connection.commit()

# This function delete the duplicate and adjust the book quantity
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

