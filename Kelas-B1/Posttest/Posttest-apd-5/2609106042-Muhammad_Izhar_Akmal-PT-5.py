import os
from datetime import datetime
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
pengguna = [
    ["AdminSistem", "admin120307", "Administrator"],
    ["izhar", "okedeh01", "Petugas Pendaftaran"],
]
khusus_admin = [
    ["1", "Tambah data pengunjung", "tambah"],
    ["2", "Lihat / cari data pengunjung", "lihat"],
    ["3", "Ubah data pengunjung", "ubah"],
    ["4", "Hapus data pengunjung", "hapus"],
    ["5", "Cek data ganda", "ganda"],
    ["6", "Riwayat penghapusan", "riwayat"],
    ["7", "Kelola akun petugas", "kelola"],
    ["8", "Logout", "logout"],
]
khusus_guest = [
    ["1", "Tambah pengunjung", "tambah"],
    ["2", "Lihat/cari data pengunjung", "lihat"],
    ["3", "Tandai pengunjung keluar", "keluar"],
    ["4", "Logout", "logout"],
]
hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
nama_tiap_bulan = ("Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                   "Agustus", "September", "Oktober", "November", "Desember")
kategori_pengunjung = [
    ["1", "Pihak yang Berperkara"],
    ["2", "Saksi"],
    ["3", "Kuasa Hukum (Advokat)"],
    ["4", "Keluarga Pihak yang Berperkara"],
    ["5", "Pengunjung Umum"],
    ["6", "Wartawan"],
]
seluruh_pengunjung = [
    [1, "Muhammad Nur Fadilla", "13 Oktober 2026", "Pihak yang Berperkara", "Sengketa tanah No. 123/Pdt.G/2026", "09:15", "10:40"],
    [2, "Muhammad Al-Kahfi Hafidz Mufajar", "13 Oktober 2026", "Saksi", "Pidana pencurian No. 45/Pid.B/2026", "09:30", "-"],
    [3, "Muhammad Khairul Anaam", "12 Oktober 2026", "Kuasa Hukum (Advokat)", "Penganiayaan No. 88/Pid.B/2026", "13:00", "14:20"],
]
alasan_hapus = [
    ["1", "Data ganda (double)"],
    ["2", "Pengunjung fiktif"],
    ["3", "Salah data"],
]
riwayat_hapus = []
dlm_lihat = [
    ["1", "Semua data"],
    ["2", "Berdasarkan kategori"],
    ["3", "Berdasarkan tanggal berkunjung"],
    ["4", "Berdasarkan nama"],
    ["5", "Yang masih di dalam (belum keluar)"],
    ["6", "Yang sudah keluar"],
]
kolom_admin = [
    ["1", "Nama pengunjung", 1],
    ["2", "Tanggal berkunjung", 2],
    ["3", "Kategori pengunjung", 3],
    ["4", "Duduk perkara", 4],
    ["5", "Jam masuk", 5],
    ["6", "Jam keluar", 6],
]
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
        jenis_akun = None
        for akun in pengguna:
            if akun[0] == username and akun[1] == password:
                jenis_akun = akun
                break
        if jenis_akun is None:
            print("Username atau password anda salah, silahkan coba login kembali.")
            input("Tekan Enter untuk kembali...")
            continue
        if jenis_akun[2] == "Administrator":
            menu_utama = khusus_admin
            daftar_kolom = kolom_admin
        else:
            menu_utama = khusus_guest
            daftar_kolom = []
        while True:
            clear_screen()
            print(f"Anda login sebagai {jenis_akun[2]}")
            print("=" * 36)
            print("             MENU UTAMA")
            print("=" * 36)
            for isi_menu in menu_utama:
                print(f"{isi_menu[0]}. {isi_menu[1]}")
            pilih_menu = input("Pilih menu: ").strip()
            tujuan = ""
            for isi_menu in menu_utama:
                if isi_menu[0] == pilih_menu:
                    tujuan = isi_menu[2]
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
                    mentok_hari = hari_per_bulan[bulan - 1]
                    if bulan == 2 and (tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)):
                        mentok_hari = 29
                    if tanggal < 1 or tanggal > mentok_hari:
                        print(f"Tanggal tidak valid! (bulan {bulan} hanya sampai tanggal {mentok_hari})")
                        continue
                    break
                tanggal_berkunjung = f"{tanggal} {nama_tiap_bulan[bulan - 1]} {tahun}"
                print("-" * 45)
                print(f"Tanggal berkunjung : {tanggal_berkunjung}")
                print("-" * 45)
                print(f"{nama} berkunjung sebagai:")
                for urutan in kategori_pengunjung:
                    print(f"  {urutan[0]}. {urutan[1]}")
                while True:
                    print("")
                    pilihan = input("Kategori pengunjung: ").strip()
                    nama_kategori = ""
                    for urutan in kategori_pengunjung:
                        if urutan[0] == pilihan:
                            nama_kategori = urutan[1]
                    if nama_kategori == "":
                        print("Pilihan kategori tidak valid!")
                        continue
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
                for urutan in seluruh_pengunjung:
                    if urutan[0] >= new_id:
                        new_id = urutan[0] + 1
                for urutan in riwayat_hapus:
                    if urutan[0] >= new_id:
                        new_id = urutan[0] + 1
                seluruh_pengunjung.append([new_id, nama, tanggal_berkunjung, nama_kategori, perkara, jam_masuk, jam_keluar])
                print(f"\nData pengunjung berhasil ditambahkan dengan ID {new_id}.")
            elif tujuan == "lihat":
                clear_screen()
                print("=== LIHAT DATA PENGUNJUNG ===")
                for urutan in dlm_lihat:
                    print(f"{urutan[0]}. {urutan[1]}")
                pilihan = input("Pilih kategori data: ").strip()
                lihat_data = ""
                for urutan in dlm_lihat:
                    if urutan[0] == pilihan:
                        lihat_data = urutan[0]
                if lihat_data == "":
                    print("Pilihan kategori data tidak valid!")
                else:
                    valid = True
                    kata_kunci = ""
                    if lihat_data == "2":
                        clear_screen()
                        print("\nKategori pengunjung:")
                        for urutan in kategori_pengunjung:
                            print(f"  {urutan[0]}. {urutan[1]}")
                        pil_kat = input("Pilih kategori: ").strip()
                        for urutan in kategori_pengunjung:
                            if urutan[0] == pil_kat:
                                kata_kunci = urutan[1]
                        if kata_kunci == "":
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
                                mentok_hari = hari_per_bulan[bulan - 1]
                                if bulan == 2 and (tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)):
                                    mentok_hari = 29
                                if tanggal < 1 or tanggal > mentok_hari:
                                    print(f"Tanggal tidak valid! (bulan {bulan} hanya sampai tanggal {mentok_hari})")
                                    valid = False
                                else:
                                    kata_kunci = f"{tanggal} {nama_tiap_bulan[bulan - 1]} {tahun}"
                    elif lihat_data == "4":
                        clear_screen()
                        kata_kunci = input("Masukkan nama (boleh sebagian): ").strip().lower()
                        if len(kata_kunci) == 0:
                            print("Nama tidak boleh kosong!")
                            valid = False
                    if valid:
                        hasilnya = []
                        for urutan in seluruh_pengunjung:
                            cocok = False
                            if lihat_data == "1":
                                cocok = True
                            elif lihat_data == "2" and urutan[3] == kata_kunci:
                                cocok = True
                            elif lihat_data == "3" and urutan[2] == kata_kunci:
                                cocok = True
                            elif lihat_data == "4" and kata_kunci in urutan[1].lower():
                                cocok = True
                            elif lihat_data == "5" and urutan[6] == "-":
                                cocok = True
                            elif lihat_data == "6" and urutan[6] != "-":
                                cocok = True
                            if cocok:
                                hasilnya.append(urutan)
                        print()
                        if len(hasilnya) == 0:
                            print("Tidak ada data yang sesuai kriteria.")
                        else:
                            clear_screen()
                            print("DATA PENGUNJUNG".center(131, " "))
                            print("-" * 131)
                            print(f"{'ID':<4}{'Nama':<28}{'Tanggal':<17}{'Kategori':<32}{'Duduk Perkara':<36}{'Masuk':<7}{'Keluar':<7}")
                            print("-" * 131)
                            for urutan in hasilnya:
                                print(f"{urutan[0]:<4}{urutan[1][:26]:<28}{urutan[2]:<17}{urutan[3]:<32}{urutan[4][:34]:<36}{urutan[5]:<7}{urutan[6]:<7}")
                            print(f"\nTotal: {len(hasilnya)} Data")
            elif tujuan == "keluar":
                clear_screen()
                print("=== TANDAI PENGUNJUNG KELUAR ===")
                carikan_id = input("Masukkan ID pengunjung: ").strip()
                if not carikan_id.isdecimal():
                    print("ID harus berupa angka!")
                else:
                    id_nya = -1
                    for i in range(len(seluruh_pengunjung)):
                        if seluruh_pengunjung[i][0] == int(carikan_id):
                            id_nya = i
                    if id_nya == -1:
                        print("ID tidak ditemukan!")
                    elif seluruh_pengunjung[id_nya][6] != "-":
                        print("Pengunjung ini sudah ditandai keluar.")
                    else:
                        data = seluruh_pengunjung[id_nya]
                        print(f"\nNama       : {data[1]}")
                        print(f"Jam masuk  : {data[5]}")
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
                            if jam < data[5]:
                                print("Jam keluar tidak boleh lebih awal dari jam masuk!")
                                continue
                            data[6] = jam
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
                        id_ubah = -1
                        for i in range(len(seluruh_pengunjung)):
                            if seluruh_pengunjung[i][0] == int(carikan_id):
                                id_ubah = i
                        if id_ubah == -1:
                            print("ID tidak ditemukan!")
                        else:
                            data = seluruh_pengunjung[id_ubah]
                            print(f"\nNama           : {data[1]}")
                            print(f"Tanggal        : {data[2]}")
                            print(f"Kategori       : {data[3]}")
                            print(f"Duduk perkara  : {data[4]}")
                            print(f"Jam masuk      : {data[5]}")
                            print(f"Jam keluar     : {data[6]}")
                            print("\nData yang ingin diubah:")
                            for urutan in daftar_kolom:
                                print(f"  {urutan[0]}. {urutan[1]}")
                            pilih_kolom = input("Pilih: ").strip()
                            kol = 0
                            for urutan in daftar_kolom:
                                if urutan[0] == pilih_kolom:
                                    kol = urutan[2]
                            if kol == 0:
                                print("Pilihan tidak valid!")
                            elif kol == 1:
                                nama_baru = input("Masukkan nama baru. (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
                                if len(nama_baru) == 0:
                                    print("Perubahan nama dibatalkan.")
                                else:
                                    data[1] = nama_baru
                                    print("\nNama pengunjung berhasil diubah.")
                            elif kol == 2:
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
                                    mentok_hari = hari_per_bulan[new_month - 1]
                                    if new_month == 2 and (new_year % 400 == 0 or (new_year % 4 == 0 and new_year % 100 != 0)):
                                        mentok_hari = 29
                                    if new_date < 1 or new_date > mentok_hari:
                                        print(f"Tanggal tidak valid! (bulan {new_month} hanya sampai tanggal {mentok_hari})")
                                        continue
                                    tanggal_baru = f"{new_date} {nama_tiap_bulan[new_month - 1]} {new_year}"
                                    break
                                if tanggal_baru != "":
                                    data[2] = tanggal_baru
                                    print("\nTanggal berkunjung berhasil diubah.")
                            elif kol == 3:
                                print("Kategori pengunjung:")
                                for urutan in kategori_pengunjung:
                                    print(f"  {urutan[0]}. {urutan[1]}")
                                kategori_baru = ""
                                while True:
                                    kode = input("Pilih kategori baru anda (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
                                    if len(kode) == 0:
                                        break
                                    for urutan in kategori_pengunjung:
                                        if urutan[0] == kode:
                                            kategori_baru = urutan[1]
                                    if kategori_baru == "":
                                        print("Pilihan kategori tidak valid!")
                                        continue
                                    break
                                if kategori_baru == "":
                                    print("Perubahan kategori dibatalkan.")
                                else:
                                    data[3] = kategori_baru
                                    print("\nKategori berhasil diubah.")
                            elif kol == 4:
                                perkara_baru = input("Duduk perkara baru (kosong = batal): ").strip()
                                if len(perkara_baru) == 0:
                                    print("Perubahan perkara dibatalkan.")
                                else:
                                    data[4] = perkara_baru
                                    print("Duduk perkara berhasil diubah.")
                            else:
                                if kol == 5:
                                    nama_kolom = "Jam masuk"
                                else:
                                    nama_kolom = "Jam keluar"
                                jam_baru = ""
                                while True:
                                    j = input(f"{nama_kolom} baru dengan format HH:MM (Jika anda mengosongkan perubahan ini, maka perubahan dibatalkan): ").strip()
                                    if len(j) == 0:
                                        break
                                    if kol == 6 and j == "-":
                                        jam_baru = "-"
                                        break
                                    if len(j) != 5 or j[2] != ":" or not j[0:2].isdecimal() or not j[3:5].isdecimal():
                                        print("Format jam harus HH:MM (contoh 09:30)!")
                                        continue
                                    if int(j[0:2]) > 23 or int(j[3:5]) > 59:
                                        print("Jam tidak valid (00:00 - 23:59)!")
                                        continue
                                    if kol == 5 and data[6] != "-" and j > data[6]:
                                        print("Jam masuk tidak boleh lebih lambat dari jam keluar!")
                                        continue
                                    if kol == 6 and j < data[5]:
                                        print("Jam keluar tidak boleh lebih awal dari jam masuk!")
                                        continue
                                    jam_baru = j
                                    break
                                if jam_baru == "":
                                    print("Perubahan dibatalkan.")
                                else:
                                    data[kol] = jam_baru
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
                        id_nya = -1
                        for i in range(len(seluruh_pengunjung)):
                            if seluruh_pengunjung[i][0] == int(carikan_id):
                                id_nya = i
                        if id_nya == -1:
                            print("ID tidak ditemukan!")
                        else:
                            data = seluruh_pengunjung[id_nya]
                            print(f"\nNama             : {data[1]}")
                            print(f"Tanggal          : {data[2]}")
                            print(f"Kategori         : {data[3]}")
                            print(f"Duduk perkara    : {data[4]}")
                            print(f"Jam masuk/keluar : {data[5]} / {data[6]}")
                            print("\nAlasan anda melakukan penghapusan:")
                            for a in alasan_hapus:
                                print(f"  {a[0]}. {a[1]}")
                            while True:
                                kode = input("Pilih alasan: ").strip()
                                alasan = ""
                                for a in alasan_hapus:
                                    if a[0] == kode:
                                        alasan = a[1]
                                if alasan == "":
                                    print("Pilihan alasan tidak valid!")
                                    continue
                                break
                            konfirmasi = input("\nApakah anda yakin ingin menghapus data ini? (Ya/Tidak): ").strip().lower()
                            while konfirmasi != "ya" and konfirmasi != "tidak":
                                konfirmasi = input("Masukkan hanya Ya atau Tidak: ").strip().lower()
                            if konfirmasi == "ya":
                                waktu = datetime.now().strftime("%d-%m-%Y %H:%M")
                                riwayat_hapus.append([data[0], data[1], data[2], alasan, jenis_akun[0], waktu])
                                seluruh_pengunjung.pop(id_nya)
                                print("Data berhasil dihapus dan dicatat di riwayat penghapusan.")
                            else:
                                print("Penghapusan ini dibatalkan.")
            elif tujuan == "ganda":
                clear_screen()
                print("=== PEMERIKSAAN DATA GANDA ===")
                print("Data akan dianggap ganda jika nama, tanggal, dan kategori sama.\n")
                jumlah = 0
                for i in range(len(seluruh_pengunjung)):
                    for j in range(i + 1, len(seluruh_pengunjung)):
                        a = seluruh_pengunjung[i]
                        b = seluruh_pengunjung[j]
                        if a[1].lower() == b[1].lower() and a[2] == b[2] and a[3] == b[3]:
                            print(f"ID {a[0]} dan ID {b[0]}  ->  {a[1]} | {a[2]} | {a[3]}")
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
                    for r in riwayat_hapus:
                        print(f"{r[0]:<4}{r[1][:26]:<28}{r[2]:<17}{r[3]:<24}{r[4]:<14}{r[5]:<18}")
                    print(f"\nTotal: {len(riwayat_hapus)} data dihapus")
            elif tujuan == "kelola":
                clear_screen()
                print("=== KELOLA AKUN ===")
                print(f"{'No':<4}{'Username':<20}{'Role':<20}")
                print("-" * 44)
                for i in range(len(pengguna)):
                    print(f"{i + 1:<4}{pengguna[i][0]:<20}{pengguna[i][2]:<20}")
                print("\n1. Hapus akun")
                print("2. Kembali")
                sub = input("Pilih: ").strip()
                while sub != "1" and sub != "2":
                    sub = input("Pilihan tidak valid, ulangi (1/2): ").strip()
                if sub == "1":
                    target = input("Masukkan username yang akan dihapus: ").strip()
                    id_nya = -1
                    for i in range(len(pengguna)):
                        if pengguna[i][0] == target:
                            id_nya = i
                    if id_nya == -1:
                        print("Username tidak ditemukan!")
                    elif pengguna[id_nya][0] == jenis_akun[0]:
                        print("Tidak dapat menghapus akun yang sedang dipakai!")
                    elif pengguna[id_nya][2] == "Administrator":
                        print("Akun administrator tidak dapat dihapus!")
                    else:
                        konfirmasi = input(f"Yakin hapus akun {target}? (Ya/Tidak): ").strip().lower()
                        while konfirmasi != "ya" and konfirmasi != "tidak":
                            konfirmasi = input("Masukkan hanya Ya atau Tidak: ").strip().lower()
                        if konfirmasi == "ya":
                            pengguna.pop(id_nya)
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
                if u[0].lower() == username_baru.lower():
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
        pengguna.append([username_baru, password_baru, "Petugas Pendaftaran"])
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