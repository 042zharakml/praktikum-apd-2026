import os
from datetime import datetime
pengguna = {
    "AdminSistem": {"password": "admin120307", "role": "Administrator"},
    "izhar": {"password": "okedeh01", "role": "Petugas Pendaftaran"},
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
riwayat_hapus = {}
username_aktif = ""
role_aktif = ""
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
    "6": "Wartawan  ",
}
alasan_hapus = {
    "1": "Data ganda (double)",
    "2": "Pengunjung fiktif",
    "3": "Salah data",
}
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
class AksesDitolakError(Exception):
    pass
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
def judul_halaman(judul):
    clear_screen()
    print(f"=== {judul} ===")
def tampilkan_detail(data):
    print(f"\nNama           : {data['nama']}")
    print(f"Tanggal        : {data['tanggal']}")
    print(f"Kategori       : {data['kategori']}")
    print(f"Duduk perkara  : {data['perkara']}")
    print(f"Jam masuk      : {data['jam_masuk']}")
    print(f"Jam keluar     : {data['jam_keluar']}")
def tampilkan_tabel(hasilnya):
    print("DATA PENGUNJUNG".center(131, " "))
    print("-" * 131)
    print(f"{'ID':<4}{'Nama':<28}{'Tanggal':<17}{'Kategori':<32}{'Duduk Perkara':<36}{'Masuk':<7}{'Keluar':<7}")
    print("-" * 131)
    for id_pengunjung, data in hasilnya.items():
        print(f"{id_pengunjung:<4}{data['nama'][:26]:<28}{data['tanggal']:<17}{data['kategori']:<32}{data['perkara'][:34]:<36}{data['jam_masuk']:<7}{data['jam_keluar']:<7}")
    print(f"\nTotal: {len(hasilnya)} Data")
def tampilkan_penutup():
    clear_screen()
    print("=" * 68)
    print("")
    print(" Sebelum pulang kerja, jangan lupa memeriksa kembali area kerja ♥♥♥")
    print("")
    print("JANGAN LUPA ISTIRAHAT YANG CUKUP ♥♥♥".center(68, " "))
    print("")
    print("=" * 68)
def proses_logout():
    global username_aktif, role_aktif
    username_aktif = ""
    role_aktif = ""
def wajib_admin():
    if role_aktif != "Administrator":
        raise AksesDitolakError("Akses ditolak! Menu ini hanya untuk Administrator.")
def buat_id_baru():
    id_baru = 1
    for id_pengunjung in seluruh_pengunjung:
        if id_pengunjung >= id_baru:
            id_baru = id_pengunjung + 1
    for catatan in riwayat_hapus.values():
        if catatan["id_pengunjung"] >= id_baru:
            id_baru = catatan["id_pengunjung"] + 1
    return id_baru
def ambil_waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M")
def proses_login():
    global username_aktif, role_aktif
    clear_screen()
    print("")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()
    try:
        akun = pengguna[username]
        if akun["password"] != password:
            raise ValueError("Password salah")
    except (KeyError, ValueError):
        print("Username atau password anda salah, silahkan coba login kembali.")
        return False
    username_aktif = username
    role_aktif = akun["role"]
    return True
def ke_angka(teks, nama="Input"):
    try:
        return int(teks)
    except ValueError:
        raise ValueError(f"{nama} harus berupa angka!") from None
def tahun_kabisat(tahun):
    return tahun % 400 == 0 or (tahun % 4 == 0 and tahun % 100 != 0)
def jumlah_hari(bulan, tahun):
    hari = hari_per_bulan[bulan]
    if bulan == 2 and tahun_kabisat(tahun):
        hari = 29
    return hari
def validasi_tanggal(tanggal, bulan, tahun):
    if tahun < 2000 or tahun > 2100:
        raise ValueError("Masukkan tahun hanya antara 2000 - 2100")
    if bulan < 1 or bulan > 12:
        raise ValueError("Masukkan bulan hanya antara 1 - 12")
    mentok_hari = jumlah_hari(bulan, tahun)
    if tanggal < 1 or tanggal > mentok_hari:
        raise ValueError(f"Tanggal tidak valid! (bulan {bulan} hanya sampai tanggal {mentok_hari})")
    return f"{tanggal} {nama_tiap_bulan[bulan]} {tahun}"
