import csv
import os
import time
import random
import pwinput
from prettytable import PrettyTable

FIELD_USER = ["username", "password", "role", "saldo"]
FIELD_KONSOL = ["kode", "nama", "merk", "harga", "stok"]
FIELD_TRANSAKSI = ["id_transaksi", "username", "jenis", "kode", "nama", "durasi", "jumlah", "total", "waktu", "id_referensi", "jumlah_kembali"]
JENIS_TRANSAKSI = ("Sewa", "Top Up E-Money", "Pengembalian")

def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")

def tunggu():
    input("\nTekan Enter untuk melanjutkan...")

def waktu_sekarang():
    return time.strftime("%d-%m-%Y %H:%M:%S")

def format_rupiah(angka):
    return "Rp " + f"{int(angka):,}".replace(",", ".")

def instruksi_batal():
    print("ketik 0 untuk batal atau tekan Ctrl+C untuk kembali ke menu utama.")

def input_teks(pesan):
    teks = input(pesan).strip()

    if teks == "0":
        print("Proses dibatalkan.")
        return None

    while teks == "":
        print("Input tidak boleh kosong.")
        teks = input(pesan).strip()

        if teks == "0":
            print("Proses dibatalkan.")
            return None

    return teks

def input_angka(pesan):
    while True:
        teks = input(pesan).strip()

        if teks == "0":
            print("Proses dibatalkan.")
            return None

        try:
            return int(teks)
        except ValueError:
            print("Input tidak valid, masukkan angka.")

def input_konfirmasi(pesan):
    while True:
        jawaban = input(pesan).strip().lower()

        if jawaban == "0":
            print("Proses dibatalkan.")
            return None

        if jawaban == "y":
            return True
        elif jawaban == "n":
            return False
        else:
            print("Input tidak valid, masukkan y atau n.")

def input_password(pesan):
    while True:
        password = pwinput.pwinput(pesan).strip()

        if password == "0":
            print("Proses dibatalkan.")
            return None

        if len(password) < 4:
            print("Password minimal 4 karakter.")
        else:
            return password

#  FILE CSV 
def ambil_data_csv(nama_file):
    try:
        with open(nama_file, "r", newline="", encoding="utf-8") as file:
            return list(csv.DictReader(file))

    except FileNotFoundError:
        print("File", nama_file, "tidak ditemukan.")

    except PermissionError:
        print("File tidak dapat diakses.")

    return None

def simpan_data_csv(nama_file, data):
    try:
        with open(nama_file, "r", newline="", encoding="utf-8") as file:
            pembaca = csv.DictReader(file)
            kolom = pembaca.fieldnames

        daftar_kolom = {
            "user.csv": FIELD_USER,
            "DaftarKonsol.csv": FIELD_KONSOL,
            "Transaksi.csv": FIELD_TRANSAKSI
        }
        if os.path.basename(nama_file) in daftar_kolom:
            kolom = daftar_kolom[os.path.basename(nama_file)]

        if not kolom:
            print("Header kolom CSV tidak ditemukan.")
            return False

        with open(nama_file, "w", newline="", encoding="utf-8") as file:
            penulis = csv.DictWriter(file, fieldnames=kolom)
            penulis.writeheader()
            penulis.writerows(data)

        return True

    except FileNotFoundError:
        print("File", nama_file, "tidak ditemukan. Data tidak bisa disimpan.")
        return False

    except PermissionError:
        print("File tidak dapat diakses. Data tidak bisa disimpan.")
        return False

    except (TypeError, csv.Error, OSError):
        print("Data tidak bisa disimpan.")
        return False

def buat_id_transaksi():
    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        return None

    for percobaan in range(100):
        id_baru = "TRX" + str(random.randint(10000, 99999))

        if not any(
            data["id_transaksi"] == id_baru
            for data in transaksi
        ):
            return id_baru

    print("Gagal membuat ID transaksi.")
    return None


