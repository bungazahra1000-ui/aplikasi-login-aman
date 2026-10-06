import tkinter as tk
from tkinter import messagebox
import datetime
import platform
import os

def is_sql_injection(text):
    patterns = ["' OR", "\" OR", " OR 1=1", "1=1", "--", " UNION ", " SELECT ", " DROP ", "';"]
    text_upper = text.upper()
    for p in patterns:
        if p.upper() in text_upper:
            return True, p
    return False, ""

def log_activity(username, status, threat=""):
    waktu = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    laptop = platform.node()
    line = f"[{waktu}] User:{username} | Status:{status} | Threat:{threat} | Laptop:{laptop} | Lokasi:Jekulo\n"
    with open("database.txt", "a", encoding="utf-8") as f:
        f.write(line)

def daftar():
    user = entry_user.get()
    pw = entry_pass.get()
    if not user or not pw:
        messagebox.showwarning("Gagal", "Username & Password wajib diisi!")
        return
    serangan, pola = is_sql_injection(user + " " + pw)
    if serangan:
        log_activity(user, "BLOCKED - SQL INJECTION", pola)
        messagebox.showerror("🚨 SERANGAN TERDETEKSI! 🚨", f"Blue Team Alert!\nPola: {pola}\nAksi: DIBLOKIR & DICATAT")
        return
    log_activity(user, "DAFTAR AKUN - AMAN")
    messagebox.showinfo("Sukses", f"Akun {user} berhasil! Status: AMAN")

def login():
    user = entry_user.get()
    serangan, pola = is_sql_injection(user)
    if serangan:
        log_activity(user, "BLOCKED - LOGIN INJECTION", pola)
        messagebox.showerror("🚨 INTRUSION DETECTED", f"Pola: {pola}\nLogin diblokir!")
        return
    log_activity(user, "LOGIN - AMAN")
    messagebox.showinfo("Login", f"Welcome {user}! AMAN")

def scan_laptop():
    info = f"Laptop: {platform.node()}\nOS: {platform.system()}\nLokasi: Jekulo\n\nFirewall: Aktif\nBlue Team Mode: ON"
    messagebox.showinfo("SCAN LAPTOP", info)

root = tk.Tk()
root.title("BUNGA HACKER v8.0 - Blue Team Detector - Axioo Hype 1")
root.geometry("500x400")
root.configure(bg="black")
tk.Label(root, text="BUNGA CYBER SYSTEM", fg="#00FF00", bg="black", font=("Consolas", 18, "bold")).pack(pady=10)
tk.Label(root, text="🔵 BLUE TEAM - THREAT DETECTOR MODE", fg="cyan", bg="black", font=("Consolas", 10)).pack()
tk.Label(root, text="Username:", fg="white", bg="black").pack(pady=(20,0))
entry_user = tk.Entry(root, width=40, font=("Consolas", 11))
entry_user.pack()
entry_user.insert(0, "orang_araa")
tk.Label(root, text="Password:", fg="white", bg="black").pack(pady=(10,0))
entry_pass = tk.Entry(root, width=40, show="*", font=("Consolas", 11))
entry_pass.pack()
tk.Button(root, text="DAFTAR AKUN", bg="#00FF00", fg="black", font=("Consolas", 11, "bold"), width=25, command=daftar).pack(pady=(15,5))
tk.Button(root, text="LOGIN", bg="#00BFFF", fg="white", font=("Consolas", 11, "bold"), width=25, command=login).pack(pady=5)
tk.Button(root, text="SCAN LAPTOP", bg="orange", fg="black", font=("Consolas", 10, "bold"), width=25, command=scan_laptop).pack(pady=5)
tk.Label(root, text="Jekulo | Blue Team | SOC Analyst Journey | 08/10/2026", fg="gray", bg="black", font=("Consolas", 8)).pack(side=tk.BOTTOM, pady=5)
root.mainloop()
