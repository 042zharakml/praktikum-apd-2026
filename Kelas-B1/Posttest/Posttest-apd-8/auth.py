from getpass import getpass
from data import pengguna, sesi
from tampilan import clear_screen, judul_halaman, pesan_error, pesan_sukses
class AksesDitolakError(Exception):
    pass
def wajib_admin():
    if sesi["role"] != "Administrator":
        raise AksesDitolakError("Akses ditolak! Menu ini hanya untuk Administrator.")
def username_sudah_ada(nama_user):
    for u in pengguna:
        if u.lower() == nama_user.lower():
            return True
    return False
def proses_login():
    clear_screen()
    print("")
    username = input("Masukkan username: ").strip()
    password = getpass("Masukkan password: ").strip()  # password tidak terlihat
    try:
        akun = pengguna[username]
        if akun["password"] != password:
            raise ValueError("Password salah")
    except (KeyError, ValueError):
        pesan_error("Username atau password anda salah, silahkan coba login kembali.")
        return False
    sesi["username"] = username
    sesi["role"] = akun["role"]
    return True
def proses_logout():
    sesi["username"] = ""
    sesi["role"] = ""
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
            pesan_error(e)
        else:
            break
    while True:
        password_baru = getpass("Masukkan password baru (min. 6 karakter): ").strip()
        try:
            if len(password_baru) < 6:
                raise ValueError("Password minimal 6 karakter!")
            ulang = getpass("Masukkan kembali password: ").strip()
            if ulang != password_baru:
                raise ValueError("Konfirmasi password tidak sama!")
        except ValueError as e:
            pesan_error(e)
        else:
            break
    pengguna[username_baru] = {"password": password_baru, "role": "Petugas Pendaftaran"}
    pesan_sukses("\nRegister berhasil! Silakan login.")