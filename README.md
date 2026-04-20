# 🔐 AES File Encryption Tool

A secure file encryption and decryption tool built using Python that uses Advanced Encryption Standard (AES) to protect sensitive data.

---

## 🚀 Features

- 🔐 Encrypt files using AES encryption  
- 🔓 Decrypt encrypted files securely  
- 🗂️ Supports any file type (text, images, PDFs, etc.)  
- 🔑 Password-based encryption  
- ⚡ Fast and lightweight CLI-based tool  

---

## 🧠 How It Works

1. User provides a file and password  
2. The password is converted into a secure encryption key  
3. File is encrypted using AES algorithm  
4. Encrypted file can only be decrypted using the correct password  

---

## 🎥 Demo Video

Demo video of the project is uploaded in [YouTube](https://youtu.be/tM9Ht8uBsZU?si=1-es9uUOPx1VXSZz)

---

## 🛠️ Tech Stack

- Python  
- Cryptography Library (AES)  

---

## 📁 Project Structure


```

aes-file-encryption/
│
├── encrypt.py 
├── decrypt.py 
├── utils.py 
├── requirements.txt
└── README.md

```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/vrxayush/aes-file-encryption.git
cd aes-file-encryption
```

### 2️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 3️⃣ Usage
🔐 Encrypt a File
``` 
python encrypt.py
```
🔓 Decrypt a File
```
python decrypt.py
```

---
## 🔑 Example
1. Input: `file.txt`
2. Output: `file.enc` (encrypted)
3. Decrypted back using same password

### ⚠️ Important Notes

- Keep your password secure (cannot recover if lost)
- Works locally (no cloud storage involved)
- Designed for educational and security purposes

---
## 📈 Future Improvements

- 🖥️ GUI interface
- 📂 Batch file encryption
- ☁️ Secure cloud integration
- 🔐 Key management system

## 🎯 Use Case

This project demonstrates:

- Encryption techniques
- File security
- Cryptography fundamentals
- Secure data handling
---
## 👨‍💻 Author

Ayush Shah  
Computer Science Engineering Student  
Specialization: IoT, Cyber Security, Blockchain
