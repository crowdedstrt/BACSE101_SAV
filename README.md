# BACSE101_SAV
# University Portal Management System

A Python-based **University Portal Management System** that allows administrators and students to interact with a centralized MySQL database.  
Built using **Python**, **MySQL**, **NumPy**, and **Pandas**, this project demonstrates core programming concepts such as regex validation, sorting, searching, and data analysis — all backed by a persistent SQL database.

---

## Features

### Admin Module
- Secure admin login
- Add new student records
- View all student details
- Sort student records by ID, Name, or Department
- Search students by ID
- Password authentication (stored in MySQL)

### Student Module
- Student login using unique Student ID and password
- Password validation 
- Create password on first login
- View personal details, marks, and average performance

### Data Analysis Module
- Uses **Pandas** and **NumPy** to:
  - Create DataFrames from student data
  - Calculate average marks
  - Sort students by performance
  - Display tabular and statistical insights

---

## Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend | Python 3 |
| Database | MySQL |
| Libraries | `mysql-connector-python`, `numpy`, `pandas`, `re` |
| Concepts | Functions, Loops, Conditionals, Bubble Sort, Binary Search, SQL Integration |

---

## Setup Instructions

### 1️ Install Dependencies
Make sure you have Python 3 and MySQL installed.

Then run:
- bash
- pip install mysql-connector-python pandas numpy

### 2️ Create MySQL Database
Open MySQL shell or Workbench and run:

- sql
- (Copy code)
- CREATE DATABASE university_portal;
The program will automatically create the required tables on first run.

### 3️ Update Connection Details (if needed)
By default, the connection is:

- python
- (Copy code)
- host="localhost"
- user="root"
- password="root"
- database="university_portal"
Edit these in the code if your MySQL credentials differ.

### 4️ Run the Program
- bash
- (Copy code)
- python portal.py

## Database Schema
Table: admins
Field	Type	Description
username	VARCHAR(50)	Admin username
password	VARCHAR(100)	Admin password

Table: students
Field	Type	Description
id	VARCHAR(20)	Student ID
name	VARCHAR(100)	Student Name
dept	VARCHAR(20)	Department
marks	VARCHAR(100)	Comma-separated marks (e.g., 85,90,78)
password	VARCHAR(100)	Student password

## Key Concepts Demonstrated
Data Types (Numeric, String, Boolean)

Password Validation

Bubble Sort and Binary Search

Lists, Dictionaries, Tuples

Functions (Parameters, Return Values)

Loops (for, while)

Conditional Statements (if, elif, else)

Exception Handling

Persistent Data Storage via MySQL

Data Analysis with Pandas and NumPy