def catat_transaksi(
    id_transaksi, username, jenis, kode, nama,
    durasi, jumlah, total, waktu,
    id_referensi="", jumlah_kembali=0
):
    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        return False

    transaksi.append({
        "id_transaksi": id_transaksi,
        "username": username,
        "jenis": jenis,
        "kode": kode,
        "nama": nama,
        "durasi": str(durasi),
        "jumlah": str(jumlah),
        "total": str(total),
        "waktu": waktu,
        "id_referensi": id_referensi,
        "jumlah_kembali": str(jumlah_kembali)
    })

    return simpan_data_csv("Transaksi.csv", transaksi)


def catat_banyak_transaksi(data_baru):
    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        return False

    transaksi.extend(data_baru)
    return simpan_data_csv("Transaksi.csv", transaksi)


#  REGISTRASI DAN LOGIN 

def registrasi():
    bersihkan_layar()
    print("===== REGISTRASI AKUN =====")
    instruksi_batal()

    users = ambil_data_csv("user.csv")

    if users is None:
        tunggu()
        return

    while True:
        username = input_teks("Buat username: ")

        if username is None:
            return

        if len(username) < 4:
            print("Username minimal 4 karakter.")

        elif any(
            data["username"].lower() == username.lower()
            for data in users
        ):
            print("Username sudah digunakan.")

        else:
            break

    password = input_password("Buat password: ")

    if password is None:
        return

    users.append({
        "username": username,
        "password": password,
        "role": "user",
        "saldo": "0"
    })

    if simpan_data_csv("user.csv", users):
        print("Registrasi berhasil. Silakan login.")

    tunggu()


def login():
    bersihkan_layar()
    print("===== LOGIN =====")
    instruksi_batal()

    for percobaan in range(3):
        username = input_teks("Username: ")

        if username is None:
            return None

        password = pwinput.pwinput("Password: ").strip()

        if password == "0":
            print("Login dibatalkan.")
            return None

        if password == "":
            print("Password tidak boleh kosong.")
            continue

        users = ambil_data_csv("user.csv")

        if users is None:
            return None

        for data in users:
            if (
                data["username"] == username
                and data["password"] == password
            ):
                print("Login berhasil. Selamat datang,", username)
                tunggu()
                return data

        print("Username atau password salah.")
        print("Sisa percobaan:", 2 - percobaan)

    print("Kesempatan login habis.")
    tunggu()

    return None


#  DATA KONSOL 

def lihat_konsol():
    daftar = ambil_data_csv("DaftarKonsol.csv")

    if daftar is None:
        return

    if not daftar:
        print("Belum ada data konsol.")
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode", "Nama", "Merek", "Harga/Jam", "Stok"
    ]

    for data in daftar:
        tabel.add_row([
            data["kode"],
            data["nama"],
            data["merk"],
            format_rupiah(data["harga"]),
            data["stok"]
        ])

    print(tabel)


def tambah_konsol():
    bersihkan_layar()
    print("===== TAMBAH KONSOL =====")
    instruksi_batal()

    daftar = ambil_data_csv("DaftarKonsol.csv")

    if daftar is None:
        tunggu()
        return

    while True:
        kode = input_teks("Kode konsol: ")

        if kode is None:
            return

        kode = kode.upper()

        if any(data["kode"].upper() == kode for data in daftar):
            print("Kode sudah terdaftar.")
        else:
            break

    nama = input_teks("Nama konsol: ")

    if nama is None:
        return

    merk = input_teks("Merek konsol: ")

    if merk is None:
        return

    harga = input_angka("Harga sewa per jam (Rp): ")

    if harga is None:
        return

    if harga < 1:
        print("Harga harus lebih dari 0.")
        tunggu()
        return

    stok = input_angka("Stok konsol: ")

    if stok is None:
        return

    if stok < 0:
        print("Stok tidak boleh negatif.")
        tunggu()
        return

    daftar.append({
        "kode": kode,
        "nama": nama,
        "merk": merk,
        "harga": str(harga),
        "stok": str(stok)
    })

    konfirmasi = input_konfirmasi("Simpan data konsol? (y/n): ")

    if konfirmasi is None:
        return

    if konfirmasi:
        if simpan_data_csv("DaftarKonsol.csv", daftar):
            print("Konsol berhasil ditambahkan.")
    else:
        print("Penambahan dibatalkan.")

    tunggu()


