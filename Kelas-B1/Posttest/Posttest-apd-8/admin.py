from auth import wajib_admin
from data import seluruh_pengunjung, riwayat_hapus, pengguna, sesi
from tampilan import (judul_halaman, pesan_error, pesan_sukses, pesan_info,
                      tampilkan_tabel_ganda, tampilkan_tabel_riwayat, tampilkan_tabel_akun)
from utils import minta_pilihan, minta_konfirmasi
def menu_ganda():
    wajib_admin()
    judul_halaman("PEMERIKSAAN DATA GANDA")
    pesan_info("Data akan dianggap ganda jika nama, tanggal, dan kategori sama.\n")
    pasangan = []
    daftar_id = list(seluruh_pengunjung.keys())
    for i in range(len(daftar_id)):
        for j in range(i + 1, len(daftar_id)):
            id_a = daftar_id[i]
            id_b = daftar_id[j]
            a = seluruh_pengunjung[id_a]
            b = seluruh_pengunjung[id_b]
            if (a["nama"].lower() == b["nama"].lower()
                    and a["tanggal"] == b["tanggal"]
                    and a["kategori"] == b["kategori"]):
                pasangan.append((id_a, id_b, a))
    if len(pasangan) == 0:
        pesan_sukses("Tidak ditemukan data ganda.")
    else:
        tampilkan_tabel_ganda(pasangan)
        print(f"\nDitemukan {len(pasangan)} pasangan data ganda.")
        print("Hapus salah satunya melalui menu Hapus data pengunjung.")
def menu_riwayat():
    wajib_admin()
    judul_halaman("RIWAYAT PENGHAPUSAN DATA")
    if len(riwayat_hapus) == 0:
        pesan_info("Belum ada data yang dihapus.")
        return
    tampilkan_tabel_riwayat()
def menu_kelola():
    wajib_admin()
    judul_halaman("KELOLA AKUN")
    tampilkan_tabel_akun()
    print("\n1. Hapus akun")
    print("2. Kembali")
    sub = minta_pilihan("Pilih: ", ("1", "2"), "Pilihan tidak valid, ulangi (1/2)!")
    if sub == "2":
        return
    target = input("Masukkan username yang akan dihapus: ").strip()
    try:
        role_target = pengguna[target]["role"]
    except KeyError:
        pesan_error("Username tidak ditemukan!")
        return
    if target == sesi["username"]:
        pesan_error("Tidak dapat menghapus akun yang sedang dipakai!")
    elif role_target == "Administrator":
        pesan_error("Akun administrator tidak dapat dihapus!")
    elif minta_konfirmasi(f"Yakin hapus akun {target}? (Ya/Tidak): "):
        del pengguna[target]
        pesan_sukses("Akun berhasil dihapus.")
    else:
        pesan_info("Penghapusan dibatalkan.")