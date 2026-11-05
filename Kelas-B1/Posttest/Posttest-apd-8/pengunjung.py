from auth import wajib_admin
from data import (seluruh_pengunjung, riwayat_hapus, sesi, kategori_pengunjung,
                  alasan_hapus, dlm_lihat, kolom_admin)
from tampilan import (clear_screen, judul_halaman, pesan_error, pesan_sukses, pesan_info,
                      tampilkan_detail, tampilkan_tabel, tampilkan_pilihan)
from utils import (ke_angka, ambil_waktu_sekarang, minta_input_wajib, minta_pilihan,
                   minta_konfirmasi, input_tanggal, input_jam)
def buat_id_baru():
    id_baru = 1
    for id_pengunjung in seluruh_pengunjung:
        if id_pengunjung >= id_baru:
            id_baru = id_pengunjung + 1
    for catatan in riwayat_hapus.values():
        if catatan["id_pengunjung"] >= id_baru:
            id_baru = catatan["id_pengunjung"] + 1
    return id_baru
def cari_pengunjung(teks_id):
    id_angka = ke_angka(teks_id.strip(), "ID")
    return id_angka, seluruh_pengunjung[id_angka]
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
def _ambil_pengunjung_dari_input():
    """Minta ID lalu kembalikan (id, data); None jika gagal."""
    try:
        return cari_pengunjung(input("Masukkan ID pengunjung: "))
    except ValueError as e:
        pesan_error(e)
    except KeyError:
        pesan_error("ID tidak ditemukan!")
    return None
def menu_tambah():
    judul_halaman("TAMBAH DATA PENGUNJUNG")
    nama = minta_input_wajib("Nama pengunjung: ", "Nama")
    print("")
    tanggal_berkunjung = input_tanggal()
    print("-" * 45)
    print(f"Tanggal berkunjung : {tanggal_berkunjung}")
    print("-" * 45)
    pesan_info(f"{nama} berkunjung sebagai:")
    tampilkan_pilihan("KATEGORI PENGUNJUNG", kategori_pengunjung)
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
    pesan_sukses(f"\nData pengunjung berhasil ditambahkan dengan ID {new_id}.")
def menu_lihat():
    judul_halaman("LIHAT DATA PENGUNJUNG")
    tampilkan_pilihan("CARI BERDASARKAN", dlm_lihat)
    pilihan = input("Pilih kategori data: ").strip()
    if pilihan not in dlm_lihat:
        pesan_error("Pilihan kategori data tidak valid!")
        return
    kata_kunci = ""
    if pilihan == "2":
        clear_screen()
        tampilkan_pilihan("KATEGORI PENGUNJUNG", kategori_pengunjung)
        pil_kat = input("Pilih kategori: ").strip()
        if pil_kat not in kategori_pengunjung:
            pesan_error("Pilihan kategori tidak valid!")
            return
        kata_kunci = kategori_pengunjung[pil_kat]
    elif pilihan == "3":
        clear_screen()
        kata_kunci = input_tanggal(boleh_batal=True)
        if kata_kunci is None:
            pesan_info("Pencarian dibatalkan.")
            return
    elif pilihan == "4":
        clear_screen()
        kata_kunci = input("Masukkan nama (boleh sebagian): ").strip().lower()
        if len(kata_kunci) == 0:
            pesan_error("Nama tidak boleh kosong!")
            return
    hasilnya = {}
    for id_pengunjung, data in seluruh_pengunjung.items():
        if cocok_filter(pilihan, data, kata_kunci):
            hasilnya[id_pengunjung] = data
    print()
    if len(hasilnya) == 0:
        pesan_info("Tidak ada data yang sesuai kriteria.")
    else:
        clear_screen()
        tampilkan_tabel(hasilnya)
def menu_keluar():
    judul_halaman("TANDAI PENGUNJUNG KELUAR")
    hasil = _ambil_pengunjung_dari_input()
    if hasil is None:
        return
    id_cari, data = hasil
    if data["jam_keluar"] != "-":
        pesan_info("Pengunjung ini sudah ditandai keluar.")
        return
    print(f"\nNama       : {data['nama']}")
    print(f"Jam masuk  : {data['jam_masuk']}")
    jam = input_jam("Jam keluar (HH:MM, kosong = batal): ", boleh_kosong=True, awal=data["jam_masuk"])
    if jam == "":
        pesan_info("Dibatalkan.")
    else:
        data["jam_keluar"] = jam
        pesan_sukses("Pengunjung berhasil ditandai keluar.")