def ubah_konsol():
    bersihkan_layar()
    print("===== UBAH DATA KONSOL =====")
    instruksi_batal()

    daftar = ambil_data_csv("DaftarKonsol.csv")

    if daftar is None:
        tunggu()
        return

    lihat_konsol()

    kode = input_teks("\nMasukkan kode konsol: ")

    if kode is None:
        return

    kode = kode.upper()

    item = next(
        (data for data in daftar if data["kode"].upper() == kode),
        None
    )

    if item is None:
        print("Kode konsol tidak ditemukan.")
        tunggu()
        return

    print("Tekan Enter jika tidak ingin mengubah data.")

    nama = input("Nama konsol baru : ").strip()

    if nama == "0":
        print("Perubahan dibatalkan.")
        return

    merk = input("Merek konsol baru : ").strip()

    if merk == "0":
        print("Perubahan dibatalkan.")
        return

    harga_baru = input("Harga konsol baru per jam : ").strip()

    if harga_baru == "0":
        print("Perubahan dibatalkan.")
        return

    stok_baru = input("Stok konsol baru : ").strip()

    if stok_baru == "0":
        print("Perubahan dibatalkan.")
        return

    if harga_baru:
        try:
            harga = int(harga_baru)

            if harga < 1:
                print("Harga harus lebih dari 0.")
                tunggu()
                return

            item["harga"] = str(harga)

        except ValueError:
            print("Input harga harus berupa angka.")
            tunggu()
            return
    else:
        print("Harga tidak diubah.")

    if stok_baru:
        try:
            stok = int(stok_baru)

            if stok < 0:
                print("Stok tidak boleh negatif.")
                tunggu()
                return

            item["stok"] = str(int(item["stok"]) + stok)

        except ValueError:
            print("Input stok harus berupa angka.")
            tunggu()
            return
    else:
        print("Stok tidak diubah.")

    if nama:
        item["nama"] = nama
    else:
        print("Nama tidak diubah.")

    if merk:
        item["merk"] = merk
    else:
        print("Merek tidak diubah.")

    konfirmasi = input_konfirmasi("Simpan perubahan? (y/n): ")

    if konfirmasi is None:
        return

    if konfirmasi:
        if simpan_data_csv("DaftarKonsol.csv", daftar):
            print("Data konsol berhasil diubah.")
    else:
        print("Perubahan dibatalkan.")

    tunggu()


def hapus_konsol():
    bersihkan_layar()
    print("===== HAPUS KONSOL =====")
    instruksi_batal()

    daftar = ambil_data_csv("DaftarKonsol.csv")

    if daftar is None:
        tunggu()
        return

    lihat_konsol()

    kode = input_teks("\nMasukkan kode konsol: ")

    if kode is None:
        return

    kode = kode.upper()

    item = next(
        (data for data in daftar if data["kode"].upper() == kode),
        None
    )

    if item is None:
        print("Kode konsol tidak ditemukan.")
        tunggu()
        return

    if int(item["stok"]) > 0:
        print("Stok harus 0 sebelum konsol dihapus.")
        tunggu()
        return

    konfirmasi = input_konfirmasi("Yakin menghapus konsol? (y/n): ")

    if konfirmasi is None:
        return

    if not konfirmasi:
        print("Penghapusan dibatalkan.")
        tunggu()
        return

    daftar = [
        data for data in daftar
        if data["kode"].upper() != kode
    ]

    if simpan_data_csv("DaftarKonsol.csv", daftar):
        print("Konsol berhasil dihapus.")

    tunggu()


#  TRANSAKSI ADMIN 

def lihat_transaksi_admin():
    bersihkan_layar()
    print("===== DAFTAR TRANSAKSI =====")

    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        tunggu()
        return

    if not transaksi:
        print("Belum ada transaksi.")
        tunggu()
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "ID", "Username", "Jenis", "Kode", "Nama",
        "Durasi", "Jumlah", "Total", "Waktu"
    ]

    for data in transaksi:
        tabel.add_row([
            data["id_transaksi"],
            data["username"],
            data["jenis"],
            data["kode"],
            data["nama"],
            data["durasi"],
            data["jumlah"],
            format_rupiah(data["total"]),
            data["waktu"]
        ])

    print(tabel)
    tunggu()


