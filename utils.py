from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import os

SALT_SIZE = 16
KEY_SIZE = 32  # AES-256
ITERATIONS = 100000

def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=KEY_SIZE, count=ITERATIONS)

def pad(data):
    padding_length = AES.block_size - len(data) % AES.block_size 
    return data + bytes([padding_length]) * padding_length

def unpad(data):
    return data[:-data[-1]]

def encrypt_file(input_file, output_file, password):
    salt = get_random_bytes(SALT_SIZE)
    key = derive_key(password, salt)

    cipher = AES.new(key, AES.MODE_CBC)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    padded_data = pad(plaintext)
    ciphertext = cipher.encrypt(padded_data)

    with open(output_file, 'wb') as f:
        f.write(salt + cipher.iv + ciphertext)

    print(f"[+] File encrypted successfully → {output_file}")

def decrypt_file(input_file, output_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(SALT_SIZE)
        iv = f.read(16)
        ciphertext = f.read()

    key = derive_key(password, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    decrypted = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

    print(f"[+] File decrypted successfully → {output_file}")
