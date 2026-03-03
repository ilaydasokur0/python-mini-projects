# 🐍 Python Mini Projects

Hello! I am a Mathematical Engineering student working on building a solid foundation in Python and software development.

This repository contains small-scale projects developed during my learning journey.  
The projects are intentionally simple — my goal is to deeply understand fundamentals before moving to more complex systems.

I prioritize writing clean, structured, and maintainable code.

---

## 🎯 Learning Focus

- Strengthening Python fundamentals  
- Object-Oriented Programming (OOP)  
- Modular and maintainable project structures  
- File systems and databases  
- Basic UI development  
- Version control with Git & GitHub  
- Designing software inspired by real-world use cases  

More projects will be added and existing ones will continue to evolve.

---

# 📌 Projects

## 1) Library Management System (CLI)

A command-line based library management system developed using Python.

### Features
- User registration and authentication  
- Borrowing up to three books  
- Returning borrowed books  
- Donating new books  
- Viewing available and borrowed books  
- Persistent local storage using JSON  

All user and book data is stored locally and automatically loaded when the program starts.

### What I Learned
- Object-Oriented Programming (OOP) with Python classes  
- Designing data models (User, Book)  
- File handling and JSON-based persistence  
- Date and time operations using `datetime`  
- Input validation  
- Program modularization  
- Code readability and maintainability  
- Basic Git workflow  

### ▶️ How to Run

```bash
cd library_system
python library.py
```

## 2) Job Tracker (Streamlit + SQLite)

A simple job application tracker built with Python, SQLite, and Streamlit.

This project introduces relational database design and a basic web interface.

### Features
- Add job applications  
- Track application status  
- Store metadata (link, notes, date)  
- Automatic skill extraction from job descriptions  
- Display most frequently requested skills  
- Interactive Streamlit interface  

### What I Learned
- Working with SQLite and relational database design  
- Table relationships and foreign keys  
- Writing SQL queries  
- Layered project architecture  
- Basic text processing with regular expressions  
- Building a minimal web UI with Streamlit  
- Connecting backend logic to a frontend interface  

### ▶️ How to Run

```bash
cd job_tracker
pip install -r requirements.txt
streamlit run streamlit_app.py