def validasi_jam(jam):
    if len(jam) != 5 or jam[2] != ":" or not jam[0:2].isdecimal() or not jam[3:5].isdecimal():
        raise ValueError("Format jam harus HH:MM (contoh 09:30)!")
    if int(jam[0:2]) > 23 or int(jam[3:5]) > 59:
        raise ValueError("Jam tidak valid (00:00 - 23:59)!")
    return jam
def cari_pengunjung(teks_id):
    id_angka = ke_angka(teks_id.strip(), "ID")
    return id_angka, seluruh_pengunjung[id_angka]
def username_sudah_ada(nama_user):
    for u in pengguna:
        if u.lower() == nama_user.lower():
            return True
    return False
def cocok_filter(pilihan, data, kata_kunci):
    if pilihan == "1":
        return True
    if pilihan == "2":
        return data["kategori"] == kata_kunci
    if pilihan == "3":
        return data["tanggal"] == kata_kunci
    if pilihan == "4":
        return kata_kunci in data["nama"].lower()
    if pilihan == "5":
        return data["jam_keluar"] == "-"
    if pilihan == "6":
        return data["jam_keluar"] != "-"
    return False
def minta_input_wajib(pesan, label):
    teks = input(pesan).strip()
    if len(teks) == 0:
        print(f"{label} tidak boleh kosong!")
        return minta_input_wajib(pesan, label)
    return teks
def minta_pilihan(pesan, daftar_valid, pesan_salah, boleh_kosong=False):
    pilihan = input(pesan).strip()
    if boleh_kosong and pilihan == "":
        return ""
    if pilihan in daftar_valid:
        return pilihan
    print(pesan_salah)
    return minta_pilihan(pesan, daftar_valid, pesan_salah, boleh_kosong)
def minta_konfirmasi(pesan):
    jawaban = input(pesan).strip().lower()
    if jawaban == "ya":
        return True
    if jawaban == "tidak":
        return False
    return minta_konfirmasi("Masukkan hanya Ya atau Tidak: ")
def input_tanggal(boleh_batal=False):
    while True:
        if boleh_batal:
            print("\nMasukkan tanggal berkunjung (kosongkan semua kolom untuk membatalkan):")
        else:
            print("Masukkan tanggal, bulan, dan tahun secara terpisah di bawah ini:")
        teks_tanggal = input("Masukkan tanggal: ").strip()
        teks_bulan = input("Masukkan bulan: ").strip()
        teks_tahun = input("Masukkan tahun: ").strip()
        if boleh_batal and teks_tanggal == "" and teks_bulan == "" and teks_tahun == "":
            return None
        try:
            tanggal = ke_angka(teks_tanggal, "Tanggal")
            bulan = ke_angka(teks_bulan, "Bulan")
            tahun = ke_angka(teks_tahun, "Tahun")
            hasil = validasi_tanggal(tanggal, bulan, tahun)
        except ValueError as e:
            print(e)
        else:
            return hasil
def input_jam(pesan, boleh_kosong=False, awal=None, akhir=None, boleh_strip=False):
    """
    Input jam HH:MM sampai valid.
    - boleh_kosong : Enter kosong diterima, return ""
    - awal         : jam tidak boleh lebih awal dari 'awal' (jam masuk)
    - akhir        : jam tidak boleh lebih lambat dari 'akhir' (jam keluar)
    - boleh_strip  : tanda "-" diterima (belum keluar)
    """
    while True:
        jam = input(pesan).strip()
        if jam == "" and boleh_kosong:
            return ""
        if jam == "-" and boleh_strip:
            return "-"
        try:
            validasi_jam(jam)
            if awal is not None and jam < awal:
                raise ValueError("Jam keluar tidak boleh lebih awal dari jam masuk!")
            if akhir is not None and akhir != "-" and jam > akhir:
                raise ValueError("Jam masuk tidak boleh lebih lambat dari jam keluar!")
        except ValueError as e:
            print(e)
        else:
            return jam
