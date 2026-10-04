import hashlib, time
from datetime import datetime

def jadi_hash(pw):
    return hashlib.sha256(pw.encode()).hexdigest()

print("=== APLIKASI CYBERSECURITY BUNGA v1.0 ===")
print("Laptop: Axioo Hype 1 - Mode Hacker Aktif")
print("")

# DAFTAR DULU
print("--- DAFTAR AKUN BARU ---")
user_baru = input("Bikin username: ")
pw_baru = input("Bikin password kuat: ")
hash_baru = jadi_hash(pw_baru)

# Simpen ke database rahasia
with open("database.txt", "w") as f:
    f.write(f"{user_baru}:{hash_baru}")

print(f"\n✅ Akun {user_baru} berhasil dibuat! Hash disimpan!")
print("Sekarang coba LOGIN\n")
time.sleep(1)

# LOGIN
percobaan = 0
while percobaan < 3:
    print(f"--- LOGIN (Percobaan {percobaan+1}/3) ---")
    u = input("Username: ")
    p = input("Password: ")

    # Cek database
    with open("database.txt", "r") as f:
        data = f.read().split(":")
        user_asli = data[0]
        hash_asli = data[1].strip()

    if u == user_asli and jadi_hash(p) == hash_asli:
        print("\n🎉 AKSES DITERIMA! SELAMAT DATANG HACKER BUNGA!")
        print(f"Login jam {datetime.now()}")
        break
    else:
        percobaan += 1
        print("❌ SALAH!")
        with open("log_hacker.txt", "a") as log:
            log.write(f"GAGAL LOGIN jam {datetime.now()} coba user:{u} pw:{p}\n")

if percobaan == 3:
    print("\n🚨 AKUN TERKUNCI 10 DETIK!")
    for i in range(10, 0, -1):
        print(f"Terkunci... {i}")
        time.sleep(1)

input("")
