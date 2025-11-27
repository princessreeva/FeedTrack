import os
import csv
import pandas as pd
from tabulate import tabulate

# ---------- CEK FILE AKUN ----------
def cekakun():
    if not os.path.exists('akun.csv'):
        with open('akun.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])


# ---------- LOGIN CUSTOMER --------
def login():
    os.system('cls')
    tampilkan_judul()
    print("╔════════════════ ♡═════════════╗")
    print("   𝐋 𝐎 𝐆 𝐈 𝐍  𝐂 𝐔 𝐒 𝐓 𝐎 𝐌 𝐄 𝐑   ")
    print("╚═══════════════♡ ══════════════╝")
    cekakun()
    username = input('Masukkan Username : ')
    password = input('Masukkan Password : ')

    loginsukses = False
    with open('akun.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username and row['Password'] == password:
                loginsukses = True
                break

    if loginsukses:
        usernamelogin = username
        print('Login berhasil.')
        input('Tekan Enter untuk melanjutkan.')
        os.system('cls')
        pembeli_main()
    else:
        print('Username atau Password salah.')
        input('Tekan Enter untuk kembali ke menu utama...')
        tampilanawal()


# ---------- REGISTER ----------
def register():
    os.system('cls')
    tampilkan_judul()
    print("╔═══════════ ♡═════════╗")
    print("    𝐑 𝐄 𝐆 𝐈 𝐒 𝐓 𝐄 𝐑    ")
    print("╚═══════════♡ ═════════╝")
    cekakun()

    # Ambil username yang sudah ada
    with open('akun.csv', mode='r') as file:
        username_sama = {row['Username'] for row in csv.DictReader(file)}

    while True:
        username = input('Daftarkan Username anda : ')
        if len(username) < 2:
            print('Username minimal 2 huruf.')
            continue
        if username in username_sama:
            print('Username sudah digunakan!')
            continue
        break

    while True:
        password = input('Masukkan Kata Sandi (min 8 karakter): ')
        if len(password) < 8:
            print('Password terlalu pendek.')
            continue
        break

    # Konfirmasi
    print(f'\nUsername : {username}\nPassword : {password}')
    cek = input('Apakah sudah benar? (y/t): ').lower()
    if cek == 'y':
        with open('akun.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        print('Registrasi berhasil! Silahkan login.')
    else:
        print('Registrasi dibatalkan.')

    input('Tekan Enter untuk kembali ke menu utama...')
    tampilanawal()


# ---------- LOGIN PENJUAL ----------
def loginpenjual():
    os.system('cls')
    tampilkan_judul()
    print("╔═════════════ ♡═════════════╗")
    print("   𝐋 𝐎 𝐆 𝐈 𝐍  𝐏 𝐄 𝐍 𝐉 𝐔 𝐀 𝐋   ")
    print("╚═════════════♡ ═════════════╝")
    if not os.path.exists('admin.csv'):
        with open('admin.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Username', 'Password'])
            writer.writerow(['admin', 'admin123'])

    while True:
        username = input('Masukkan Nama Pengguna Anda : ')
        password = input('Masukkan Kata Sandi Anda : ')

        login_sukses = False
        with open('admin.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Username'] == username and row['Password'] == password:
                    login_sukses = True
                    break

        if login_sukses:
            print("Login Anda Sebagai Penjual Berhasil")
            input('Tekan Enter Untuk Melanjutkan')
            os.system('cls' if os.name == 'nt' else 'clear')
            menupenjual()
            break
        else:
            print('Username atau Password salah.')
            cek = input('Apakah anda ingin mencoba lagi (y/t)? ').lower()
            if cek == 't':
                break

                

def tampilkan_judul():
    try:
        with open("judul.txt", "r", encoding="utf-8") as file:
            isi = file.read()
            print(isi)
    except FileNotFoundError:
        print("File judul.txt tidak ditemukan")

# ---------- MENU AWAL ----------
def tampilanawal():
    while True:
        os.system('cls')
        tampilkan_judul()
        print("✧･ﾟ: ✧･ﾟ: ✦ ——————————————————————————————  ✦ :･ﾟ✧:･ﾟ✧")
        print("              SELAMAT DATANG DI FEEDTRACK               ")
        print("           \"APLIKASI LAYANAN PAKAN TERNAK\"            ")
        print("✧･ﾟ: ✧･ﾟ: ✦ ——————————————————————————————  ✦ :･ﾟ✧:･ﾟ✧")

        print("Silahkan pilih menu:")
        print("[1] LOGIN CUSTOMER")
        print("[2] LOGIN PENJUAL")
        print("[3] REGISTER")
        print("[4] KELUAR")
        pilihan = input('Masukkan menu pilihan anda : ').lower()

        if pilihan in ('1', 'login customer'):
            login()
        elif pilihan in ('2', 'login penjual'):
            loginpenjual()
        elif pilihan in ('3', 'register'):
            register()
        elif pilihan in ('4', 'keluar', 'exit'):
            os.system('cls')
            print('Terima kasih telah menggunakan aplikasi!')
            break
        else:
            input('Pilihan tidak valid. Tekan Enter untuk ulang...')


# ---------- MENU COSTUMER ----------


#struktur yang hewan, hardcode

def daftar_hewan():
    print("\n✧･ﾟ: ✧ PILIH HEWAN TERNAK ✧:･ﾟ✧")

    hewan = ["🐄 Sapi", "🐐 Kambing", "🐓 Ayam"]
    for i, h in enumerate(hewan, 1):
        print(f"{i}. {h}")

    return ["Sapi", "Kambing", "Ayam"]


#csv pakan

def baca_pakan():
    data = []
    try:
        with open("Pakan.csv", "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print("File Pakan.csv tidak ditemukan.")
    return data

def tampilkan_pakan(hewan, daftar_pakan):
    print(f"\n⋆˙⟡⟡ DAFTAR PAKAN UNTUK {hewan.upper()} ⟡⟡˙⋆")

    pakan_hewan = [p for p in daftar_pakan if p["Hewan"] == hewan]

    if not pakan_hewan:
        print("Tidak ada pakan untuk hewan ini.")
        return []

    for i, p in enumerate(pakan_hewan, 1):
        print(f"{i}. 🌾 {p['Pakan']} — 💸 Rp{p['Harga']}")

    return pakan_hewan

#voucher csv

def baca_voucher():
    voucher = {}
    try:
        with open("Voucher.csv", "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            for row in reader:
                voucher[row["Kode"]] = int(row["Diskon"])
    except FileNotFoundError:
        print("File Voucher.csv tidak ditemukan.")
    return voucher


#totals

def hitung_total(harga, jumlah, kode_voucher, daftar_voucher):
    subtotal = harga * jumlah
    diskon = 0

    if kode_voucher in daftar_voucher:
        diskon = subtotal * daftar_voucher[kode_voucher] / 100

    total = subtotal - diskon
    return subtotal, diskon, total


#tampiln pembeli

def menu_pembeli():
    print("\n⋆｡‧˚ʚ♡ɞ˚‧｡⋆  MENU PEMBELI  ⋆｡‧˚ʚ♡ɞ˚‧｡⋆")
    print("[1] 🛒 Beli Pakan")
    print("[2] 🧾 Struk Belanja")
    print("[3] 🚪 Logout")

def pembayaran(grand_total):
    os.system('cls')
    print("⋆˙⟡⟡─── PILIH METODE PEMBAYARAN ───⟡⟡˙⋆")
    print("[1] Transfer Bank")
    print("[2] E-Wallet")
    print("[3] Bayar di Tempat (COD)")

    metode = input("Pilih metode pembayaran [1/2/3]: ")

    if metode == "1":
        print("✦•········ TRANSFER BANK ········•✦")
        print("Bank BRI : 1234 5678 9012 a.n FeedTrack")
        print("Bank BCA : 9876 5432 1098 a.n FeedTrack")
        print(f"Total yang harus dibayar: Rp{grand_total}")
        input("Tekan Enter setelah melakukan pembayaran...")
        return "Transfer Bank"

    elif metode == "2":
        print("✦•········ E-WALLET ········•")
        print("Dana : 0812-3456-7890")
        print("OVO  : 0812-3456-7890")
        print("Gopay: 0812-3456-7890")
        print(f"Total yang harus dibayar: Rp{grand_total}")
        input("Tekan Enter setelah melakukan pembayaran...")
        return "E-Wallet"

    elif metode == "3":
        print("✦•········ COD (Bayar di Tempat) ········•")
        print("Silakan bayar kepada kurir saat pesanan tiba.")
        print(f"Total: Rp{grand_total}")
        input("Tekan Enter untuk konfirmasi...")
        return "COD"
    
    else:
        print("Pilihan tidak valid. Ulangi.")
        return pembayaran(grand_total)

#keranjangs

# === FITUR BARU: Gabungkan item yang sama ===
def gabungkan_keranjang(keranjang):
    hasil = {}
    for item in keranjang:
        key = item['pakan']  # pengelompokan berdasarkan nama pakan

        if key not in hasil:
            hasil[key] = {
                "hewan": item["hewan"],
                "pakan": item["pakan"],
                "harga": item["harga"],
                "jumlah": item["jumlah"],
                "subtotal": item["subtotal"]
            }
        else:
            # Menambah jumlah dan subtotal
            hasil[key]["jumlah"] += item["jumlah"]
            hasil[key]["subtotal"] += item["subtotal"]

    return list(hasil.values())

# === FITUR BARU: Simpan struk ke CSV ===
def simpan_struk_csv(keranjang, grand_total, diskon, total_akhir, metode):
    nama_file = "struk.csv"

    # Jika file belum ada → buat header
    file_baru = not os.path.exists(nama_file)

    with open(nama_file, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if file_baru:
            writer.writerow(["Hewan", "Pakan", "Harga", "Jumlah", "Subtotal",
                             "Total Awal", "Diskon", "Total Akhir", "Metode Pembayaran"])

        # Simpan item keranjang
        for item in keranjang:
            writer.writerow([
                item["hewan"],
                item["pakan"],
                item["harga"],
                item["jumlah"],
                item["subtotal"],
                grand_total,
                diskon,
                total_akhir,
                metode
            ])




def pembeli_main():
    keranjang = []  

    while True:
        os.system('cls')
        menu_pembeli()
        pilih = input("Pilih menu [1/2/3]: ")

        if pilih == "1":
            os.system('cls')

            while True:
                os.system('cls')
                hewan_list = daftar_hewan()
                daftar_pakan = baca_pakan()

                try:
                    pilih_hewan = int(input("Pilih hewan: "))
                    hewan = hewan_list[pilih_hewan - 1]
                except:
                    print("Pilihan tidak valid.")
                    continue

                pakan_hewan = tampilkan_pakan(hewan, daftar_pakan)
                if not pakan_hewan:
                    continue

                try:
                    pilih_pakan = int(input("Pilih pakan: "))
                    barang = pakan_hewan[pilih_pakan - 1]
                except:
                    print("Pilihan tidak valid.")
                    continue

                jumlah = int(input("Jumlah beli: "))
                harga = float(barang["Harga"])

                keranjang.append({
                    "hewan": hewan,
                    "pakan": barang["Pakan"],
                    "harga": harga,
                    "jumlah": jumlah,
                    "subtotal": harga * jumlah
                })

                lanjut = input("Tambah pembelian lain? (y/n): ").lower()
                if lanjut != "y":
                    break

        #struks
        elif pilih == "2":
            os.system('cls')

            if keranjang:

                #Hitung total awal
                grand_total = sum(item["subtotal"] for item in keranjang)
                print("TOTAL BELANJA SEBELUM DISKON :", grand_total)

                #vouch
                voucher_list = baca_voucher()
                kode_voucher = input("Masukkan kode voucher (opsional): ").upper()

                diskon = 0
                if kode_voucher in voucher_list:
                    persen = voucher_list[kode_voucher]
                    diskon = grand_total * persen / 100
                    print(f"Voucher valid! Diskon {persen}% diterapkan.")
                else:
                    print("Tidak ada voucher atau kode tidak valid.")

                #Total akhir setelah diskon
                total_setelah_diskon = grand_total - diskon

                #Pembayaran
                metode_bayar = pembayaran(total_setelah_diskon)

                #Cetak struks
                os.system('cls')
                print("\n𐙚₊˚⊹♡  STRUK BELANJA FEEDTRACK  ♡⊹˚₊𐙚")
                print("—☆✧—☆✧—☆✧—☆✧—☆✧—☆✧——☆✧—☆✧—☆✧—☆✧✧—☆✧")

                # === FITUR BARU: Gabungkan item dengan pakan yang sama ===
                keranjang = gabungkan_keranjang(keranjang)

                for item in keranjang:
                    print("")
                    print(f"🐾 Hewan   : {item['hewan']}     ")
                    print(f"🌾 Pakan   : {item['pakan']}     ")
                    print(f"🧺 Jumlah  : {item['jumlah']}    ")
                    print(f"💸 Subtotal: Rp{item['subtotal']}")
                    print("⋆｡‧˚ʚ♡ɞ˚‧｡⋆⋆｡‧˚ʚ♡ɞ˚‧｡⋆｡‧˚ʚ♡ɞ")
                print("")
                print(f"TOTAL SEBELUM DISKON  : Rp{grand_total}         ")
                print(f"DISKON VOUCHER        : Rp{diskon} ")
                print(f"TOTAL AKHIR           : Rp{total_setelah_diskon}") 
                print(f"METODE PEMBAYARAN     : {metode_bayar}")

                print("—☆✧—☆✧—☆✧—☆✧—☆✧—☆✧——☆✧—☆✧—☆✧—☆✧✧—☆✧")
                print("")
                print("Terima kasih telah berbelanja! ")
                # === FITUR BARU:Simpan struk ke CSV ===
                simpan_struk_csv(keranjang, grand_total, diskon, total_setelah_diskon, metode_bayar)

                input("Tekan Enter untuk kembali...")

        # LOGOUT
        elif pilih == "3":
            print("\nLogout berhasil.\n")
            break

        else:
            print("Pilihan tidak valid.")

#======================== MENU PENJUAL ==========================
def daftar_menu():
    data = pd.read_csv('Pakan.csv')
    # print(data)
    print(tabulate(data, headers='keys', tablefmt='pretty'))
    input('Tekan Enter untuk kembali ke menu penjual...')
    menupenjual()

def ubah_data():
    pakan = input("Masukkan nama pakan yang ingin diubah: ")
    harga = int(input("Masukkan harga baru: "))
    data = pd.read_csv('Pakan.csv')
    if pakan not in data['Pakan'].values:
        print("Menu tersebut tidak tersedia")
    else:
        # Update harga
        data.loc[data['Pakan'] == pakan, 'Harga'] = harga
        data.to_csv('Pakan.csv', index=False)
        print("Harga berhasil diperbarui!")
    input('Tekan Enter untuk kembali ke menu penjual...')
    menupenjual()

def tambah_data():
    hewan = input("Masukkan Nama Hewan: ")
    pakan = input("Masukkan Nama Pakan: ")
    harga = int(input("Masukkan Harga: "))
    data = pd.read_csv('Pakan.csv')
    data = pd.concat([data, pd.DataFrame([{'Hewan': hewan, 'Pakan': pakan, 'Harga': harga}])], ignore_index=True)
    data.to_csv('Pakan.csv', index=False)
    print("Menu berhasil ditambah!")
    input('Tekan Enter untuk kembali ke menu penjual...')
    menupenjual()

def hapus_data():
    pakan = input("Masukkan Nama Pakan yang ingin dihapus: ")
    data = pd.read_csv('Pakan.csv')
    if pakan not in data['Pakan'].values:
        print("Nama Pakan tersebut tidak tersedia")
    else:
        data = data[data['Pakan'] != pakan]
        data.to_csv('Pakan.csv', index=False)
        print("Menu berhasil dihapus!")
    input('Tekan Enter untuk kembali ke menu penjual...')
    menupenjual()

def rekap_struk():
    data = pd.read_csv('struk.csv')
    print(tabulate(data, headers='keys', tablefmt='pretty'))
    input('Tekan Enter untuk kembali ke menu penjual...')
    menupenjual()

def voucher():
    tampilkan_judul()
    while True :
        os.system('cls')
        print("🎀⋆｡‧˚  KELOLA VOUCHER  ˚‧｡⋆🎀")
        print("[1] 👀 Lihat Voucher")
        print("[2] ➕ Tambah Voucher")
        print("[3] ✏ Ubah Voucher")
        print("[4] ❌ Hapus Voucher")
        print("[5] 🔙 Kembali")
        pilihan = input("Masukkan opsi [1/2/3/4/5]: ")
        if pilihan == "1":
            os.system('cls')
            data = pd.read_csv('voucher.csv')
            # print(data)
            print(tabulate(data, headers='keys', tablefmt='pretty'))
            input('Tekan Enter untuk kembali ke menu kelola voucher...')

        elif pilihan == "2":
            os.system('cls')
            kode = input("Masukkan Kode: ").upper()
            diskon = int(input("Masukkan Besar Diskon: "))
            data = pd.read_csv('voucher.csv')
            data = pd.concat([data, pd.DataFrame([{'Kode': kode, 'Diskon': diskon}])], ignore_index=True)
            data.to_csv('voucher.csv', index=False)
            print("Voucher berhasil ditambah!")
            input('Tekan Enter untuk kembali ke menu kelola voucher...')

        elif pilihan == "3":
            os.system('cls')
            data = pd.read_csv('voucher.csv')
            kode = input("Masukkan kode yang ingin diubah: ").upper()
            diskon = int(input("Masukkan diskon baru: "))
            if kode not in data['Kode'].values:
                print("Kode tersebut tidak tersedia")
            else:
                 # Update harga
                data.loc[data['Kode'] == kode, 'Diskon'] = diskon
                data.to_csv('voucher.csv', index=False)
                print("Voucher berhasil diubah!")
            input('Tekan Enter untuk kembali ke menu kelola voucher...')
                 
        elif pilihan == "4":
            os.system('cls')
            kode = input("Masukkan kode yang ingin dihapus: ").upper()
            data = pd.read_csv('voucher.csv')
            if kode not in data['Kode'].values:
                print("Kode tersebut tidak tersedia")
            else:
                data = data[data['Kode'] != kode]
                data.to_csv('voucher.csv', index=False)
                print("Voucher berhasil dihapus!")
            input('Tekan Enter untuk kembali ke menu kelola voucher...')

        elif pilihan == "5":
            os.system('cls')
            tampilkan_judul()
            print("🌼⋆｡‧˚  MENU PENJUAL  ˚‧｡⋆🌼")
            print("[0] 🚪 Keluar")
            print("[1] 📋 Lihat daftar pakan")
            print("[2] ✏  Ubah daftar pakan")
            print("[3] ➕ Tambah daftar pakan")
            print("[4] ❌ Hapus daftar pakan")
            print("[5] 🎟 Kelola voucher")
            print("[6] 🧾  Lihat rekap struk")
            break 

        else:
            print("Pilihan tidak valid. Coba lagi.")

def menupenjual():
    os.system('cls')
    tampilkan_judul()
    print("🌼⋆｡‧˚  MENU PENJUAL  ˚‧｡⋆🌼")
    print("[0] 🚪 Keluar")
    print("[1] 📋 Lihat daftar pakan")
    print("[2] ✏  Ubah daftar pakan")
    print("[3] ➕ Tambah daftar pakan")
    print("[4] ❌ Hapus daftar pakan")
    print("[5] 🎟  Kelola voucher")
    print("[6] 🧾  Lihat rekap struk")
    while True :
        pilihan = input('Masukkan pilihan anda : ').lower()
        if pilihan == '1' or pilihan == 'daftar menu pakan ternak' :
            os.system('cls')
            daftar_menu()
        elif pilihan == '2' or pilihan == 'ubah daftar menu pakan ternak' :
            os.system('cls')
            ubah_data()
        elif pilihan == '3' or pilihan == 'tambah daftar menu pakan ternak' :
            os.system('cls')
            tambah_data ()
        elif pilihan == '4' or pilihan == 'hapus daftar menu pakan ternak' :
            os.system('cls')
            hapus_data()
        elif pilihan == '5' or pilihan == 'kelola voucher' :
            os.system('cls')
            voucher()
        elif pilihan == '6' or pilihan == 'lihat rekap struk' :
            os.system('cls')
            rekap_struk()
        elif pilihan == '0' or pilihan == 'keluar' :
            tampilanawal()
        else :
            input('Pilihan invalid,enter untuk ulang')
            os.system('cls')
            menupenjual()

# ---------- PROGRAM UTAMA ----------

tampilanawal()