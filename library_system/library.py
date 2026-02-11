#This is a simple library management system that allows users to create accounts, borrow books, donate books, and return books. The system keeps track of borrowed books and their due dates. Users can only borrow up to 3 books at a time, and they are encouraged to return books on time to avoid late returns.
import datetime
import json
import os
class User: #User class to represent library users
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.borrowed_books = []
class Book: #Book class to represent books in the library
    def __init__(self,title,author):
        self.title = title
        self.author = author

def save_data(users, books): #Function to save user and book data to a JSON file
    data = {
        "users": [],
        "books": []
    }
    for u in users:
        user_dict = {
            "username": u.username,
            "password": u.password,
            "borrowed_books": []
        }
        for b in u.borrowed_books:
            b_copy = b.copy()
            b_copy["Borrowed Date"] = b["Borrowed Date"].isoformat()
            b_copy["Return Date"] = b["Return Date"].isoformat()
            user_dict["borrowed_books"].append(b_copy)
        data["users"].append(user_dict)
    for b in books:
        data["books"].append({"title": b.title, "author": b.author})

    with open("library_data.json", "w") as f:
        json.dump(data, f, indent=4) 

def load_data(): #Function to load user and book data from a JSON file
    if not os.path.exists("library_data.json"):
        return None, None
    with open("library_data.json", "r") as f:
        data = json.load(f)
    loaded_books = [Book(b["title"], b["author"]) for b in data["books"]]
    loaded_users = []
    for u_data in data["users"]:
        u = User(u_data["username"], u_data["password"])
        for b_dict in u_data["borrowed_books"]:
            b_dict["Borrowed Date"] = datetime.datetime.fromisoformat(b_dict["Borrowed Date"])
            b_dict["Return Date"] = datetime.datetime.fromisoformat(b_dict["Return Date"])
            u.borrowed_books.append(b_dict)
        loaded_users.append(u)
    return loaded_users, loaded_books

def LogIn(users): #Function to handle user login
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for user in users:
        if user.username == username and user.password == password:
            print(f'Welcome {user.username}!')
            return user
    else:
        print("Invalid username or password. You can try again or create a new account.")
        return None
    
def CreateAccount(users): #Function to handle account creation
    username = input("Choose a username: ")
    password = input("Choose a password: ")
    new_user = User(username,password)
    users.append(new_user)
    print("Account created successfully!")
    return new_user

def BorrowBook(user, books): #Function to handle borrowing books
    if len(user.borrowed_books) >= 3: # Users can only borrow up to 3 books at a time
        print("Sorry, you can only borrow up to 3 books at a time.")
        return
    book_choice = input("Enter the title of the book you want to borrow: ").strip().lower()
    for book in books:
        if book.title.strip().lower() == book_choice:
            borrow_date = datetime.datetime.now()
            return_date = borrow_date + datetime.timedelta(days=30) # Users have 30 days to return the book
            user.borrowed_books.append({
                "Name": book.title,
                "Author": book.author,
                "Borrowed Date": borrow_date,
                "Return Date": return_date
            })
            books.remove(book)
            print(
                f"You have borrowed '{book.title}' by {book.author}. "
                f"You must return it by {return_date.strftime('%Y-%m-%d')}. Enjoy reading!"
            )
            return
    else:
        print("Sorry, that book is not available in our library.")

def DonateBook(books): #Function to handle donating books
    donating_book_title=input("Enter the title of the book you want to donate: ").strip().title()
    donating_book_author=input("Enter the author of the book you want to donate: ").strip().title()
    for book in books:
        if book.title.strip().lower()==donating_book_title.strip().lower() and book.author.strip().lower()==donating_book_author.strip().lower():
            print("This book is already in our library. Thank you for your willingness to donate!")
            return
    else:
        new_book=Book(donating_book_title.strip().title(),donating_book_author.strip().title())
        books.append(new_book)
        print(f"Thank you for donating '{new_book.title}' by {new_book.author} to our library!")

