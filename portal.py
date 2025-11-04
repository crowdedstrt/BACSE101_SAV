import mysql.connector
import re
import numpy as np
import pandas as pd

# ---------------------- MySQL Connection Setup ----------------------
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS university_portal")
    cursor.execute("USE university_portal")

    # create tables if not exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            username VARCHAR(50) PRIMARY KEY,
            password VARCHAR(100)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id VARCHAR(20) PRIMARY KEY,
            name VARCHAR(100),
            dept VARCHAR(20),
            marks VARCHAR(100),
            password VARCHAR(100)
        )
    """)
    conn.commit()
    return conn

# ---------------------- Helper Functions ----------------------
def validate_password(password):
    print("\nPassword must have at least 6 characters, contain one letter, one digit, and one special character (@, $, !, %, *, #, ?, &).")
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%#?&])[A-Za-z\d@$!#%*?&]{6,}$'
    if bool(re.match(pattern, password)):
        return True
    else:
        print("Invalid password format. Please follow the above rules.\n")
        return False


def calculate_average(marks_list):
    return sum(marks_list) / len(marks_list)

def parse_marks(marks_str):
    return list(map(int, marks_str.split(',')))

def bubble_sort(data, key):
    n = len(data)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

def binary_search(data, key, target):
    low, high = 0, len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid][key] == target:
            return data[mid]
        elif data[mid][key] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None

# ---------------------- Admin Functions ----------------------
def admin_login(cursor):
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
    admin = cursor.fetchone()

    if admin:
        print("\nLogin Successful! Welcome Admin.")
        return {"username": admin[0], "password": admin[1]}
    else:
        print("Invalid credentials!")
        return None


   

def add_student(cursor, conn):
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dept = input("Enter department: ")
    marks = input("Enter 3 marks separated by commas (e.g. 85,90,78): ")
    cursor.execute("INSERT INTO students (id, name, dept, marks, password) VALUES (%s, %s, %s, %s, %s)", 
                   (student_id, name, dept, marks, ""))
    conn.commit()
    print(f"Student {name} added successfully!")

def view_students(cursor):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print("\n--- Student Records ---")
    for s in students:
        marks = parse_marks(s[3])
        print(f"ID: {s[0]} | Name: {s[1]} | Dept: {s[2]} | Avg Marks: {calculate_average(marks):.2f}")

def sort_students(cursor):
    key = input("Sort by (id/name/dept): ")
    if key not in ("id","name","dept"):
        print("Invalid sort key!")
        return
    cursor.execute(f"SELECT * FROM students ORDER BY {key}")
    students = cursor.fetchall()
    print("\n--- Sorted Students ---")
    for s in students:
        print(s)

def search_student(cursor):
    target_id = input("Enter student ID to search: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (target_id,))
    student = cursor.fetchone()
    if student:
        print(f"Found: {student}")
    else:
        print("Student not found!")

# ---------------------- Student Functions ----------------------
def student_login(cursor, conn):
    student_id = input("Enter your Student ID: ")
    cursor.execute("SELECT * FROM students WHERE id=%s", (student_id,))
    student = cursor.fetchone()

    if not student:
        print("No student found with this ID.")
        return None

    if student[4] == "" or student[4] is None:
        print("\nNo password set. Please create one.")
        while True:
            new_pass = input("Create a new password: ")
            if validate_password(new_pass):
                confirm_pass = input("Confirm password: ")
                if new_pass == confirm_pass:
                    cursor.execute("UPDATE students SET password=%s WHERE id=%s", (new_pass, student_id))
                    conn.commit()
                    print("Password set successfully!\n")
                    break
                else:
                    print("Passwords do not match. Try again.")
            else:
                print("Invalid password. Try again.")
    else:
        entered_pass = input("Enter your password: ")
        if entered_pass != student[4]:
            print("Incorrect password!")
            return None
        else:
            print(f"\nLogin successful! Welcome, {student[1]}.\n")

    return {"id": student[0], "name": student[1], "dept": student[2], "marks": student[3]}

def student_portal(cursor, conn):
    student = student_login(cursor, conn)
    if not student:
        return
    marks = parse_marks(student['marks'])
    print(f"Department: {student['dept']}")
    print(f"Your Marks: {marks}")
    print(f"Your Average: {calculate_average(marks):.2f}")

# ---------------------- Data Handling with Pandas ----------------------
def data_analysis(cursor):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    df = pd.DataFrame(students, columns=['id', 'name', 'dept', 'marks', 'password'])
    df['marks'] = df['marks'].apply(lambda x: list(map(int, x.split(','))))
    df['average'] = df['marks'].apply(np.mean)
    print("\n--- DataFrame ---")
    print(df[['id', 'name', 'dept', 'average']])
    print("\n--- Sorted by Average Marks ---")
    print(df.sort_values(by='average', ascending=False))

# ---------------------- Main Program ----------------------
def main():
    conn = connect_db()
    cursor = conn.cursor()

    # Ensure at least one admin exists
    cursor.execute("SELECT COUNT(*) FROM admins")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO admins (username, password) VALUES (%s, %s)", ("admin", "ElStupido"))
        conn.commit()

    while True:
        print("\n===== UNIVERSITY PORTAL =====")
        print("1. Admin Login")
        print("2. Student Access")
        print("3. Data Analysis")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            admin = admin_login(cursor)
            if admin:
                while True:
                    print("\n--- Admin Menu ---")
                    print("1. Add Student")
                    print("2. View Students")
                    print("3. Sort Students")
                    print("4. Search Student")
                    
                    print("5. Logout")
                    admin_choice = input("Enter your choice: ")

                    if admin_choice == '1':
                        add_student(cursor, conn)
                    elif admin_choice == '2':
                        view_students(cursor)
                    elif admin_choice == '3':
                        sort_students(cursor)
                    elif admin_choice == '4':
                        search_student(cursor)
               
                    elif admin_choice == '5':
                        break
                    else:
                        print("Invalid option! Try again.")

        elif choice == '2':
            student_portal(cursor, conn)

        elif choice == '3':
            data_analysis(cursor)

        elif choice == '4':
            print("Exiting portal... Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()