# LAPORAN RINGKAS 

def laporan_ringkas():
    bersihkan_layar()
    print("===== LAPORAN RINGKAS =====")

    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        tunggu()
        return

    total_pendapatan = 0
    daftar_transaksi = set()
    daftar_produk = {}

    for data in transaksi:
        if data["jenis"] == JENIS_TRANSAKSI[0]:
            try:
                total_pendapatan += int(data["total"])
                daftar_transaksi.add(data["id_transaksi"])

                kode = data["kode"]
                nama = data["nama"]
                jumlah = int(data["jumlah"])

                if kode not in daftar_produk:
                    daftar_produk[kode] = {
                        "nama": nama,
                        "jumlah": 0,
                        "kali_disewa": 0
                    }

                daftar_produk[kode]["jumlah"] += jumlah
                daftar_produk[kode]["kali_disewa"] += 1

            except (ValueError, KeyError):
                print("Ada data penyewaan yang tidak valid.")

    print()
    print("Total Pendapatan :", format_rupiah(total_pendapatan))
    print("Jumlah Transaksi :", len(daftar_transaksi))

    if daftar_produk:
        kode_terlaris = ""

        for kode in daftar_produk:
            if kode_terlaris == "":
                kode_terlaris = kode
            elif (
                daftar_produk[kode]["jumlah"]
                > daftar_produk[kode_terlaris]["jumlah"]
            ):
                kode_terlaris = kode

        produk_terlaris = daftar_produk[kode_terlaris]

        print("Produk Terlaris  :", produk_terlaris["nama"])
        print("Total Unit Disewa:", produk_terlaris["jumlah"], "unit")
        print("Frekuensi Disewa :", produk_terlaris["kali_disewa"], "kali")

    else:
        print("Produk Terlaris  : Belum ada penyewaan.")
        print("Total Unit Disewa: 0 unit")
        print("Frekuensi Disewa : 0 kali")

    tunggu()

#  MENU ADMIN 

def menu_admin(user):
    while True:
        try:
            bersihkan_layar()
            print("===== MENU ADMIN =====")
            print("1. Tambah Konsol")
            print("2. Lihat Konsol")
            print("3. Ubah Konsol")
            print("4. Hapus Konsol")
            print("5. Lihat Penyewaan dan Transaksi")
            print("6. Laporan Ringkas")
            print("7. Logout")

            pilihan = int(input("Pilih menu: "))

            if pilihan < 1 or pilihan > 7:
                print("Pilih menu 1 sampai 7.")
                tunggu()
                continue

            if pilihan == 1:
                tambah_konsol()
            elif pilihan == 2:
                bersihkan_layar()
                lihat_konsol()
                tunggu()
            elif pilihan == 3:
                ubah_konsol()
            elif pilihan == 4:
                hapus_konsol()
            elif pilihan == 5:
                lihat_transaksi_admin()
            elif pilihan == 6:
                laporan_ringkas()
            elif pilihan == 7:
                print("Logout berhasil.")
                tunggu()
                return

        except ValueError:
            print("Input tidak valid, masukkan angka.")
            tunggu()


#  TOP UP E-MONEY 

