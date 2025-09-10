```markdown
# 🧪 Selenium Login Automation

A demo project showcasing **automated login workflows** using **Selenium** and **pytest**, including UI validation and screenshot capture.

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
git clone https://github.com/Thinh59/selenium-login-automation.git
cd selenium-login-automation
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

You can change the credentials in `test_login.py`:

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

- Demo project for **automation testing practice**  
- Perfect for a **QC Intern portfolio** 💼
```
