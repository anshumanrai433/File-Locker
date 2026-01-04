from encryption import encrypt_file, decrypt_file

choice = input("Enter choice (lock/unlock): ").lower()
file_path = input("Enter file path: ")
password = input("Enter password: ")

try:
    if choice == "lock":
        locked = encrypt_file(file_path, password)
        print("File locked:", locked)

    elif choice == "unlock":
        unlocked = decrypt_file(file_path, password)
        print("File unlocked:", unlocked)

    else:
        print("Invalid choice")

except Exception as e:
    print("Error:", e)
