"""menu.py - Menu utama setelah login."""
from admin import menu_ganda, menu_riwayat, menu_kelola
from auth import AksesDitolakError
from data import sesi, khusus_admin, khusus_guest
from pengunjung import menu_tambah, menu_lihat, menu_keluar, menu_ubah, menu_hapus
from tampilan import clear_screen, pesan_error, tampilkan_menu

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
    if sesi["role"] == "Administrator":
        menu_utama = khusus_admin
    else:
        menu_utama = khusus_guest
    while True:
        clear_screen()
        print(f"Anda login sebagai {sesi['role']} ({sesi['username']})")
        tampilkan_menu("MENU UTAMA", menu_utama)
        pilih_menu = input("Pilih menu: ").strip()
        try:
            tujuan = menu_utama[pilih_menu]["tujuan"]
        except KeyError:
            pesan_error("Pilihan menu tidak valid!")
        else:
            if tujuan == "logout":
                break
            try:
                daftar_aksi[tujuan]()
            except AksesDitolakError as e:
                pesan_error(e)
        input("\nTekan Enter untuk lanjut...")
