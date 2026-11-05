from auth import proses_login, proses_logout, proses_register
from menu import menu_pengguna
from tampilan import tampilkan_header_utama, tampilkan_penutup, tampilkan_menu, pesan_error
menu_awal = {
    "1": {"nama": "Login dengan akun anda"},
    "2": {"nama": "Lakukan register akun baru"},
    "3": {"nama": "Keluar"},
}
def main():
    while True:
        tampilkan_header_utama()
        tampilkan_menu("MENU AWAL", menu_awal)
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
            pesan_error("Pilihan menu tidak valid!")
            input("Tekan Enter untuk kembali...")
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram dihentikan paksa oleh pengguna.")
    except EOFError:
        print("\n\nInput terhenti secara tidak terduga. Program ditutup.")
    finally:
        print("Program selesai.")