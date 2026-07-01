# Criptografar o decoded_data no meio e dar uma mensagem engraçada
import platform
import sys
import os
import time
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

AES_KEY = b'pr4nasecretaeske'
AES_IV = b'initialvector123'

def pad(data):
    padder = padding.PKCS7(128).padder()
    return padder.update(data) + padder.finalize()

def unpad(data):
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(data) + unpadder.finalize()

def encrypt_aes(data):
    cipher = Cipher(algorithms.AES(AES_KEY), modes.CBC(AES_IV), backend=default_backend())
    encryptor = cipher.encryptor()
    padded_data = pad(data)
    return encryptor.update(padded_data) + encryptor.finalize()

def unxor_file(input_file, output_file, xor_key=35):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()
        
        decoded_data = bytearray([byte ^ xor_key for byte in data])
        print(decoded_data)
        encrypted_data = encrypt_aes(decoded_data)

        if encrypted_data:
            print("Dados criptografados com sucesso!\n")

            
        with open(output_file, 'wb') as f:
            f.write(decoded_data)
        
        print(f"File '{input_file}' successfully un-XORed and saved as '{output_file}'")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python un_file.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        unxor_file(input_file, output_file)

