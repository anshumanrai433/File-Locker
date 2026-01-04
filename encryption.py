import base64
import os
from cryptography.fernet import Fernet
import hashlib


def generate_key(password: str) -> bytes:
    password_bytes = password.encode()
    sha256 = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(sha256)


def encrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()

    encrypted_data = fernet.encrypt(data)

    encrypted_file_path = file_path + ".locked"
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_data)

    os.remove(file_path)
    return encrypted_file_path


def decrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    original_file_path = file_path.replace(".locked", "")
    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)

    os.remove(file_path)
    return original_file_path
