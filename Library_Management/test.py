# import sqlite3
#
# connection = sqlite3.connect('library.db')
#
# cursor = connection.cursor()
#
# cursor.execute("SELECT * FROM books")
# every_books = cursor.fetchall()
# for book in every_books:
#     print(f"{book[0]} : {book[1]} : {book[2]} : {book[3]} : {book[4]}")




import random

def generate_random_data(size):
    names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack", "Kelly", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Riley", "Sophia", "Thomas", "Uma", "Victor", "Wendy", "Xavier", "Yara", "Zack", "Ava", "Ethan", "Isabella", "James", "Charlotte", "Daniel", "Amelia", "Michael", "Emily", "William", "Abigail", "Alexander", "Madison", "Benjamin", "Elizabeth", "Elijah", "Sofia", "Lucas", "Scarlett", "Mason", "Victoria", "Henry", "Avery", "Owen", "Nora", "Jackson", "Eleanor", "Caleb", "Hazel"]
    lastnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Lewis", "Robinson", "Walker", "Hall", "Allen", "Young", "King", "Wright", "Scott", "Green", "Baker", "Adams", "Nelson", "Carter", "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins"]
    domains = ["example.com", "test.net", "mail.org", "domain.co"]
    streets = ["Main St", "Oak Ave", "Pine Ln", "Maple Dr", "Cedar Rd", "Willow Ct", "Birch Pl", "High St", "Low St", "River Rd", "Forest Ave", "Meadow Ln", "Valley Dr", "Summit Rd", "Canyon Ct"]
    cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Jacksonville", "Fort Worth", "Columbus", "Indianapolis"]
    states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
    sexes = ["Male", "Female"]

    data = []
    for _ in range(size):
        name = random.choice(names)
        lastname = random.choice(lastnames)
        mail = f"{name.lower()}.{lastname.lower()}@{random.choice(domains)}"
        street = random.choice(streets)
        city = random.choice(cities)
        state = random.choice(states)
        zip_code = random.randint(10000, 99999)
        address = f"{random.randint(1, 100)} {street}, {city}, {state} {zip_code}"
        sex = random.choice(sexes)
        age = random.randint(18, 65)
        data.append((name, lastname, mail, address, sex, age))
    return data

random_data = generate_random_data(50)
print(random_data)