def ReturnBook(user, books): #Function to handle returning books
    returning_title = input("Enter the title of the book you want to return: ").strip().lower()
    for record in user.borrowed_books:
        if record["Name"].strip().lower() == returning_title:
            now = datetime.datetime.now()
            books.append(Book(record["Name"], record["Author"]))
            if now > record["Return Date"]: # Check if the book is returned late
                print(f"You returned '{record['Name']}' late. Please return books on time next time.")
            else:
                print(f"Thank you for returning '{record['Name']}' on time!")
            user.borrowed_books.remove(record)
            return
    print("You haven't borrowed this book.")

def Menu(user, books): #Function to display the main menu and handle user choices
    while True:
        print("\nMenu:")
        print("1. List of available books")
        print("2. Borrow a book")
        print("3. Donate a book")
        print("4. Show my borrowed books")
        print("5. Return a book")
        print("6. Exit")
        choice = input("Enter your choice (1/2/3/4/5/6): ").strip()
        if choice == "1":
            for book in books:
                print(f"'{book.title.title()}' by {book.author.title()}")
        elif choice == "2":
            BorrowBook(user, books)
        elif choice == "3":
            DonateBook(books)
        elif choice == "4":
            if not user.borrowed_books:
                print("You haven't borrowed any books yet.")
            else:
                for record in user.borrowed_books:
                    due = record["Return Date"].strftime("%Y-%m-%d")
                    print(f"'{record['Name'].title()}' by {record['Author'].title()} (due: {due})")
        elif choice == "5":
            ReturnBook(user, books)
        elif choice == "6":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.")

# Sample book data to populate the library
book_data = [
    ("A Tale of Two Cities", "Charles Dickens"),
    ("1984", "George Orwell"),
    ("To Kill a Mockingbird", "Harper Lee"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Pride and Prejudice", "Jane Austen"),
    ("Moby Dick", "Herman Melville"),
    ("The Catcher in the Rye", "J.D. Salinger"),
    ("Brave New World", "Aldous Huxley"),
    ("The Hobbit", "J.R.R. Tolkien"),
    ("Fahrenheit 451", "Ray Bradbury"),
    ("The Alchemist", "Paulo Coelho"),
    ("Animal Farm", "George Orwell"),
    ("The Little Prince", "Antoine de Saint-Exupéry"),
    ("Harry Potter and the Sorcerer's Stone", "J.K. Rowling"),
    ("Dune", "Frank Herbert"),
    ("Crime and Punishment", "Fyodor Dostoevsky"),
    ("The Brothers Karamazov", "Fyodor Dostoevsky"),
    ("Les Misérables", "Victor Hugo"),
    ("Madonna in a Fur Coat", "Sabahattin Ali"),
    ("The Time Regulation Institute", "Ahmet Hamdi Tanpinar"),
    ("The Stranger", "Albert Camus"),
    ("The Metamorphosis", "Franz Kafka"),
    ("The Lord of the Rings", "J.R.R. Tolkien"),
    ("Anna Karenina", "Leo Tolstoy"),
    ("Ulysses", "James Joyce"),
    ("The Old Man and the Sea", "Ernest Hemingway"),
    ("One Hundred Years of Solitude", "Gabriel García Márquez"),
    ("Don Quixote", "Miguel de Cervantes"),
    ("War and Peace", "Leo Tolstoy"),
    ("The Divine Comedy", "Dante Alighieri"),
    ("The Odyssey", "Homer"),
]

users, books = load_data()

if users is None:
    users = [User("ilaydasokur0", "12345")] #Default user account for testing purposes
if books is None:
    books = [Book(title, author) for title, author in book_data] # Create Book objects from the sample data and add them to the library if no data was loaded

# Main program loop to handle user login and menu navigation
user = None
while user is None:
    choice = input("Hi! Do you have an account? (yes/no): ")
    if choice.strip().lower()=="yes":
        user=LogIn(users)
        if user:
            print("You can now access the library menu.")
            break
    elif choice.strip().lower()=="no":
        user=CreateAccount(users)
        print("You can now access the library menu.")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
Menu(user,books)
save_data(users, books)
