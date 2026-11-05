"""tampilan.py - Semua output ke layar (PrettyTable)."""
import os

from prettytable import PrettyTable, ALL

from data import pengguna, riwayat_hapus


# ---------- Pesan ----------
def pesan_sukses(teks):
    print(teks)


def pesan_error(teks):
    print(teks)


def pesan_info(teks):
    print(teks)


# ---------- Layar ----------
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def judul_halaman(judul):
    clear_screen()
    print(f"=== {judul} ===")


# ---------- Tabel (prettytable) ----------
def _buat_tabel(judul, kolom, rata_kiri=True):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = kolom
    if rata_kiri:
        tabel.align = "l"
    tabel.max_width = 34
    tabel.hrules = ALL
    return tabel


def tampilkan_pilihan(judul, daftar):
    """daftar: dict {kode: teks}"""
    tabel = _buat_tabel(judul, ["No", "Pilihan"])
    for kode, teks in daftar.items():
        tabel.add_row([kode, teks])
    print(tabel)


def tampilkan_menu(judul, menu):
    """menu: dict {nomor: {"nama": ..., "tujuan": ...}}"""
    tabel = _buat_tabel(judul, ["No", "Menu"])
    for nomor, isi in menu.items():
        tabel.add_row([nomor, isi["nama"]])
    print(tabel)


def tampilkan_detail(data):
    tabel = _buat_tabel("DETAIL PENGUNJUNG", ["Keterangan", "Isi"])
    tabel.add_row(["Nama", data["nama"]])
    tabel.add_row(["Tanggal", data["tanggal"]])
    tabel.add_row(["Kategori", data["kategori"]])
    tabel.add_row(["Duduk perkara", data["perkara"]])
    tabel.add_row(["Jam masuk", data["jam_masuk"]])
    tabel.add_row(["Jam keluar", data["jam_keluar"]])
    print()
    print(tabel)


def tampilkan_tabel(hasilnya):
    tabel = _buat_tabel(
        "DATA PENGUNJUNG",
        ["ID", "Nama", "Tanggal", "Kategori", "Duduk Perkara", "Masuk", "Keluar"],
    )
    for id_pengunjung, d in hasilnya.items():
        tabel.add_row([id_pengunjung, d["nama"], d["tanggal"], d["kategori"],
                       d["perkara"], d["jam_masuk"], d["jam_keluar"]])
    print(tabel)
    print(f"\nTotal: {len(hasilnya)} Data")


def tampilkan_tabel_ganda(pasangan):
    tabel = _buat_tabel("DATA GANDA", ["ID A", "ID B", "Nama", "Tanggal", "Kategori"])
    for id_a, id_b, d in pasangan:
        tabel.add_row([id_a, id_b, d["nama"], d["tanggal"], d["kategori"]])
    print(tabel)


def tampilkan_tabel_riwayat():
    tabel = _buat_tabel(
        "RIWAYAT PENGHAPUSAN DATA",
        ["ID", "Nama", "Tanggal", "Alasan", "Oleh", "Waktu Hapus"],
    )
    for r in riwayat_hapus.values():
        tabel.add_row([r["id_pengunjung"], r["nama"], r["tanggal"],
                       r["alasan"], r["dihapus_oleh"], r["waktu"]])
    print(tabel)
    print(f"\nTotal: {len(riwayat_hapus)} data dihapus")


def tampilkan_tabel_akun():
    tabel = _buat_tabel("DAFTAR AKUN", ["No", "Username", "Role"])
    for nomor, (nama_user, info) in enumerate(pengguna.items(), start=1):
        tabel.add_row([nomor, nama_user, info["role"]])
    print(tabel)


# ---------- Header & penutup ----------
def tampilkan_header_utama():
    clear_screen()
    print("=" * 42)
    print(" SISTEM PENDATAAN PENGUNJUNG PENGADILAN")
    print("=" * 42)


def tampilkan_penutup():
    clear_screen()
    print("=" * 68)
    print("")
    print(" Sebelum pulang kerja, jangan lupa memeriksa kembali area kerja ♥♥♥")
    print("")
    print("JANGAN LUPA ISTIRAHAT YANG CUKUP ♥♥♥".center(68, " "))
    print("")
    print("=" * 68)