def menu_ubah():
    wajib_admin()
    judul_halaman("UBAH DATA PENGUNJUNG")
    if len(seluruh_pengunjung) == 0:
        pesan_info("Belum ada data pengunjung.")
        return
    hasil = _ambil_pengunjung_dari_input()
    if hasil is None:
        return
    id_ubah, data = hasil
    tampilkan_detail(data)
    print()
    tampilkan_pilihan("DATA YANG INGIN DIUBAH", {k: v["nama"] for k, v in kolom_admin.items()})
    pilih_kolom = input("Pilih: ").strip()
    if pilih_kolom not in kolom_admin:
        pesan_error("Pilihan tidak valid!")
        return
    kunci = kolom_admin[pilih_kolom]["kunci"]
    nama_kolom = kolom_admin[pilih_kolom]["nama"]
    if kunci == "nama":
        nama_baru = input("Masukkan nama baru. (Jika bagian ini kosong, perubahan akan dibatalkan): ").strip()
        if len(nama_baru) == 0:
            pesan_info("Perubahan nama dibatalkan.")
        else:
            data["nama"] = nama_baru
            pesan_sukses("\nNama pengunjung berhasil diubah.")
    elif kunci == "tanggal":
        tanggal_baru = input_tanggal(boleh_batal=True)
        if tanggal_baru is None:
            pesan_info("Perubahan tanggal dibatalkan.")
        else:
            data["tanggal"] = tanggal_baru
            pesan_sukses("\nTanggal berkunjung berhasil diubah.")
    elif kunci == "kategori":
        tampilkan_pilihan("KATEGORI PENGUNJUNG", kategori_pengunjung)
        kode = minta_pilihan("Pilih kategori baru anda (Jika bagian ini kosong, perubahan akan dibatalkan): ",
                             kategori_pengunjung, "Pilihan kategori tidak valid!", boleh_kosong=True)
        if kode == "":
            pesan_info("Perubahan kategori dibatalkan.")
        else:
            data["kategori"] = kategori_pengunjung[kode]
            pesan_sukses("\nKategori berhasil diubah.")
    elif kunci == "perkara":
        perkara_baru = input("Duduk perkara baru (kosong = batal): ").strip()
        if len(perkara_baru) == 0:
            pesan_info("Perubahan perkara dibatalkan.")
        else:
            data["perkara"] = perkara_baru
            pesan_sukses("Duduk perkara berhasil diubah.")
    else:
        pesan = f"{nama_kolom} baru dengan format HH:MM (Jika anda mengosongkan perubahan ini, maka perubahan dibatalkan): "
        if kunci == "jam_masuk":
            jam_baru = input_jam(pesan, boleh_kosong=True, akhir=data["jam_keluar"])
        else:
            jam_baru = input_jam(pesan, boleh_kosong=True, awal=data["jam_masuk"], boleh_strip=True)
        if jam_baru == "":
            pesan_info("Perubahan dibatalkan.")
        else:
            data[kunci] = jam_baru
            pesan_sukses(f"{nama_kolom} berhasil diubah.")
def menu_hapus():
    wajib_admin()
    judul_halaman("HAPUS DATA PENGUNJUNG")
    if len(seluruh_pengunjung) == 0:
        pesan_info("Belum ada data pengunjung.")
        return
    hasil = _ambil_pengunjung_dari_input()
    if hasil is None:
        return
    id_hapus, data = hasil
    tampilkan_detail(data)
    print()
    tampilkan_pilihan("ALASAN PENGHAPUSAN", alasan_hapus)
    kode = minta_pilihan("Pilih alasan: ", alasan_hapus, "Pilihan alasan tidak valid!")
    alasan = alasan_hapus[kode]
    if minta_konfirmasi("\nApakah anda yakin ingin menghapus data ini? (Ya/Tidak): "):
        nomor_riwayat = len(riwayat_hapus) + 1
        riwayat_hapus[nomor_riwayat] = {
            "id_pengunjung": id_hapus,
            "nama": data["nama"],
            "tanggal": data["tanggal"],
            "alasan": alasan,
            "dihapus_oleh": sesi["username"],
            "waktu": ambil_waktu_sekarang(),
        }
        del seluruh_pengunjung[id_hapus]
        pesan_sukses("Data berhasil dihapus dan dicatat di riwayat penghapusan.")
    else:
        pesan_info("Penghapusan ini dibatalkan.")