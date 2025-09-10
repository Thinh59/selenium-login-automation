# 🧪 Selenium Login Automation Demo

This project demonstrates **automated testing** of a login workflow using **Selenium** and **pytest**.

It uses a demo login page: [The Internet – Login Page](https://the-internet.herokuapp.com/login) 🌐

---

## ✨ Features

- Test **successful login** with valid credentials
- Test **failed login** with invalid credentials
- Validate UI elements and capture **screenshots** for each test
- Fully automated and ready to run

---

## 🛠️ Prerequisites

- Python 3.10+   
- Chrome browser installed  
- VS Code or any IDE (optional) 

---

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/<your-username>/selenium-login-test.git
cd selenium-login-test
```

2. (Optional) Create a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Tests

Run all tests with **pytest**:

```bash
pytest -v
```

- 📸 Screenshots will be saved in the `screenshots/` folder  
- 📊 Test output will show **PASSED / FAILED** for each case

---

## 🔑 Customize Username / Password

You can easily change the credentials in `test_login.py`:

```python
USERNAME = "tomsmith"              # Change to your username
PASSWORD = "SuperSecretPassword!"  # Change to your password
```

---

## 📷 Demo Screenshots

- **Success:** `screenshots/success.png`  
- **Failure:** `screenshots/failure.png`  

---

## ⚠️ Notes

- This is a demo project for **automation testing practice**  
- Ready to use as a **QC Intern portfolio project** 💼
# selenium-login-automation
A demo project showcasing automated login and logout workflows with Selenium and Python, including UI validation and screenshot capture.
