"""utils.py - Fungsi bantu: konversi, validasi, dan pengambilan input."""
from datetime import datetime

from data import hari_per_bulan, nama_tiap_bulan
from tampilan import pesan_error, pesan_info


def ambil_waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def ke_angka(teks, nama="Input"):
    try:
        return int(teks)
    except ValueError:
        raise ValueError(f"{nama} harus berupa angka!") from None


# ---------- Validasi tanggal & jam ----------
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


# ---------- Input berulang sampai valid ----------
def minta_input_wajib(pesan, label):
    teks = input(pesan).strip()
    if len(teks) == 0:
        pesan_error(f"{label} tidak boleh kosong!")
        return minta_input_wajib(pesan, label)
    return teks


def minta_pilihan(pesan, daftar_valid, pesan_salah, boleh_kosong=False):
    pilihan = input(pesan).strip()
    if boleh_kosong and pilihan == "":
        return ""
    if pilihan in daftar_valid:
        return pilihan
    pesan_error(pesan_salah)
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
            pesan_info("\nMasukkan tanggal berkunjung (kosongkan semua kolom untuk membatalkan):")
        else:
            pesan_info("Masukkan tanggal, bulan, dan tahun secara terpisah di bawah ini:")
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
            pesan_error(e)
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
            pesan_error(e)
        else:
            return jam
