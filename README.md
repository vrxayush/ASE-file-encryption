# AES File Encryption Tool 🔐

This project is a Python-based file encryption and decryption tool using AES-256 encryption.

## Features
- AES-256 encryption (CBC mode)
- Password-based key derivation (PBKDF2)
- File encryption & decryption
- Secure salt + IV usage

## Usage

### Encrypt
python encrypt.py input.txt encrypted.bin password

### Decrypt
python decrypt.py encrypted.bin output.txt password

## Requirements
pip install pycryptodome
