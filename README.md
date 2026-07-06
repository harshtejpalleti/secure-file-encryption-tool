# 🔐 CipherVault

CipherVault is a desktop application built with **Python** that allows users to securely encrypt and decrypt files using a password. The application uses **AES-256 encryption (AES-GCM)** for data security and provides a clean graphical interface built with **CustomTkinter**.

---

## ✨ Features

- 🔒 Encrypt files securely using AES-256 (AES-GCM)
- 🔓 Decrypt encrypted files with the correct password
- 📁 Browse and select files through an easy-to-use GUI
- 📊 Progress bar to indicate encryption/decryption completion
- ⚡ Fast and lightweight desktop application
- 🖥️ Modern dark-themed interface
- ⚠️ Error handling for invalid files or incorrect passwords

---

## 🛠️ Technologies Used

- Python 3
- CustomTkinter
- Tkinter
- Cryptography Library
- AES-GCM (AES-256)
- PBKDF2-HMAC (SHA-256)

---

## 📂 Project Structure

```
CipherVault/
│
├── main.py
├── crypto_utils.py
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/harshtejpalleti/CipherVault.git
```

### 2. Open the project folder

```bash
cd CipherVault
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

---

## 📖 How to Use

1. Launch the application.
2. Click **Browse File** and select the file you want to encrypt.
3. Enter a secure password.
4. Click **Encrypt** to create an encrypted `.enc` file.
5. To decrypt, select the encrypted file, enter the same password, and click **Decrypt**.

---

## 🔒 Security

CipherVault protects files using modern cryptographic techniques:

- **AES-256 GCM** for authenticated encryption
- **PBKDF2-HMAC (SHA-256)** for secure password-based key generation
- Random **16-byte salt** for every encryption
- Random **12-byte nonce** for every encrypted file
- Password is never stored or saved

---

## 💡 Future Improvements

- Drag and drop file support
- Multiple file encryption
- Password visibility toggle
- Password strength indicator
- File encryption history
- Build a standalone executable (.exe)

---

## 📸 User Interface

The application includes:

- Modern dark-themed GUI
- File selection dialog
- Password input field
- Encrypt and Decrypt buttons
- Progress bar
- Status indicator
- Success and error pop-up messages

---

## 👨‍💻 Author

**Palleti Venkata Harsh Tej Reddy**

B.Tech – Computer Science & Engineering (Cybersecurity)

GitHub: https://github.com/harshtejpalleti

LinkedIn: https://www.linkedin.com/in/harsh-tej-reddy-palleti-venkata-013550312/

---

## 📄 License

This project is developed for educational and learning purposes.

Feel free to use, modify, and improve the project for personal or academic use.