def top_up(user):
    bersihkan_layar()
    print("===== TOP UP E-MONEY =====")
    instruksi_batal()
    print("Minimal top up: Rp5.000")
    print("Maksimal top up: Rp2.000.000")

    while True:
        teks_nominal = input("Masukkan nominal top up: Rp ").strip()

        if teks_nominal == "0":
            print("Top up dibatalkan.")
            return

        try:
            nominal = int(teks_nominal)

            if 5000 <= nominal <= 2000000:
                break

            print("Nominal harus antara Rp5.000 sampai Rp2.000.000.")

        except ValueError:
            print("Input tidak valid, masukkan angka.")

        ulang = input_konfirmasi("Mau memasukkan nominal lagi? (y/n): ")

        if ulang is not True:
            print("Top up dibatalkan.")
            return

    users = ambil_data_csv("user.csv")

    if users is None:
        tunggu()
        return

    id_transaksi = buat_id_transaksi()

    if id_transaksi is None:
        tunggu()
        return

    akun = next(
        (data for data in users if data["username"] == user["username"]),
        None
    )

    if akun is None:
        print("Akun tidak ditemukan.")
        tunggu()
        return

    akun["saldo"] = str(int(akun["saldo"]) + nominal)

    if not catat_transaksi(
        id_transaksi,
        user["username"],
        "Top Up",
        "-",
        "Top Up E-Money",
        0,
        0,
        nominal,
        waktu_sekarang()
    ):
        print("Top up gagal dicatat.")
        tunggu()
        return

    if not simpan_data_csv("user.csv", users):
        transaksi = ambil_data_csv("Transaksi.csv")

        if transaksi is not None:
            transaksi = [
                data for data in transaksi
                if data["id_transaksi"] != id_transaksi
            ]
            simpan_data_csv("Transaksi.csv", transaksi)

        print("Saldo gagal disimpan.")
        tunggu()
        return

    user["saldo"] = akun["saldo"]

    print("Top up berhasil.")
    print("ID transaksi:", id_transaksi)
    print("Nominal:", format_rupiah(nominal))
    print("Saldo sekarang:", format_rupiah(user["saldo"]))

    tunggu()


#  PENYEWAAN KONSOL 

