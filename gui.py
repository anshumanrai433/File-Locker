import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt_file, decrypt_file


def lock_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return

    try:
        locked_path = encrypt_file(file_path, password)
        messagebox.showinfo("Success", f"File locked:\n{locked_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def unlock_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password")
        return

    try:
        unlocked_path = decrypt_file(file_path, password)
        messagebox.showinfo("Success", f"File unlocked:\n{unlocked_path}")
    except Exception:
        messagebox.showerror("Error", "Wrong password or invalid file")


# Main window
app = tk.Tk()
app.title("Secure File Locker")
app.geometry("400x250")
app.resizable(False, False)

# Title
tk.Label(app, text="Secure File Locker", font=("Arial", 16, "bold")).pack(pady=10)

# Password input
tk.Label(app, text="Enter Password").pack()
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack(pady=5)

# Buttons
tk.Button(app, text="🔒 Lock File", width=20, command=lock_file).pack(pady=5)
tk.Button(app, text="🔓 Unlock File", width=20, command=unlock_file).pack(pady=5)

# Exit
tk.Button(app, text="Exit", width=10, command=app.destroy).pack(pady=10)

app.mainloop()
