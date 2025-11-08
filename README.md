# 🎓 University Portal System

A **Python + MySQL** based console application that automates academic record management for universities and colleges.
It provides **secure login systems**, **database-driven CRUD operations**, and **analytical tools** for both administrators and students — all from the command line.

---

## 📘 Overview

The **University Portal System** simplifies how institutions manage student, teacher, and subject data.
Administrators can add, edit, and analyze academic records, while students can log in to view their marks, check subject statistics, and update personal information securely.

It integrates MySQL for reliable data persistence, uses hashing for password protection, and leverages data analysis libraries to provide real-time insights.

---

## 🧩 Features

### 👨‍💼 Admin Module

* Secure admin login with password hashing
* Add, view, delete, and sort **students**, **teachers**, and **subjects**
* Add and update **marks** for students
* View **subject statistics** (highest, average, lowest)
* Change admin password securely

### 👩‍🎓 Student Module

* Secure student login with hashed password
* Update personal information
* View assigned subjects and teachers
* Check marks with comparative statistics
* Change password from student account

### ⚙️ System Features

* MySQL-based backend for persistent storage
* Input validation (email format, numeric entries, etc.)
* Sorting and binary search algorithms for student lookup
* Automatic demo data generation for quick testing
* Tabulated console output using `tabulate`

---

## 🛠️ Tech Stack & Libraries

| Library             | Purpose                                          |
| ------------------- | ------------------------------------------------ |
| **mysql.connector** | Connects Python to MySQL database                |
| **hashlib**         | Secures passwords with SHA-256 hashing           |
| **getpass**         | Handles hidden password input                    |
| **re**              | Validates email formats                          |
| **NumPy**           | Performs statistical calculations                |
| **Pandas**          | Displays and manipulates tabular data            |
| **tabulate**        | Formats data neatly in the console               |
| **sys**             | Exits program and handles system-level functions |

---

## 📂 Project Structure

```
University_Portal_System/
│
├── VBOTTOM.py                # Main Python script
├── University_Portal_Report.pdf
├── README.md                 # Project description (you’re here)
└── requirements.txt          # dependencies
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have:

* Python 3.8 or above
* MySQL Server installed and running
* MySQL user credentials (default: root/root)

### Installation

```bash
# Clone this repository
git clone https://github.com/<your-username>/University-Portal-System.git

# Navigate to project folder
cd University-Portal-System

# Install required Python packages
pip install mysql-connector-python pandas numpy tabulate
```

### Database Setup

The system **automatically creates** the `university_portal` database and required tables on the first run.
Default admin credentials:

```
Username: admin
Password: admin
```

### Run the Application

```bash
python VBOTTOM.py
```

### Demo Data

When prompted, choose **‘y’** to generate demo entries for:

* Students
* Teachers
* Subjects
* Marks

---

## 📊 Sample Functionalities

* Add a new student → Assign password → View details in tabular form
* Enter marks for subjects and compute analytics
* Binary search a student by roll number
* View class-wide subject statistics with highest/average/lowest marks

---

## 🔐 Security Notes

All user passwords are stored using **SHA-256 encryption** via the `hashlib` module.
Passwords are never stored or displayed in plain text.

---

## 📈 Future Enhancements

* Web or GUI interface using Flask or Tkinter
* Role-based access control (multiple admins, department heads, etc.)
* Graphical data visualization for marks
* Export functionality (CSV/Excel reports)

---