def sewa_konsol(user):
    bersihkan_layar()
    print("===== PENYEWAAN KONSOL =====")
    instruksi_batal()

    daftar = ambil_data_csv("DaftarKonsol.csv")

    if daftar is None:
        tunggu()
        return

    if not daftar:
        print("Belum ada konsol yang tersedia.")
        tunggu()
        return

    daftar_sewa = []

    while True:
        bersihkan_layar()
        print("===== DAFTAR KONSOL =====")
        lihat_konsol()

        kode = input_teks("\nMasukkan kode konsol yang ingin disewa: ")

        if kode is None:
            return

        kode = kode.upper()

        item = next(
            (data for data in daftar if data["kode"].upper() == kode),
            None
        )

        if item is None:
            print("Kode konsol tidak ditemukan.")
            tunggu()
            continue

        if int(item["stok"]) <= 0:
            print("Stok konsol sedang habis.")
            tunggu()
            continue

        durasi = input_angka("Durasi sewa (jam): ")

        if durasi is None:
            return

        if durasi < 1:
            print("Durasi sewa harus lebih dari 0 jam.")
            tunggu()
            continue

        jumlah = input_angka("Jumlah konsol yang ingin disewa: ")

        if jumlah is None:
            return

        if jumlah < 1:
            print("Jumlah konsol harus lebih dari 0.")
            tunggu()
            continue

        if jumlah > int(item["stok"]):
            print("Jumlah melebihi stok yang tersedia.")
            tunggu()
            continue

        total = int(item["harga"]) * durasi * jumlah

        daftar_sewa.append({
            "kode": item["kode"],
            "nama": item["nama"],
            "durasi": durasi,
            "jumlah": jumlah,
            "harga": int(item["harga"]),
            "total": total
        })

        tambah_lagi = input_konfirmasi(
            "Apakah ingin menambah konsol lain? (y/n): "
        )

        if tambah_lagi is None:
            return

        if not tambah_lagi:
            break

    total_bayar = sum(data["total"] for data in daftar_sewa)

    bersihkan_layar()
    print("===== RINGKASAN PENYEWAAN =====")

    tabel = PrettyTable()
    tabel.field_names = [
        "Kode", "Nama Konsol", "Harga/Jam",
        "Durasi", "Jumlah", "Subtotal"
    ]

    for data in daftar_sewa:
        tabel.add_row([
            data["kode"],
            data["nama"],
            format_rupiah(data["harga"]),
            str(data["durasi"]) + " jam",
            data["jumlah"],
            format_rupiah(data["total"])
        ])

    print(tabel)
    print("Total pembayaran:", format_rupiah(total_bayar))
    print("Saldo Anda:", format_rupiah(user["saldo"]))

    if int(user["saldo"]) < total_bayar:
        print("Saldo tidak mencukupi. Silakan lakukan top up.")
        tunggu()
        return

    konfirmasi = input_konfirmasi("Lanjutkan penyewaan? (y/n): ")

    if konfirmasi is None:
        return

    if not konfirmasi:
        print("Penyewaan dibatalkan.")
        tunggu()
        return

    users = ambil_data_csv("user.csv")
    daftar = ambil_data_csv("DaftarKonsol.csv")

    if users is None or daftar is None:
        tunggu()
        return

    akun = next(
        (data for data in users if data["username"] == user["username"]),
        None
    )

    if akun is None:
        print("Akun tidak ditemukan.")
        tunggu()
        return

    for sewa in daftar_sewa:
        item = next(
            (
                data for data in daftar
                if data["kode"].upper() == sewa["kode"].upper()
            ),
            None
        )

        if item is None or int(item["stok"]) < sewa["jumlah"]:
            print("Stok berubah atau tidak mencukupi. Penyewaan dibatalkan.")
            tunggu()
            return

    id_transaksi = buat_id_transaksi()

    if id_transaksi is None:
        tunggu()
        return

    akun["saldo"] = str(int(akun["saldo"]) - total_bayar)

    for sewa in daftar_sewa:
        item = next(
            data for data in daftar
            if data["kode"].upper() == sewa["kode"].upper()
        )
        item["stok"] = str(int(item["stok"]) - sewa["jumlah"])

    if not simpan_data_csv("DaftarKonsol.csv", daftar):
        tunggu()
        return

    if not simpan_data_csv("user.csv", users):
        for sewa in daftar_sewa:
            item = next(
                data for data in daftar
                if data["kode"].upper() == sewa["kode"].upper()
            )
            item["stok"] = str(int(item["stok"]) + sewa["jumlah"])

        simpan_data_csv("DaftarKonsol.csv", daftar)
        print("Saldo gagal disimpan.")
        tunggu()
        return

    data_transaksi = []

    for sewa in daftar_sewa:
        data_transaksi.append({
            "id_transaksi": id_transaksi,
            "username": user["username"],
            "jenis": "Sewa",
            "kode": sewa["kode"],
            "nama": sewa["nama"],
            "durasi": str(sewa["durasi"]),
            "jumlah": str(sewa["jumlah"]),
            "total": str(sewa["total"]),
            "waktu": waktu_sekarang(),
            "id_referensi": "",
            "jumlah_kembali": "0"
        })

    if not catat_banyak_transaksi(data_transaksi):
        print("Penyewaan gagal dicatat sepenuhnya.")
        tunggu()
        return

    user["saldo"] = akun["saldo"]

    print("\nPenyewaan berhasil!")

    tabel = PrettyTable()
    tabel.field_names = ["ID Transaksi", "Total Pembayaran", "Sisa Saldo"]
    tabel.add_row([
        id_transaksi,
        format_rupiah(total_bayar),
        format_rupiah(user["saldo"])
    ])
    print(tabel)

    tunggu()

# RIWAYAT TRANSAKSI USER 
def riwayat_transaksi(user):
    bersihkan_layar()
    print("===== RIWAYAT TRANSAKSI =====")

    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        tunggu()
        return

    riwayat = [
        data for data in transaksi
        if data["username"] == user["username"]
    ]

    if not riwayat:
        print("Belum ada riwayat transaksi.")
        tunggu()
        return

    tabel = PrettyTable()
    tabel.field_names = [
        "ID", "Jenis", "Kode", "Nama",
        "Durasi", "Jumlah", "Total", "Waktu"
    ]

    for data in riwayat:
        tabel.add_row([
            data["id_transaksi"],
            data["jenis"],
            data["kode"],
            data["nama"],
            data["durasi"],
            data["jumlah"],
            format_rupiah(data["total"]),
            data["waktu"]
        ])

    print(tabel)
    tunggu()


#  CETAK INVOICE 

