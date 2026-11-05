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
sesi = {"username": "", "role": ""}
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