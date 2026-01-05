import base64
import os
import hashlib
from cryptography.fernet import Fernet


# ---------- KEY GENERATION ----------
def generate_key(password: str) -> bytes:
    password_bytes = password.encode()
    sha = hashlib.sha256(password_bytes).digest()
    return base64.urlsafe_b64encode(sha)


# ---------- SINGLE FILE ----------
def encrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    locked_path = file_path + ".locked"
    with open(locked_path, "wb") as f:
        f.write(encrypted)

    os.remove(file_path)
    return locked_path


def decrypt_file(file_path: str, password: str):
    key = generate_key(password)
    fernet = Fernet(key)

    with open(file_path, "rb") as f:
        encrypted = f.read()

    decrypted = fernet.decrypt(encrypted)

    original_path = file_path.replace(".locked", "")
    with open(original_path, "wb") as f:
        f.write(decrypted)

    os.remove(file_path)
    return original_path


# ---------- MULTIPLE FILES ----------
def encrypt_multiple_files(files, password):
    locked = []
    for file in files:
        if not file.endswith(".locked"):
            locked.append(encrypt_file(file, password))
    return locked


def decrypt_multiple_files(files, password):
    unlocked = []
    for file in files:
        if file.endswith(".locked"):
            unlocked.append(decrypt_file(file, password))
    return unlocked


# ---------- FOLDER ----------
def encrypt_folder(folder_path, password):
    locked = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            if not full_path.endswith(".locked"):
                locked.append(encrypt_file(full_path, password))
    return locked


def decrypt_folder(folder_path, password):
    unlocked = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".locked"):
                full_path = os.path.join(root, file)
                unlocked.append(decrypt_file(full_path, password))
    return unlocked
