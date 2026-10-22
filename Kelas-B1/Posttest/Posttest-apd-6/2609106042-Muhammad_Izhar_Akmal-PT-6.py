import os
from datetime import datetime
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
pengguna = {
    "AdminSistem": {"password": "admin120307", "role": "Administrator"},
    "izhar": {"password": "okedeh01", "role": "Petugas Pendaftaran"},
}
khusus_admin = {
    "1": {"nama": "Tambah data pengunjung", "tujuan": "tambah"},
    "2": {"nama": "Lihat / cari data pengunjung", "tujuan": "lihat"},
    "3": {"nama": "Ubah data pengunjung", "tujuan": "ubah"},
    "4": {"nama": "Hapus data pengunjung", "tujuan": "hapus"},
    "5": {"nama": "Cek data ganda", "tujuan": "ganda"},
    "6": {"nama": "Riwayat penghapusan", "tujuan": "riwayat"},
    "7": {"nama": "Kelola akun petugas", "tujuan": "kelola"},
    "8": {"nama": "Logout", "tujuan": "logout"},
}
khusus_guest = {
    "1": {"nama": "Tambah pengunjung", "tujuan": "tambah"},
    "2": {"nama": "Lihat/cari data pengunjung", "tujuan": "lihat"},
    "3": {"nama": "Tandai pengunjung keluar", "tujuan": "keluar"},
    "4": {"nama": "Logout", "tujuan": "logout"},
}
hari_per_bulan = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31,
}
nama_tiap_bulan = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember",
}
kategori_pengunjung = {
    "1": "Pihak yang Berperkara",
    "2": "Saksi",
    "3": "Kuasa Hukum (Advokat)",
    "4": "Keluarga Pihak yang Berperkara",
    "5": "Pengunjung Umum",
    "6": "Wartawan",
}
seluruh_pengunjung = {
    1: {
        "nama": "Muhammad Nur Fadilla",
        "tanggal": "13 Oktober 2026",
        "kategori": "Pihak yang Berperkara",
        "perkara": "Sengketa tanah No. 123/Pdt.G/2026",
        "jam_masuk": "09:15",
        "jam_keluar": "10:40",
    },
    2: {
        "nama": "Muhammad Al-Kahfi Hafidz Mufajar",
        "tanggal": "13 Oktober 2026",
        "kategori": "Saksi",
        "perkara": "Pidana pencurian No. 45/Pid.B/2026",
        "jam_masuk": "09:30",
        "jam_keluar": "-",
    },
    3: {
        "nama": "Muhammad Khairul Anaam",
        "tanggal": "12 Oktober 2026",
        "kategori": "Kuasa Hukum (Advokat)",
        "perkara": "Penganiayaan No. 88/Pid.B/2026",
        "jam_masuk": "13:00",
        "jam_keluar": "14:20",
    },
}
alasan_hapus = {
    "1": "Data ganda (double)",
    "2": "Pengunjung fiktif",
    "3": "Salah data",
}
riwayat_hapus = {}
dlm_lihat = {
    "1": "Semua data",
    "2": "Berdasarkan kategori",
    "3": "Berdasarkan tanggal berkunjung",
    "4": "Berdasarkan nama",
    "5": "Yang masih di dalam (belum keluar)",
    "6": "Yang sudah keluar",
}
kolom_admin = {
    "1": {"nama": "Nama pengunjung", "kunci": "nama"},
    "2": {"nama": "Tanggal berkunjung", "kunci": "tanggal"},
    "3": {"nama": "Kategori pengunjung", "kunci": "kategori"},
    "4": {"nama": "Duduk perkara", "kunci": "perkara"},
    "5": {"nama": "Jam masuk", "kunci": "jam_masuk"},
    "6": {"nama": "Jam keluar", "kunci": "jam_keluar"},
}
while True:
    clear_screen()
    print("=" * 42)
    print(" SISTEM PENDATAAN PENGUNJUNG PENGADILAN")
    print("=" * 42)
    print("1. Login dengan akun anda")
    print("2. Lakukan register akun baru")
    print("3. Keluar")
    option = input("Pilih menu: ").strip()
    if option == "1":
        clear_screen()
        print("")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()
        if username not in pengguna or pengguna[username]["password"] != password:
            print("Username atau password anda salah, silahkan coba login kembali.")
            input("Tekan Enter untuk kembali...")
            continue
        username_aktif = username
        role_aktif = pengguna[username]["role"]
        if role_aktif == "Administrator":
            menu_utama = khusus_admin
            daftar_kolom = kolom_admin
        else:
            menu_utama = khusus_guest
            daftar_kolom = {}
        while True:
            clear_screen()
            print(f"Anda login sebagai {role_aktif}")
            print("=" * 36)
            print("             MENU UTAMA")
            print("=" * 36)
            for nomor, isi_menu in menu_utama.items():
                print(f"{nomor}. {isi_menu['nama']}")
            pilih_menu = input("Pilih menu: ").strip()
            tujuan = ""
            if pilih_menu in menu_utama:
                tujuan = menu_utama[pilih_menu]["tujuan"]
            if tujuan == "logout":
                break
            if tujuan == "":
                print("Pilihan menu tidak valid!")
            elif tujuan == "tambah":
                clear_screen()
                print("=== TAMBAH DATA PENGUNJUNG ===")
                nama = input("Nama pengunjung: ").strip()
                print("")
                while len(nama) == 0:
                    print("Nama tidak boleh kosong!")
                    print("")
                    nama = input("Nama pengunjung: ").strip()
                    print("")
                while True:
                    print("Masukkan tanggal, bulan, dan tahun secara terpisah di bawah ini:")
                    tanggal = input("Masukkan tanggal berkunjung (hanya tanggal): ").strip()
                    bulan = input("Masukkan bulan berkunjung: ").strip()
                    tahun = input("Masukkan tahun berkunjung: ").strip()
                    if not tanggal.isdecimal() or not bulan.isdecimal() or not tahun.isdecimal():
                        print("Tanggal, bulan, dan tahun harus berupa angka")
                        continue
                    tanggal = int(tanggal)
                    bulan = int(bulan)
                    tahun = int(tahun)
                    if tahun < 2000 or tahun > 2100:
                        print("Masukkan tahun hanya antara 2000 - 2100")
                        continue
                    if bulan < 1 or bulan > 12:
                        print("Masukkan bulan hanya antara 1 - 12")
                        continue
                    mentok_hari = hari_per_bulan[bulan]
                    if bulan == 2 and (tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)):
                        mentok_hari = 29
                    if tanggal < 1 or tanggal > mentok_hari:
                        print(f"Tanggal tidak valid! (bulan {bulan} hanya sampai tanggal {mentok_hari})")
                        continue
                    break
                tanggal_berkunjung = f"{tanggal} {nama_tiap_bulan[bulan]} {tahun}"
                print("-" * 45)
                print(f"Tanggal berkunjung : {tanggal_berkunjung}")
                print("-" * 45)
                print(f"{nama} berkunjung sebagai:")
                for kode, nama_kat in kategori_pengunjung.items():
                    print(f"  {kode}. {nama_kat}")
                while True:
                    print("")
                    pilihan = input("Kategori pengunjung: ").strip()
                    if pilihan not in kategori_pengunjung:
                        print("Pilihan kategori tidak valid!")
                        continue
                    nama_kategori = kategori_pengunjung[pilihan]
                    break
                perkara = input("Duduk perkara (jenis/nomor perkara): ").strip()
                while len(perkara) == 0:
                    print("Duduk perkara tidak boleh kosong!")
                    perkara = input("Duduk perkara (jenis/nomor perkara): ").strip()
                while True:
                    jam_masuk = input("Jam masuk dengan format HH:MM: ").strip()
                    if len(jam_masuk) != 5 or jam_masuk[2] != ":" or not jam_masuk[0:2].isdecimal() or not jam_masuk[3:5].isdecimal():
                        print("Format jam harus HH:MM (contoh 09:30)!")
                        continue
                    if int(jam_masuk[0:2]) > 23 or int(jam_masuk[3:5]) > 59:
                        print("Jam tidak valid (00:00 - 23:59)!")
                        continue
                    break
                while True:
                    jam_keluar = input("Jam keluar (HH:MM, tekan Enter jika belum keluar): ").strip()
                    if len(jam_keluar) == 0:
                        jam_keluar = "-"
                        break
                    if len(jam_keluar) != 5 or jam_keluar[2] != ":" or not jam_keluar[0:2].isdecimal() or not jam_keluar[3:5].isdecimal():
                        print("Format jam harus HH:MM (contoh 14:30)!")
                        continue
                    if int(jam_keluar[0:2]) > 23 or int(jam_keluar[3:5]) > 59:
                        print("Jam tidak valid (00:00 - 23:59)!")
                        continue
                    if jam_keluar < jam_masuk:
                        print("Jam keluar tidak boleh lebih awal dari jam masuk!")
                        continue
                    break
                new_id = 1
                for id_pengunjung in seluruh_pengunjung:
                    if id_pengunjung >= new_id:
                        new_id = id_pengunjung + 1
                for catatan in riwayat_hapus.values():
                    if catatan["id_pengunjung"] >= new_id:
                        new_id = catatan["id_pengunjung"] + 1
                seluruh_pengunjung[new_id] = {
                    "nama": nama,
                    "tanggal": tanggal_berkunjung,
                    "kategori": nama_kategori,
                    "perkara": perkara,
                    "jam_masuk": jam_masuk,
                    "jam_keluar": jam_keluar,
                }
                print(f"\nData pengunjung berhasil ditambahkan dengan ID {new_id}.")
            elif tujuan == "lihat":
                clear_screen()
                print("=== LIHAT DATA PENGUNJUNG ===")
                for kode, nama_lihat in dlm_lihat.items():
                    print(f"{kode}. {nama_lihat}")
                pilihan = input("Pilih kategori data: ").strip()
                lihat_data = ""
                if pilihan in dlm_lihat:
                    lihat_data = pilihan
                if lihat_data == "":
                    print("Pilihan kategori data tidak valid!")
                else:
                    valid = True
                    kata_kunci = ""
                    if lihat_data == "2":
                        clear_screen()
                        print("\nKategori pengunjung:")
                        for kode, nama_kat in kategori_pengunjung.items():
                            print(f"  {kode}. {nama_kat}")
                        pil_kat = input("Pilih kategori: ").strip()
                        if pil_kat in kategori_pengunjung:
                            kata_kunci = kategori_pengunjung[pil_kat]
                        else:
                            print("Pilihan kategori tidak valid!")
                            valid = False
                    elif lihat_data == "3":
                        clear_screen()
                        print("\nMasukkan tanggal berkunjung yang dicari:")
                        tanggal = input("Masukkan tanggal: ").strip()
                        bulan = input("Masukkan bulan: ").strip()
                        tahun = input("Masukkan tahun: ").strip()
                        if not tanggal.isdecimal() or not bulan.isdecimal() or not tahun.isdecimal():
                            print("Tanggal, bulan, dan tahun harus berupa angka!")
                            valid = False
                        else:
                            tanggal = int(tanggal)
                            bulan = int(bulan)
                            tahun = int(tahun)
                            if tahun < 2000 or tahun > 2100:
                                print("Masukkan tahun hanya antara 2000 - 2100")
                                valid = False
                            elif bulan < 1 or bulan > 12:
                                print("Masukkan bulan hanya antara 1 - 12")
                                valid = False
                            else:
                                mentok_hari = hari_per_bulan[bulan]
                                if bulan == 2 and (tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)):
                                    mentok_hari = 29
                                if tanggal < 1 or tanggal > mentok_hari:
                                    print(f"Tanggal tidak valid! (bulan {bulan} hanya sampai tanggal {mentok_hari})")
                                    valid = False
                                else:
                                    kata_kunci = f"{tanggal} {nama_tiap_bulan[bulan]} {tahun}"
                    elif lihat_data == "4":
                        clear_screen()
                        kata_kunci = input("Masukkan nama (boleh sebagian): ").strip().lower()
                        if len(kata_kunci) == 0:
                            print("Nama tidak boleh kosong!")
                            valid = False
                    if valid:
                        hasilnya = {}
                        for id_pengunjung, data in seluruh_pengunjung.items():
                            cocok = False
                            if lihat_data == "1":
                                cocok = True
                            elif lihat_data == "2" and data["kategori"] == kata_kunci:
                                cocok = True
                            elif lihat_data == "3" and data["tanggal"] == kata_kunci:
                                cocok = True
                            elif lihat_data == "4" and kata_kunci in data["nama"].lower():
                                cocok = True
                            elif lihat_data == "5" and data["jam_keluar"] == "-":
                                cocok = True
                            elif lihat_data == "6" and data["jam_keluar"] != "-":
                                cocok = True
                            if cocok:
                                hasilnya[id_pengunjung] = data
                        print()
                        if len(hasilnya) == 0:
                            print("Tidak ada data yang sesuai kriteria.")
                        else:
                            clear_screen()
                            print("DATA PENGUNJUNG".center(131, " "))
                            print("-" * 131)
                            print(f"{'ID':<4}{'Nama':<28}{'Tanggal':<17}{'Kategori':<32}{'Duduk Perkara':<36}{'Masuk':<7}{'Keluar':<7}")
                            print("-" * 131)
                            for id_pengunjung, data in hasilnya.items():
                                print(f"{id_pengunjung:<4}{data['nama'][:26]:<28}{data['tanggal']:<17}{data['kategori']:<32}{data['perkara'][:34]:<36}{data['jam_masuk']:<7}{data['jam_keluar']:<7}")
                            print(f"\nTotal: {len(hasilnya)} Data")
            elif tujuan == "keluar":
                clear_screen()
                print("=== TANDAI PENGUNJUNG KELUAR ===")
                carikan_id = input("Masukkan ID pengunjung: ").strip()
                if not carikan_id.isdecimal():
                    print("ID harus berupa angka!")
                else:
                    id_cari = int(carikan_id)
                    if id_cari not in seluruh_pengunjung:
                        print("ID tidak ditemukan!")
                    elif seluruh_pengunjung[id_cari]["jam_keluar"] != "-":
                        print("Pengunjung ini sudah ditandai keluar.")
                    else:
                        data = seluruh_pengunjung[id_cari]
                        print(f"\nNama       : {data['nama']}")
                        print(f"Jam masuk  : {data['jam_masuk']}")
                        while True:
                            jam = input("Jam keluar (HH:MM, kosong = batal): ").strip()
                            if len(jam) == 0:
                                print("Dibatalkan.")
                                break
                            if len(jam) != 5 or jam[2] != ":" or not jam[0:2].isdecimal() or not jam[3:5].isdecimal():
                                print("Format jam harus HH:MM (contoh 14:30)!")
                                continue
                            if int(jam[0:2]) > 23 or int(jam[3:5]) > 59:
                                print("Jam tidak valid (00:00 - 23:59)!")
                                continue
                            if jam < data["jam_masuk"]:
                                print("Jam keluar tidak boleh lebih awal dari jam masuk!")
                                continue
                            data["jam_keluar"] = jam
                            print("Pengunjung berhasil ditandai keluar.")
                            break
            elif tujuan == "ubah":
                clear_screen()
                print("=== UBAH DATA PENGUNJUNG ===")
                if len(seluruh_pengunjung) == 0:
                    print("Belum ada data pengunjung.")
                else:
                    carikan_id = input("Masukkan ID pengunjung: ").strip()
                    if not carikan_id.isdecimal():
                        print("ID harus berupa angka!")
                    else:
                        id_ubah = int(carikan_id)
                        if id_ubah not in seluruh_pengunjung:
                            print("ID tidak ditemukan!")
                        else:
                            data = seluruh_pengunjung[id_ubah]
                            print(f"\nNama           : {data['nama']}")
                            print(f"Tanggal        : {data['tanggal']}")
                            print(f"Kategori       : {data['kategori']}")
                            print(f"Duduk perkara  : {data['perkara']}")
                            print(f"Jam masuk      : {data['jam_masuk']}")
                            print(f"Jam keluar     : {data['jam_keluar']}")
                            print("\nData yang ingin diubah:")
                            for kode, kolom in daftar_kolom.items():
                                print(f"  {kode}. {kolom['nama']}")
                            pilih_kolom = input("Pilih: ").strip()
                            if pilih_kolom not in daftar_kolom:
                                print("Pilihan tidak valid!")
                            else:
                                kunci = daftar_kolom[pilih_kolom]["kunci"]
                                nama_kolom = daftar_kolom[pilih_kolom]["nama"]
                                if kunci == "nama":
                                    nama_baru = input("Masukkan nama baru. (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
                                    if len(nama_baru) == 0:
                                        print("Perubahan nama dibatalkan.")
                                    else:
                                        data["nama"] = nama_baru
                                        print("\nNama pengunjung berhasil diubah.")
                                elif kunci == "tanggal":
                                    tanggal_baru = ""
                                    while True:
                                        print("\nMasukkan tanggal berkunjung baru (Jika tidak mengisi kolom, maka perubahan dibatalkan): ")
                                        new_date = input("Masukkan tanggal: ").strip()
                                        new_month = input("Masukkan bulan: ").strip()
                                        new_year = input("Masukkan tahun: ").strip()
                                        if new_date == "" and new_month == "" and new_year == "":
                                            print("Perubahan tanggal dibatalkan.")
                                            break
                                        if not new_date.isdecimal() or not new_month.isdecimal() or not new_year.isdecimal():
                                            print("Tanggal, bulan, dan tahun harus berupa angka")
                                            continue
                                        new_date = int(new_date)
                                        new_month = int(new_month)
                                        new_year = int(new_year)
                                        if new_year < 2000 or new_year > 2100:
                                            print("Masukkan tahun hanya antara 2000 - 2100")
                                            continue
                                        if new_month < 1 or new_month > 12:
                                            print("Masukkan bulan hanya antara 1 - 12")
                                            continue
                                        mentok_hari = hari_per_bulan[new_month]
                                        if new_month == 2 and (new_year % 400 == 0 or (new_year % 4 == 0 and new_year % 100 != 0)):
                                            mentok_hari = 29
                                        if new_date < 1 or new_date > mentok_hari:
                                            print(f"Tanggal tidak valid! (bulan {new_month} hanya sampai tanggal {mentok_hari})")
                                            continue
                                        tanggal_baru = f"{new_date} {nama_tiap_bulan[new_month]} {new_year}"
                                        break
                                    if tanggal_baru != "":
                                        data["tanggal"] = tanggal_baru
                                        print("\nTanggal berkunjung berhasil diubah.")
                                elif kunci == "kategori":
                                    print("Kategori pengunjung:")
                                    for kode, nama_kat in kategori_pengunjung.items():
                                        print(f"  {kode}. {nama_kat}")
                                    kategori_baru = ""
                                    while True:
                                        kode = input("Pilih kategori baru anda (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
                                        if len(kode) == 0:
                                            break
                                        if kode in kategori_pengunjung:
                                            kategori_baru = kategori_pengunjung[kode]
                                            break
                                        print("Pilihan kategori tidak valid!")
                                    if kategori_baru == "":
                                        print("Perubahan kategori dibatalkan.")
                                    else:
                                        data["kategori"] = kategori_baru
                                        print("\nKategori berhasil diubah.")
                                elif kunci == "perkara":
                                    perkara_baru = input("Duduk perkara baru (kosong = batal): ").strip()
                                    if len(perkara_baru) == 0:
                                        print("Perubahan perkara dibatalkan.")
                                    else:
                                        data["perkara"] = perkara_baru
                                        print("Duduk perkara berhasil diubah.")
                                else:
                                    jam_baru = ""
                                    while True:
                                        j = input(f"{nama_kolom} baru dengan format HH:MM (Jika anda mengosongkan perubahan ini, maka perubahan dibatalkan): ").strip()
                                        if len(j) == 0:
                                            break
                                        if kunci == "jam_keluar" and j == "-":
                                            jam_baru = "-"
                                            break
                                        if len(j) != 5 or j[2] != ":" or not j[0:2].isdecimal() or not j[3:5].isdecimal():
                                            print("Format jam harus HH:MM (contoh 09:30)!")
                                            continue
                                        if int(j[0:2]) > 23 or int(j[3:5]) > 59:
                                            print("Jam tidak valid (00:00 - 23:59)!")
                                            continue
                                        if kunci == "jam_masuk" and data["jam_keluar"] != "-" and j > data["jam_keluar"]:
                                            print("Jam masuk tidak boleh lebih lambat dari jam keluar!")
                                            continue
                                        if kunci == "jam_keluar" and j < data["jam_masuk"]:
                                            print("Jam keluar tidak boleh lebih awal dari jam masuk!")
                                            continue
                                        jam_baru = j
                                        break
                                    if jam_baru == "":
                                        print("Perubahan dibatalkan.")
                                    else:
                                        data[kunci] = jam_baru
                                        print(f"{nama_kolom} berhasil diubah.")
            elif tujuan == "hapus":
                clear_screen()
                print("=== HAPUS DATA PENGUNJUNG ===")
                if len(seluruh_pengunjung) == 0:
                    print("Belum ada data pengunjung.")
                else:
                    carikan_id = input("Masukkan ID pengunjung: ").strip()
                    if not carikan_id.isdecimal():
                        print("ID harus berupa angka!")
                    else:
                        id_hapus = int(carikan_id)
                        if id_hapus not in seluruh_pengunjung:
                            print("ID tidak ditemukan!")
                        else:
                            data = seluruh_pengunjung[id_hapus]
                            print(f"\nNama             : {data['nama']}")
                            print(f"Tanggal          : {data['tanggal']}")
                            print(f"Kategori         : {data['kategori']}")
                            print(f"Duduk perkara    : {data['perkara']}")
                            print(f"Jam masuk/keluar : {data['jam_masuk']} / {data['jam_keluar']}")
                            print("\nAlasan anda melakukan penghapusan:")
                            for kode, teks in alasan_hapus.items():
                                print(f"  {kode}. {teks}")
                            while True:
                                kode = input("Pilih alasan: ").strip()
                                if kode not in alasan_hapus:
                                    print("Pilihan alasan tidak valid!")
                                    continue
                                alasan = alasan_hapus[kode]
                                break
                            konfirmasi = input("\nApakah anda yakin ingin menghapus data ini? (Ya/Tidak): ").strip().lower()
                            while konfirmasi != "ya" and konfirmasi != "tidak":
                                konfirmasi = input("Masukkan hanya Ya atau Tidak: ").strip().lower()
                            if konfirmasi == "ya":
                                waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
                                nomor_riwayat = len(riwayat_hapus) + 1
                                riwayat_hapus[nomor_riwayat] = {
                                    "id_pengunjung": id_hapus,
                                    "nama": data["nama"],
                                    "tanggal": data["tanggal"],
                                    "alasan": alasan,
                                    "dihapus_oleh": username_aktif,
                                    "waktu": waktu,
                                }
                                del seluruh_pengunjung[id_hapus]
                                print("Data berhasil dihapus dan dicatat di riwayat penghapusan.")
                            else:
                                print("Penghapusan ini dibatalkan.")
            elif tujuan == "ganda":
                clear_screen()
                print("=== PEMERIKSAAN DATA GANDA ===")
                print("Data akan dianggap ganda jika nama, tanggal, dan kategori sama.\n")
                jumlah = 0
                daftar_id = list(seluruh_pengunjung.keys())
                for i in range(len(daftar_id)):
                    for j in range(i + 1, len(daftar_id)):
                        id_a = daftar_id[i]
                        id_b = daftar_id[j]
                        a = seluruh_pengunjung[id_a]
                        b = seluruh_pengunjung[id_b]
                        if a["nama"].lower() == b["nama"].lower() and a["tanggal"] == b["tanggal"] and a["kategori"] == b["kategori"]:
                            print(f"ID {id_a} dan ID {id_b}  ->  {a['nama']} | {a['tanggal']} | {a['kategori']}")
                            jumlah += 1
                if jumlah == 0:
                    print("Tidak ditemukan data ganda.")
                else:
                    print(f"\nDitemukan {jumlah} pasangan data ganda.")
                    print("Hapus salah satunya melalui menu Hapus data pengunjung.")
            elif tujuan == "riwayat":
                clear_screen()
                print("=== RIWAYAT PENGHAPUSAN DATA ===")
                if len(riwayat_hapus) == 0:
                    print("Belum ada data yang dihapus.")
                else:
                    print(f"{'ID':<4}{'Nama':<28}{'Tanggal':<17}{'Alasan':<24}{'Oleh':<14}{'Waktu hapus':<18}")
                    print("-" * 105)
                    for r in riwayat_hapus.values():
                        print(f"{r['id_pengunjung']:<4}{r['nama'][:26]:<28}{r['tanggal']:<17}{r['alasan']:<24}{r['dihapus_oleh']:<14}{r['waktu']:<18}")
                    print(f"\nTotal: {len(riwayat_hapus)} data dihapus")
            elif tujuan == "kelola":
                clear_screen()
                print("=== KELOLA AKUN ===")
                print(f"{'No':<4}{'Username':<20}{'Role':<20}")
                print("-" * 44)
                nomor = 1
                for nama_user, info in pengguna.items():
                    print(f"{nomor:<4}{nama_user:<20}{info['role']:<20}")
                    nomor += 1
                print("\n1. Hapus akun")
                print("2. Kembali")
                sub = input("Pilih: ").strip()
                while sub != "1" and sub != "2":
                    sub = input("Pilihan tidak valid, ulangi (1/2): ").strip()
                if sub == "1":
                    target = input("Masukkan username yang akan dihapus: ").strip()
                    if target not in pengguna:
                        print("Username tidak ditemukan!")
                    elif target == username_aktif:
                        print("Tidak dapat menghapus akun yang sedang dipakai!")
                    elif pengguna[target]["role"] == "Administrator":
                        print("Akun administrator tidak dapat dihapus!")
                    else:
                        konfirmasi = input(f"Yakin hapus akun {target}? (Ya/Tidak): ").strip().lower()
                        while konfirmasi != "ya" and konfirmasi != "tidak":
                            konfirmasi = input("Masukkan hanya Ya atau Tidak: ").strip().lower()
                        if konfirmasi == "ya":
                            del pengguna[target]
                            print("Akun berhasil dihapus.")
                        else:
                            print("Penghapusan dibatalkan.")
            input("\nTekan Enter untuk lanjut...")
    elif option == "2":
        clear_screen()
        print("=== REGISTRASI AKUN BARU ===")
        while True:
            username_baru = input("Masukkan username baru: ").strip()
            if len(username_baru) < 4:
                print("Username minimal 4 karakter!")
                continue
            if " " in username_baru:
                print("Username tidak boleh mengandung spasi!")
                continue
            sudah_ada = False
            for u in pengguna:
                if u.lower() == username_baru.lower():
                    sudah_ada = True
            if sudah_ada:
                print("Username sudah dipakai!")
                continue
            break
        while True:
            password_baru = input("Masukkan password baru (min. 6 karakter): ").strip()
            if len(password_baru) < 6:
                print("Password minimal 6 karakter!")
                continue
            ulang = input("Masukkan kembali password: ").strip()
            if ulang != password_baru:
                print("Konfirmasi password tidak sama!")
                continue
            break
        pengguna[username_baru] = {"password": password_baru, "role": "Petugas Pendaftaran"}
        print("\nRegister berhasil! Silakan login.")
        input("Tekan Enter untuk kembali...")
    elif option == "3":
        clear_screen()
        print("=" * 68)
        print("")
        print(" Sebelum pulang kerja, jangan lupa memeriksa kembali area kerja ♥♥♥")
        print("")
        print("JANGAN LUPA ISTIRAHAT YANG CUKUP ♥♥♥".center(68, " "))
        print("")
        print("=" * 68)
        break
    else:
        print("Pilihan menu tidak valid!")
        input("Tekan Enter untuk kembali...")
