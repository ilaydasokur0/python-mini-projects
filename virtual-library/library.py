# This is a simple library management system that allows users to create accounts,
# borrow books, donate books, and return books. The system keeps track of borrowed
# books and their due dates. Users can only borrow up to 3 books at a time.

import datetime
import json
import os

DATA_FILE = "library_data.json"


class User:  # User class to represent library users
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.borrowed_books = []


class Book:  # Book class to represent books in the library
    def __init__(self, title, author):
        self.title = title
        self.author = author


# ---------- Input helpers ----------

def ask_text(prompt: str) -> str:
    """Free text input: strip only (no lowercasing)."""
    return input(prompt).strip()


def ask_choice(prompt: str, valid_options: list[str]) -> str:
    """Choice input: strip + lower + validate."""
    valid = [v.lower() for v in valid_options]
    while True:
        ans = input(prompt).strip().lower()
        if ans in valid:
            return ans
        print(f"Invalid input. Please enter one of: {', '.join(valid)}.")


# ---------- Persistence ----------

def save_data(users, books):
    data = {"users": [], "books": []}

    for u in users:
        user_dict = {
            "username": u.username,
            "password": u.password,
            "borrowed_books": []
        }
        for rec in u.borrowed_books:
            rec_copy = rec.copy()
            rec_copy["Borrowed Date"] = rec["Borrowed Date"].isoformat()
            rec_copy["Return Date"] = rec["Return Date"].isoformat()
            user_dict["borrowed_books"].append(rec_copy)
        data["users"].append(user_dict)

    for b in books:
        data["books"].append({"title": b.title, "author": b.author})

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def load_data():
    if not os.path.exists(DATA_FILE):
        return None, None

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    loaded_books = [Book(b["title"], b["author"]) for b in data.get("books", [])]
    loaded_users = []

    for u_data in data.get("users", []):
        u = User(u_data["username"], u_data["password"])
        for rec in u_data.get("borrowed_books", []):
            rec["Borrowed Date"] = datetime.datetime.fromisoformat(rec["Borrowed Date"])
            rec["Return Date"] = datetime.datetime.fromisoformat(rec["Return Date"])
            u.borrowed_books.append(rec)
        loaded_users.append(u)

    return loaded_users, loaded_books


# ---------- Auth ----------

def log_in(users):
    username = ask_text("Enter your username: ")
    password = ask_text("Enter your password: ")

    for u in users:
        if u.username == username and u.password == password:
            print(f"Welcome {u.username}!")
            return u

    print("Invalid username or password. You can try again or create a new account.")
    return None


def create_account(users):
    while True:
        username = ask_text("Choose a username: ")
        if any(u.username == username for u in users):
            print("This username is already taken. Please choose another one.")
        else:
            break

    password = ask_text("Choose a password: ")
    new_user = User(username, password)
    users.append(new_user)
    print("Account created successfully!")
    return new_user


# ---------- Library actions ----------

def borrow_book(current_user, books):
    if len(current_user.borrowed_books) >= 3:
        print("Sorry, you can only borrow up to 3 books at a time.")
        return

    book_choice = ask_text("Enter the title of the book you want to borrow: ").strip().lower()

    for bk in books:
        if bk.title.strip().lower() == book_choice:
            borrow_date = datetime.datetime.now()
            return_date = borrow_date + datetime.timedelta(days=30)

            current_user.borrowed_books.append({
                "Name": bk.title,
                "Author": bk.author,
                "Borrowed Date": borrow_date,
                "Return Date": return_date
            })

            books.remove(bk)

            print(
                f"You have borrowed '{bk.title}' by {bk.author}. "
                f"You must return it by {return_date.strftime('%Y-%m-%d')}. Enjoy reading!"
            )
            return

    print("Sorry, that book is not available in our library.")


def donate_book(books):
    donating_title = ask_text("Enter the title of the book you want to donate: ").strip().title()
    donating_author = ask_text("Enter the author of the book you want to donate: ").strip().title()

    for bk in books:
        if bk.title.strip().lower() == donating_title.strip().lower() and bk.author.strip().lower() == donating_author.strip().lower():
            print("This book is already in our library. Thank you for your willingness to donate!")
            return

    new_book = Book(donating_title, donating_author)
    books.append(new_book)
    print(f"Thank you for donating '{new_book.title}' by {new_book.author} to our library!")


def return_book(current_user, books):
    returning_title = ask_text("Enter the title of the book you want to return: ").strip().lower()

    for rec in current_user.borrowed_books:
        if rec["Name"].strip().lower() == returning_title:
            now = datetime.datetime.now()
            books.append(Book(rec["Name"], rec["Author"]))

            if now > rec["Return Date"]:
                print(f"You returned '{rec['Name']}' late. Please return books on time next time.")
            else:
                print(f"Thank you for returning '{rec['Name']}' on time!")

            current_user.borrowed_books.remove(rec)
            return

    print("You haven't borrowed this book.")


# ---------- Menu ----------

def menu(current_user, books):
    while True:
        print("\nMenu:")
        print("1. List of available books")
        print("2. Borrow a book")
        print("3. Donate a book")
        print("4. Show my borrowed books")
        print("5. Return a book")
        print("6. Exit")

        choice = ask_choice("Enter your choice (1-6): ", ["1", "2", "3", "4", "5", "6"])

        if choice == "1":
            for bk in books:
                print(f"'{bk.title.title()}' by {bk.author.title()}")

        elif choice == "2":
            borrow_book(current_user, books)

        elif choice == "3":
            donate_book(books)

        elif choice == "4":
            if not current_user.borrowed_books:
                print("You haven't borrowed any books yet.")
            else:
                for rec in current_user.borrowed_books:
                    due = rec["Return Date"].strftime("%Y-%m-%d")
                    print(f"'{rec['Name'].title()}' by {rec['Author'].title()} (due: {due})")

        elif choice == "5":
            return_book(current_user, books)

        elif choice == "6":
            print("Goodbye!")
            return


# ---------- Seed ----------

def get_seed_books():
    return [
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


# ---------- Main ----------

users, books = load_data()

if users is None:
    users = [User("ilaydasokur0", "12345")]

if books is None:
    books = [Book(title, author) for title, author in get_seed_books()]

while True:
    choice = ask_choice("Do you have an account? (yes/no): ", ["yes", "no"])
    if choice == "yes":
        current_user = log_in(users)
        if current_user is not None:
            break
    else:  # no
        current_user = create_account(users)
        break

menu(current_user, books)
save_data(users, books)