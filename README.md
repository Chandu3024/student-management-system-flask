# 📘 Student Management System (Flask)  
### With Selenium-Based Automated Testing (PyTest)

A complete **web-based Student Management System** built using **Flask**, combined with a fully automated **Selenium + PyTest testing framework** that validates all core functionalities such as Login, Add Student, Search, Edit, and Delete.

This project follows the **V-Model (Verification & Validation)** approach and demonstrates full life-cycle testing, reporting, and UI automation.

---

# 📑 Table of Contents

1. [Project Overview](#project-overview)
2. [Key Features](#key-features)
3. [Architecture](#architecture)
4. [Tech Stack](#tech-stack)
5. [Project Structure](#project-structure)
6. [Installation Guide](#installation-guide)
7. [Running the Application](#running-the-application)
8. [Running Automated Tests](#running-automated-tests)
9. [HTML Report & Screenshots](#html-report--screenshots)
10. [V-Model Explanation](#v-model-explanation)
11. [Test Cases](#test-cases)
12. [Future Enhancements](#future-enhancements)
13. [Contributors](#contributors)

---

# 📘 Project Overview

The **Student Management System (SMS)** is a Flask-based web application supporting:

- Admin Login  
- Student Creation  
- Student Search  
- Student Editing  
- Student Deletion  

The system integrates a complete **Selenium + PyTest automated testing framework** validating every user interaction through UI automation.

This project demonstrates:

✔ Flask web development  
✔ Functional CRUD operations  
✔ Automated testing with Selenium  
✔ Page Object Model (POM)  
✔ HTML reporting with embedded screenshots  
✔ V-Model-based testing workflow  

---

# 🚀 Key Features

### 🎓 Student Features
- Add new students  
- Search existing students  
- Edit student details  
- Delete student records  
- Field-level validation  

### 🔐 Authentication
- Admin login  
- Session-protected dashboard  

### 🤖 Automation Framework
- Selenium WebDriver  
- PyTest  
- Fixtures  
- Page Object Model (POM)  
- Auto screenshot capture  
- Auto HTML report generation  

### 📊 Reporting
- Detailed HTML report  
- Includes screenshots for failed test cases  

---

# 🏛️ Architecture

```
Frontend → HTML / CSS / Bootstrap  
Backend  → Flask (Python)  
Database → SQLite  
Testing  → Selenium WebDriver + PyTest  
Design   → Page Object Model  
Reports  → pytest-html  
```

---

# 🧰 Tech Stack

### Backend
- Python 3.9+
- Flask
- SQLite

### UI
- HTML  
- Bootstrap  
- Jinja templates  

### Testing
- Selenium WebDriver  
- PyTest  
- Webdriver-Manager  
- pytest-html  

---

# 📂 Project Structure

```
student-management-system-flask/
│
├── app.py
├── models.py
├── init_db.py
│
├── templates/
│   ├── login.html
│   ├── dashboard.html
│   ├── edit_student.html
│   └── add_student.html
│
├── static/
│   └── styles.css
│
├── tests/
│   ├── conftest.py
│   ├── test_student_crud.py
│   └── pages/
│       ├── login_page.py
│       └── dashboard_page.py
│
├── tests_reports/
│   ├── report.html
│   └── screenshots/
│
├── run_tests.bat
├── requirements.txt
└── README.md
```

---

# 🛠️ Installation Guide

## 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/student-management-system-flask.git
cd student-management-system-flask
```

## 2️⃣ Create Virtual Environment

### Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

## 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 4️⃣ Initialize the Database
```bash
python init_db.py
```

---

# ▶️ Running the Application

Start the Flask app:
```bash
python app.py
```

Visit:
👉 http://127.0.0.1:5000

---

# 🤖 Running Automated Tests

## ✔ Option A — Using the Batch Script (Windows)
```powershell
.\run_tests.bat
```

## ✔ Option B — Manually Running Tests
```bash
pytest -q --disable-warnings --html=tests_reports/report.html --self-contained-html
```

---

# 🖼️ HTML Report & Screenshots

After running tests, the report is generated at:

```
tests_reports/report.html
```

Screenshots of failed test cases are stored at:

```
tests_reports/screenshots/
```

The system automatically attaches screenshots to the HTML report (via conftest.py).

---

# 📐 V-Model Explanation

This project follows the **V-Model** (Verification & Validation):

```
Requirements      ↔ Acceptance Tests  
High-Level Design ↔ System Tests  
Low-Level Design  ↔ Integration Tests  
Implementation    ↔ Unit & UI Tests  
```

Our Selenium functional tests validate the **right side of the V-Model**.

---

# 🧪 Test Cases

| Test Case ID | Name | Description |
|--------------|------|-------------|
| TC01 | Login Success | Valid admin login → Dashboard loads |
| TC02 | Login Failure | Wrong credentials → Error message |
| TC03 | Add Student | Add student → Verify in table |
| TC04 | Search Student | Search → Filter matches |
| TC05 | Edit Student | Change details → Save |
| TC06 | Delete Student | Accept delete → Removed |
| TC06a | Cancel Delete | Cancel popup → No change |

---

# 🔮 Future Enhancements

- Role-based access control  
- Student profile photo upload  
- Export to CSV / Excel  
- REST API for mobile integration  
- Docker support  
- CI/CD automation with GitHub Actions  
- Cross-browser testing (Grid / BrowserStack)  

---

# 👨‍💻 Contributors

- **Chandu S**  
- (Add others if needed)

---

# 🎉 You're all set!

This README is fully professional and ready for GitHub, submission, and portfolio usage.