def menu_tambah():
    judul_halaman("TAMBAH DATA PENGUNJUNG")
    nama = minta_input_wajib("Nama pengunjung: ", "Nama")
    print("")
    tanggal_berkunjung = input_tanggal()
    print("-" * 45)
    print(f"Tanggal berkunjung : {tanggal_berkunjung}")
    print("-" * 45)
    print(f"{nama} berkunjung sebagai:")
    for kode, nama_kat in kategori_pengunjung.items():
        print(f"  {kode}. {nama_kat}")
    print("")
    kode = minta_pilihan("Kategori pengunjung: ", kategori_pengunjung, "Pilihan kategori tidak valid!")
    nama_kategori = kategori_pengunjung[kode]
    perkara = minta_input_wajib("Duduk perkara (jenis/nomor perkara): ", "Duduk perkara")
    jam_masuk = input_jam("Jam masuk dengan format HH:MM: ")
    jam_keluar = input_jam("Jam keluar (HH:MM, tekan Enter jika belum keluar): ",
                           boleh_kosong=True, awal=jam_masuk)
    if jam_keluar == "":
        jam_keluar = "-"
    new_id = buat_id_baru()
    seluruh_pengunjung[new_id] = {
        "nama": nama,
        "tanggal": tanggal_berkunjung,
        "kategori": nama_kategori,
        "perkara": perkara,
        "jam_masuk": jam_masuk,
        "jam_keluar": jam_keluar,
    }
    print(f"\nData pengunjung berhasil ditambahkan dengan ID {new_id}.")
def menu_lihat():
    judul_halaman("LIHAT DATA PENGUNJUNG")
    for kode, nama_lihat in dlm_lihat.items():
        print(f"{kode}. {nama_lihat}")
    pilihan = input("Pilih kategori data: ").strip()
    if pilihan not in dlm_lihat:
        print("Pilihan kategori data tidak valid!")
        return
    kata_kunci = ""
    if pilihan == "2":
        clear_screen()
        print("\nKategori pengunjung:")
        for kode, nama_kat in kategori_pengunjung.items():
            print(f"  {kode}. {nama_kat}")
        pil_kat = input("Pilih kategori: ").strip()
        if pil_kat not in kategori_pengunjung:
            print("Pilihan kategori tidak valid!")
            return
        kata_kunci = kategori_pengunjung[pil_kat]
    elif pilihan == "3":
        clear_screen()
        kata_kunci = input_tanggal(boleh_batal=True)
        if kata_kunci is None:
            print("Pencarian dibatalkan.")
            return
    elif pilihan == "4":
        clear_screen()
        kata_kunci = input("Masukkan nama (boleh sebagian): ").strip().lower()
        if len(kata_kunci) == 0:
            print("Nama tidak boleh kosong!")
            return
    hasilnya = {}
    for id_pengunjung, data in seluruh_pengunjung.items():
        if cocok_filter(pilihan, data, kata_kunci):
            hasilnya[id_pengunjung] = data
    print()
    if len(hasilnya) == 0:
        print("Tidak ada data yang sesuai kriteria.")
    else:
        clear_screen()
        tampilkan_tabel(hasilnya)
def menu_keluar():
    judul_halaman("TANDAI PENGUNJUNG KELUAR")
    try:
        id_cari, data = cari_pengunjung(input("Masukkan ID pengunjung: "))
    except ValueError as e:
        print(e)
        return
    except KeyError:
        print("ID tidak ditemukan!")
        return
    if data["jam_keluar"] != "-":
        print("Pengunjung ini sudah ditandai keluar.")
        return
    print(f"\nNama       : {data['nama']}")
    print(f"Jam masuk  : {data['jam_masuk']}")
    jam = input_jam("Jam keluar (HH:MM, kosong = batal): ", boleh_kosong=True, awal=data["jam_masuk"])
    if jam == "":
        print("Dibatalkan.")
    else:
        data["jam_keluar"] = jam
        print("Pengunjung berhasil ditandai keluar.")