def cetak_invoice(user):
    bersihkan_layar()
    print("===== CETAK INVOICE =====")
    instruksi_batal()

    transaksi = ambil_data_csv("Transaksi.csv")

    if transaksi is None:
        tunggu()
        return

    riwayat = [
        data for data in transaksi
        if data["username"] == user["username"]
    ]

    if not riwayat:
        print("Belum ada riwayat transaksi.")
        tunggu()
        return

    daftar_id = []
    for data in riwayat:
        if data["id_transaksi"] not in daftar_id:
            daftar_id.append(data["id_transaksi"])

    print("\nRiwayat Transaksi:")
    tabel = PrettyTable()
    tabel.field_names = ["No.", "ID Transaksi", "Jenis", "Waktu", "Total"]

    for nomor, id_transaksi in enumerate(daftar_id, start=1):
        rincian = [
            data for data in riwayat
            if data["id_transaksi"] == id_transaksi
        ]
        total_transaksi = sum(int(data["total"]) for data in rincian)
        tabel.add_row([
            nomor,
            id_transaksi,
            rincian[0]["jenis"],
            rincian[0]["waktu"],
            format_rupiah(total_transaksi)
        ])

    print(tabel)
    nomor_pilihan = input_angka("\nPilih nomor transaksi untuk mencetak invoice: ")

    if nomor_pilihan is None:
        return

    if nomor_pilihan < 1 or nomor_pilihan > len(daftar_id):
        print("Nomor transaksi tidak valid.")
        tunggu()
        return

    id_pilihan = daftar_id[nomor_pilihan - 1]
    rincian = [
        data for data in riwayat
        if data["id_transaksi"] == id_pilihan
    ]
    total_transaksi = sum(int(data["total"]) for data in rincian)

    bersihkan_layar()
    print("========================================")
    print("              RENT 4-BIT")
    print("          Main Seru, Sewa Mudah!")
    print("========================================")
    print("              INVOICE")
    print("ID Transaksi :", id_pilihan)
    print("Username     :", user["username"])
    print("Jenis        :", rincian[0]["jenis"])
    print("Waktu        :", rincian[0]["waktu"])
    print("----------------------------------------")

    for data in rincian:
        print("Kode Konsol  :", data["kode"])
        print("Nama         :", data["nama"])
        print("Durasi       :", data["durasi"], "jam")
        print("Jumlah       :", data["jumlah"])
        print("Subtotal     :", format_rupiah(data["total"]))
        print("----------------------------------------")

    print("Total Transaksi:", format_rupiah(total_transaksi))
    print("========================================")
    print("       Terima kasih telah bertransaksi!")
    print("========================================")

    tunggu()

#  PENGEMBALIAN KONSOL 

