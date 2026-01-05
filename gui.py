import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import (
    encrypt_file, decrypt_file,
    encrypt_multiple_files, decrypt_multiple_files,
    encrypt_folder, decrypt_folder
)

APP_PASSWORD = "admin123"

# ================= LOGIN =================
def check_login():
    if login_pass.get() == APP_PASSWORD:
        login.destroy()
        open_dashboard()
    else:
        messagebox.showerror("Access Denied", "❌ Wrong Login Password")

login = tk.Tk()
login.title("Secure File Locker")
login.geometry("700x480")
login.configure(bg="#020617")
login.resizable(False, False)
login.eval("tk::PlaceWindow . center")

# Glass Card
login_card = tk.Frame(login, bg="#0f172a", bd=0)
login_card.place(relx=0.5, rely=0.5, anchor="center", width=520, height=360)

tk.Label(
    login_card,
    text="🔐 Secure File Locker",
    fg="white",
    bg="#0f172a",
    font=("Segoe UI", 28, "bold")
).pack(pady=35)

tk.Label(
    login_card,
    text="Enter App Password",
    fg="#cbd5e1",
    bg="#0f172a",
    font=("Segoe UI", 14)
).pack(pady=10)

login_pass = tk.Entry(
    login_card,
    show="*",
    width=32,
    font=("Segoe UI", 16),
    justify="center",
    bd=0
)
login_pass.pack(pady=15, ipady=8)

tk.Button(
    login_card,
    text="🚀 LOGIN",
    bg="#2563eb",
    fg="white",
    font=("Segoe UI", 16, "bold"),
    width=18,
    height=2,
    bd=0,
    activebackground="#1d4ed8",
    command=check_login
).pack(pady=30)

# ================= DASHBOARD =================
def open_dashboard():
    app = tk.Tk()
    app.title("Secure File Locker – Dashboard")
    app.geometry("1200x720")
    app.configure(bg="#020617")
    app.resizable(False, False)
    app.eval("tk::PlaceWindow . center")

    # Sidebar (Glass)
    sidebar = tk.Frame(app, bg="#020617", width=260)
    sidebar.pack(side="left", fill="y")

    sidebar_card = tk.Frame(sidebar, bg="#0f172a")
    sidebar_card.place(x=20, y=30, width=220, height=660)

    tk.Label(
        sidebar_card,
        text="🛡️\nSecure\nLocker",
        fg="white",
        bg="#0f172a",
        font=("Segoe UI", 22, "bold"),
        justify="center"
    ).pack(pady=40)

    tk.Label(
        sidebar_card,
        text="🔒 Encrypt\n🔓 Decrypt\n📂 Folder Lock\n📁 Multi-File",
        fg="#cbd5e1",
        bg="#0f172a",
        font=("Segoe UI", 13),
        justify="left"
    ).pack(pady=20)

    # Main Area
    main = tk.Frame(app, bg="#020617")
    main.pack(expand=True, fill="both")

    # Glass Panel
    glass = tk.Frame(main, bg="#0f172a")
    glass.place(relx=0.5, rely=0.5, anchor="center", width=820, height=620)

    tk.Label(
        glass,
        text="📊 Dashboard",
        fg="white",
        bg="#0f172a",
        font=("Segoe UI", 26, "bold")
    ).pack(pady=25)

    tk.Label(
        glass,
        text="Encryption Password",
        fg="#94a3b8",
        bg="#0f172a",
        font=("Segoe UI", 14)
    ).pack()

    password_entry = tk.Entry(
        glass,
        show="*",
        width=38,
        font=("Segoe UI", 15),
        justify="center",
        bd=0
    )
    password_entry.pack(pady=12, ipady=6)

    status = tk.Label(
        glass,
        text="🟢 Status: Ready",
        fg="#22c55e",
        bg="#0f172a",
        font=("Segoe UI", 12, "bold")
    )
    status.pack(pady=15)

    # -------- ACTIONS --------
    def lock_file():
        p = filedialog.askopenfilename()
        if p:
            encrypt_file(p, password_entry.get())
            status.config(text="🔒 File Locked")

    def unlock_file():
        p = filedialog.askopenfilename()
        if p:
            decrypt_file(p, password_entry.get())
            status.config(text="🔓 File Unlocked")

    def lock_multi():
        f = filedialog.askopenfilenames()
        if f:
            c = len(encrypt_multiple_files(f, password_entry.get()))
            status.config(text=f"📂 {c} files locked")

    def unlock_multi():
        f = filedialog.askopenfilenames()
        if f:
            c = len(decrypt_multiple_files(f, password_entry.get()))
            status.config(text=f"📂 {c} files unlocked")

    def lock_folder_ui():
        d = filedialog.askdirectory()
        if d:
            c = len(encrypt_folder(d, password_entry.get()))
            status.config(text=f"📁 Folder locked ({c} files)")

    def unlock_folder_ui():
        d = filedialog.askdirectory()
        if d:
            c = len(decrypt_folder(d, password_entry.get()))
            status.config(text=f"📁 Folder unlocked ({c} files)")

    btn = {
        "width": 30,
        "height": 2,
        "fg": "white",
        "font": ("Segoe UI", 14, "bold"),
        "bd": 0
    }

    tk.Button(glass, text="🔒 Lock File", bg="#2563eb", command=lock_file, **btn).pack(pady=6)
    tk.Button(glass, text="🔓 Unlock File", bg="#16a34a", command=unlock_file, **btn).pack(pady=6)
    tk.Button(glass, text="📂 Lock Multiple Files", bg="#0ea5e9", command=lock_multi, **btn).pack(pady=6)
    tk.Button(glass, text="📂 Unlock Multiple Files", bg="#22c55e", command=unlock_multi, **btn).pack(pady=6)
    tk.Button(glass, text="📁 Lock Folder", bg="#7c3aed", command=lock_folder_ui, **btn).pack(pady=6)
    tk.Button(glass, text="📁 Unlock Folder", bg="#a855f7", command=unlock_folder_ui, **btn).pack(pady=6)

    tk.Button(glass, text="❌ Exit App", bg="#dc2626", command=app.destroy, **btn).pack(pady=25)

    app.mainloop()

login.mainloop()