def menu_ubah():
    wajib_admin()
    judul_halaman("UBAH DATA PENGUNJUNG")
    if len(seluruh_pengunjung) == 0:
        print("Belum ada data pengunjung.")
        return
    try:
        id_ubah, data = cari_pengunjung(input("Masukkan ID pengunjung: "))
    except ValueError as e:
        print(e)
        return
    except KeyError:
        print("ID tidak ditemukan!")
        return
    tampilkan_detail(data)
    print("\nData yang ingin diubah:")
    for kode, kolom in kolom_admin.items():
        print(f"  {kode}. {kolom['nama']}")
    pilih_kolom = input("Pilih: ").strip()
    if pilih_kolom not in kolom_admin:
        print("Pilihan tidak valid!")
        return
    kunci = kolom_admin[pilih_kolom]["kunci"]
    nama_kolom = kolom_admin[pilih_kolom]["nama"]
    if kunci == "nama":
        nama_baru = input("Masukkan nama baru. (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
        if len(nama_baru) == 0:
            print("Perubahan nama dibatalkan.")
        else:
            data["nama"] = nama_baru
            print("\nNama pengunjung berhasil diubah.")
    elif kunci == "tanggal":
        tanggal_baru = input_tanggal(boleh_batal=True)
        if tanggal_baru is None:
            print("Perubahan tanggal dibatalkan.")
        else:
            data["tanggal"] = tanggal_baru
            print("\nTanggal berkunjung berhasil diubah.")
    elif kunci == "kategori":
        print("Kategori pengunjung:")
        for kode, nama_kat in kategori_pengunjung.items():
            print(f"  {kode}. {nama_kat}")
        kode = minta_pilihan("Pilih kategori baru anda (Jika bagian ini kosong, perubahan akan dibatalkan): ",
                             kategori_pengunjung, "Pilihan kategori tidak valid!", boleh_kosong=True)
        if kode == "":
            print("Perubahan kategori dibatalkan.")
        else:
            data["kategori"] = kategori_pengunjung[kode]
            print("\nKategori berhasil diubah.")
    elif kunci == "perkara":
        perkara_baru = input("Duduk perkara baru (kosong = batal): ").strip()
        if len(perkara_baru) == 0:
            print("Perubahan perkara dibatalkan.")
        else:
            data["perkara"] = perkara_baru
            print("Duduk perkara berhasil diubah.")
    else:
        pesan = f"{nama_kolom} baru dengan format HH:MM (Jika anda mengosongkan perubahan ini, maka perubahan dibatalkan): "
        if kunci == "jam_masuk":
            jam_baru = input_jam(pesan, boleh_kosong=True, akhir=data["jam_keluar"])
        else:
            jam_baru = input_jam(pesan, boleh_kosong=True, awal=data["jam_masuk"], boleh_strip=True)
        if jam_baru == "":
            print("Perubahan dibatalkan.")
        else:
            data[kunci] = jam_baru
            print(f"{nama_kolom} berhasil diubah.")
def menu_hapus():
    wajib_admin()
    judul_halaman("HAPUS DATA PENGUNJUNG")
    if len(seluruh_pengunjung) == 0:
        print("Belum ada data pengunjung.")
        return
    try:
        id_hapus, data = cari_pengunjung(input("Masukkan ID pengunjung: "))
    except ValueError as e:
        print(e)
        return
    except KeyError:
        print("ID tidak ditemukan!")
        return
    tampilkan_detail(data)
    print("\nAlasan anda melakukan penghapusan:")
    for kode, teks in alasan_hapus.items():
        print(f"  {kode}. {teks}")
    kode = minta_pilihan("Pilih alasan: ", alasan_hapus, "Pilihan alasan tidak valid!")
    alasan = alasan_hapus[kode]
    if minta_konfirmasi("\nApakah anda yakin ingin menghapus data ini? (Ya/Tidak): "):
        nomor_riwayat = len(riwayat_hapus) + 1
        riwayat_hapus[nomor_riwayat] = {
            "id_pengunjung": id_hapus,
            "nama": data["nama"],
            "tanggal": data["tanggal"],
            "alasan": alasan,
            "dihapus_oleh": username_aktif,
            "waktu": ambil_waktu_sekarang(),
        }
        del seluruh_pengunjung[id_hapus]
        print("Data berhasil dihapus dan dicatat di riwayat penghapusan.")
    else:
        print("Penghapusan ini dibatalkan.")
def menu_ganda():
    wajib_admin()
    judul_halaman("PEMERIKSAAN DATA GANDA")
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
def menu_riwayat():
    wajib_admin()
    judul_halaman("RIWAYAT PENGHAPUSAN DATA")
    if len(riwayat_hapus) == 0:
        print("Belum ada data yang dihapus.")
        return
    print(f"{'ID':<4}{'Nama':<28}{'Tanggal':<17}{'Alasan':<24}{'Oleh':<14}{'Waktu hapus':<18}")
    print("-" * 105)
    for r in riwayat_hapus.values():
        print(f"{r['id_pengunjung']:<4}{r['nama'][:26]:<28}{r['tanggal']:<17}{r['alasan']:<24}{r['dihapus_oleh']:<14}{r['waktu']:<18}")
    print(f"\nTotal: {len(riwayat_hapus)} data dihapus")
def menu_kelola():
    wajib_admin()
    judul_halaman("KELOLA AKUN")
    print(f"{'No':<4}{'Username':<20}{'Role':<20}")
    print("-" * 44)
    nomor = 1
    for nama_user, info in pengguna.items():
        print(f"{nomor:<4}{nama_user:<20}{info['role']:<20}")
        nomor += 1
    print("\n1. Hapus akun")
    print("2. Kembali")
    sub = minta_pilihan("Pilih: ", ("1", "2"), "Pilihan tidak valid, ulangi (1/2)!")
    if sub == "2":
        return
    target = input("Masukkan username yang akan dihapus: ").strip()
    try:
        role_target = pengguna[target]["role"]
    except KeyError:
        print("Username tidak ditemukan!")
        return
    if target == username_aktif:
        print("Tidak dapat menghapus akun yang sedang dipakai!")
    elif role_target == "Administrator":
        print("Akun administrator tidak dapat dihapus!")
    elif minta_konfirmasi(f"Yakin hapus akun {target}? (Ya/Tidak): "):
        del pengguna[target]
        print("Akun berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
def proses_register():
    judul_halaman("REGISTRASI AKUN BARU")
    while True:
        username_baru = input("Masukkan username baru: ").strip()
        try:
            if len(username_baru) < 4:
                raise ValueError("Username minimal 4 karakter!")
            if " " in username_baru:
                raise ValueError("Username tidak boleh mengandung spasi!")
            if username_sudah_ada(username_baru):
                raise ValueError("Username sudah dipakai!")
        except ValueError as e:
            print(e)
        else:
            break
    while True:
        password_baru = input("Masukkan password baru (min. 6 karakter): ").strip()
        try:
            if len(password_baru) < 6:
                raise ValueError("Password minimal 6 karakter!")
            ulang = input("Masukkan kembali password: ").strip()
            if ulang != password_baru:
                raise ValueError("Konfirmasi password tidak sama!")
        except ValueError as e:
            print(e)
        else:
            break
    pengguna[username_baru] = {"password": password_baru, "role": "Petugas Pendaftaran"}
    print("\nRegister berhasil! Silakan login.")
daftar_aksi = {
    "tambah": menu_tambah,
    "lihat": menu_lihat,
    "keluar": menu_keluar,
    "ubah": menu_ubah,
    "hapus": menu_hapus,
    "ganda": menu_ganda,
    "riwayat": menu_riwayat,
    "kelola": menu_kelola,
}
def menu_pengguna():
    if role_aktif == "Administrator":
        menu_utama = khusus_admin
    else:
        menu_utama = khusus_guest
    while True:
        clear_screen()
        print(f"Anda login sebagai {role_aktif}")
        print("=" * 36)
        print("             MENU UTAMA")
        print("=" * 36)
        for nomor, isi_menu in menu_utama.items():
            print(f"{nomor}. {isi_menu['nama']}")
        pilih_menu = input("Pilih menu: ").strip()
        try:
            tujuan = menu_utama[pilih_menu]["tujuan"]
        except KeyError:
            print("Pilihan menu tidak valid!")
        else:
            if tujuan == "logout":
                break
            try:
                daftar_aksi[tujuan]()
            except AksesDitolakError as e:
                print(e)
        input("\nTekan Enter untuk lanjut...")
def main():
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
            if proses_login():
                menu_pengguna()
                proses_logout()
            else:
                input("Tekan Enter untuk kembali...")
        elif option == "2":
            proses_register()
            input("Tekan Enter untuk kembali...")
        elif option == "3":
            tampilkan_penutup()
            break
        else:
            print("Pilihan menu tidak valid!")
            input("Tekan Enter untuk kembali...")
try:
    main()
except KeyboardInterrupt:
    print("\n\nProgram dihentikan paksa oleh pengguna.")
except EOFError:
    print("\n\nInput terhenti secara tidak terduga. Program ditutup.")
finally:
    print("Program selesai.")