def pengembalian_konsol(user):
    while True:
        bersihkan_layar()
        print("===== PENGEMBALIAN KONSOL =====")
        instruksi_batal()

        transaksi = ambil_data_csv("Transaksi.csv")
        daftar = ambil_data_csv("DaftarKonsol.csv")

        if transaksi is None or daftar is None:
            tunggu()
            return

        penyewaan = [
            data for data in transaksi
            if (
                data["username"] == user["username"]
                and data["jenis"] == "Sewa"
                and int(data["jumlah"]) > int(data["jumlah_kembali"])
            )
        ]

        if not penyewaan:
            print("Tidak ada konsol yang perlu dikembalikan.")
            tunggu()
            return

        tabel = PrettyTable()
        tabel.field_names = [
            "No.", "Kode", "Nama",
            "Jumlah Sewa", "Sudah Kembali", "Belum Kembali"
        ]

        for nomor, data in enumerate(penyewaan, start=1):
            tabel.add_row([
                nomor,
                data["kode"],
                data["nama"],
                data["jumlah"],
                data["jumlah_kembali"],
                int(data["jumlah"]) - int(data["jumlah_kembali"])
            ])

        print(tabel)

        nomor_pilihan = input_angka("\nPilih nomor konsol yang dikembalikan: ")

        if nomor_pilihan is None:
            return

        if nomor_pilihan < 1 or nomor_pilihan > len(penyewaan):
            print("Nomor konsol tidak valid.")
            tunggu()
            continue

        data_sewa = penyewaan[nomor_pilihan - 1]
        kode = data_sewa["kode"]
        belum_kembali = int(data_sewa["jumlah"]) - int(data_sewa["jumlah_kembali"])

        jumlah_kembali = input_angka("Jumlah konsol yang dikembalikan: ")

        if jumlah_kembali is None:
            return

        if jumlah_kembali < 1 or jumlah_kembali > belum_kembali:
            print("Jumlah pengembalian tidak valid.")
            tunggu()
            continue

        item = next(
            (data for data in daftar if data["kode"].upper() == kode.upper()),
            None
        )

        if item is None:
            print("Data konsol tidak ditemukan.")
            tunggu()
            continue

        konfirmasi = input_konfirmasi("Konfirmasi pengembalian? (y/n): ")

        if konfirmasi is None:
            return

        if not konfirmasi:
            print("Pengembalian dibatalkan.")
            tunggu()
            continue

        jumlah_sebelumnya = int(data_sewa["jumlah_kembali"])
        stok_sebelumnya = int(item["stok"])

        data_sewa["jumlah_kembali"] = str(jumlah_sebelumnya + jumlah_kembali)
        item["stok"] = str(stok_sebelumnya + jumlah_kembali)

        if not simpan_data_csv("DaftarKonsol.csv", daftar):
            tunggu()
            return

        if not simpan_data_csv("Transaksi.csv", transaksi):
            item["stok"] = str(stok_sebelumnya)
            data_sewa["jumlah_kembali"] = str(jumlah_sebelumnya)
            simpan_data_csv("DaftarKonsol.csv", daftar)
            tunggu()
            return

        print("\nPengembalian berhasil dicatat!")
        print("Konsol:", data_sewa["nama"])
        print("Jumlah dikembalikan:", jumlah_kembali)

        ulang = input_konfirmasi(
            "\nApakah ingin mengembalikan konsol lagi? (y/n): "
        )

        if ulang is not True:
            print("Proses pengembalian selesai.")
            tunggu()
            return

#  MENU USER
def menu_user(user):
    while True:
        try:
            bersihkan_layar()
            print("===== MENU USER =====")
            print("Selamat datang,", user["username"])
            print("Saldo:", format_rupiah(user["saldo"]))
            print()
            print("1. Lihat Daftar Konsol")
            print("2. Top Up E-Money")
            print("3. Sewa Konsol")
            print("4. Riwayat Transaksi")
            print("5. Cetak Invoice")
            print("6. Pengembalian Konsol")
            print("7. Logout")

            pilihan = int(input("Pilih menu: "))

            if pilihan < 1 or pilihan > 7:
                print("Pilih menu 1 sampai 7.")
                tunggu()
                continue

            if pilihan == 1:
                bersihkan_layar()
                print("===== DAFTAR KONSOL =====")
                lihat_konsol()
                tunggu()

            elif pilihan == 2:
                top_up(user)

            elif pilihan == 3:
                sewa_konsol(user)

            elif pilihan == 4:
                riwayat_transaksi(user)

            elif pilihan == 5:
                cetak_invoice(user)

            elif pilihan == 6:
                pengembalian_konsol(user)

            elif pilihan == 7:
                print("Logout berhasil.")
                tunggu()
                return

        except ValueError:
            print("Input tidak valid, masukkan angka.")
            tunggu()

#  MENU UTAMA
def main():
    while True:
        try:
            bersihkan_layar()
            print("================================")
            print("          RENT 4-BIT")
            print("      Main Seru, Sewa Mudah!")
            print("================================")
            print("1. Registrasi")
            print("2. Login")
            print("3. Keluar")

            pilihan = input("Pilih menu: ").strip()

            if pilihan == "1":
                registrasi()

            elif pilihan == "2":
                user = login()

                if user is not None:
                    if user["role"].lower() == "admin":
                        menu_admin(user)
                    else:
                        menu_user(user)

            elif pilihan == "3":
                print("Terima kasih telah menggunakan RENT 4-BIT.")
                break

            else:
                print("Pilihan tidak valid. Pilih menu 1 sampai 3.")
                tunggu()

        except KeyboardInterrupt:
            print("\nKembali ke menu utama.")

if __name__ == "__main__":
    main()