# 🐍 Python Mini Projects

Hello! I am a Mathematical Engineering student building a strong foundation in Python and software development.

This repository contains small projects developed during my learning journey.  
My goal is to deeply understand programming fundamentals while practicing **clean, structured, and efficient code**.

The projects focus on writing **maintainable code, designing modular systems, and solving real-world inspired problems**.

---

# 🚀 Projects

## 1) Virtual Library System (CLI)

A command-line based virtual library system developed using Python.

Users can create a personal reading library, track reading progress, rate books, and write reviews.

The project is structured using a simple layered architecture separating **data models, business logic, and storage**.

### Features
- User creation and simple authentication
- Adding books to a global catalog
- Creating a personal reading library
- Reading status tracking (want / reading / finished / abandoned)
- Start and finish reading with automatic date tracking
- Book rating system (1–5)
- Writing book reviews with optional spoiler flag
- Filtering personal library by reading status
- Persistent local storage using JSON
- Automatic data loading when the program starts

---

### What I Learned
- Object-Oriented Programming (OOP) with Python classes
- Designing data models using `dataclass`
- Using `Enum` for controlled status values
- Structuring a multi-module Python project
- Separating business logic with a service layer
- JSON-based data persistence
- Working with `datetime`
- CLI input handling and validation
- Writing **clean and maintainable code**
- Basic Git workflow

---

### How to Run

``` bash
cd virtual-library
python main.py 
```

## 2) Job Tracker (Streamlit + SQLite)

A simple job application tracker built with Python, SQLite, and Streamlit.

This project focuses on working with **relational databases** and building a small interactive web interface.

### Features
- Add job applications
- Track application status
- Store job metadata (link, notes, date)
- Automatic skill extraction from job descriptions
- Display most frequently requested skills
- Interactive Streamlit interface

---

### What I Learned
- Working with `SQLite` and `relational database design`
- Writing `SQL queries`
- Structuring backend logic for data-driven applications
- Basic text processing with regular expressions
- Building a minimal web UI with `Streamlit`
- Connecting backend logic with a frontend interface

---

### ▶️ How to Run

```bash
cd job_tracker
pip install -r requirements.txt
streamlit run streamlit_app.py
```

---

## 📌 Notes

This repository is part of my ongoing learning process.  
As I continue improving my skills, existing projects may evolve with new features, better architecture, and additional technologies.  
New projects will also be added over time as I explore different areas of software development.