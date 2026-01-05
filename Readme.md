# 🔐 Secure File Locker (Desktop Application)

Secure File Locker is a modern desktop-based application developed using Python that allows users to securely lock and unlock files and folders using password-based encryption.  
The application features a premium glassmorphism-inspired UI and supports single files, multiple files, and complete folders.

This project is designed for educational purposes, college submission, and personal file security.

---

## ✨ Key Features

- 🔑 Login authentication system (App-level security)
- 🔒 Lock and unlock individual files
- 📂 Lock and unlock multiple files at once
- 📁 Lock and unlock entire folders (recursive, including subfolders)
- 🧊 Glassmorphism-inspired modern UI
- 🎨 Dark premium dashboard with icons
- 🔐 Password-based AES symmetric encryption
- ❌ Passwords are never stored
- 🖥️ Simple and user-friendly desktop interface

---

## 🧠 Who Should Use This Application?

- 🎓 College students for academic projects
- 🧑‍💻 Beginners learning Python desktop development
- 🔐 Users who want basic local file privacy
- 📁 Anyone who wants to lock personal files or folders easily

---

## ⚙️ Technologies Used

- **Python 3**
- **Tkinter** – for GUI development
- **Cryptography (Fernet / AES)** – for secure encryption
- **Git & GitHub** – for version control

---

## 📁 Project Structure

secure-file-locker/
├── encryption.py # Encryption and decryption logic
├── gui.py # GUI, login, dashboard, and actions
└── README.md # Project documentation


---

## 🚀 How to Run This Project on Another Laptop (Step-by-Step)

Follow these steps carefully to run this project on any Windows laptop.

---

### 1️⃣ Install Python

1. Go to: https://www.python.org/downloads/
2. Download **Python 3.9 or above**
3. During installation:
   - ✅ Check **Add Python to PATH**
   - Click **Install Now**

To verify installation, open Command Prompt and run:


---

### 2️⃣ Download the Project from GitHub

You can download the project in either of these ways:

#### Option A: Download ZIP
1. Go to the GitHub repository
2. Click **Code → Download ZIP**
3. Extract the ZIP file

#### Option B: Clone using Git
git clone https://github.com/anshumanrai433/File-Locker.git


---

### 3️⃣ Install Required Python Library

Open Command Prompt / Terminal inside the project folder and run:


---

### 4️⃣ Run the Application

Navigate to the project folder and run:


---

### 5️⃣ Login Credentials

- **App Login Password:**


- **Encryption Password:**
  - User-defined
  - Used to encrypt and decrypt files/folders
  - Must be the same for locking and unlocking

---

## 🧭 How the Application Works

1. User logs in using the app password
2. User enters an encryption password
3. User selects a file, multiple files, or a folder
4. Selected items are encrypted and locked
5. Without the correct password, files cannot be opened or restored

---

## 🔐 Security Details

- Uses **AES-based symmetric encryption**
- Same password is required for encryption and decryption
- Passwords are **never stored** anywhere
- Encrypted files are unreadable without the correct password
- Wrong password results in access denial

---

## 🧪 Error Handling

- Displays error messages for:
  - Wrong passwords
  - Invalid file or folder selection
  - Unauthorized access attempts

---

## 🚀 Future Enhancements

The following features can be added in future versions:

- 🔄 Change login password functionality
- 📦 Convert application into an EXE installer
- 🌗 Light/Dark mode toggle
- ☁️ Cloud backup integration
- 🔐 Individual password for folders
- 🖼️ File preview locking
- 🧾 Activity log and history tracking

---

## 🎓 Viva Explanation (Quick Summary)

> Secure File Locker is a Python-based desktop application that uses AES symmetric encryption to protect files and folders.  
> It provides a graphical interface built with Tkinter and supports bulk encryption, folder encryption, and login-based access control.  
> Passwords are never stored, ensuring user privacy and security.

---

## ⚠️ Disclaimer

This project is developed **for educational purposes only**.  
It is not intended for enterprise-level or commercial security use.

---

## 👨‍💻 Author

**Anshuman Rai**  
B.Tech Computer Science & Engineering  
GitHub: https://github.com/anshumanrai433

