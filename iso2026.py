bindam = ["Miftahur Ridho", "Larasati"]
anngota_kelompok = ["Nauvan Hadya",
                     "Adzkia Firdalina",
                     "Muhammad Shaumirza Ayman",
                     "Tofa Suwarna",
                     "Ferdika Fathur Rahman",
                     "Muhammad Izhar Akmal",
                     "Muhammad Ilyas Muzakki",
                     "Artbeebi Trezequeth",
                     "Arman Nurhendra",
                     "Hanif Khailurrahim",
                     "Alfi Fadhilah",
                     "Muhammad Wira RIfadin Noor",
                     "Nur Fadilla Ariyanti",
                     "Muhammad Sultan Iqbal",
                     "Suniati Muwadah"]
profil_kelompok = """Data Science, Logo ini mempunyai data yang saling terhubung dan diolah dengan sistematis untuk menemukan pola,
                    serta menghasilkan insight. bentuk pusat menggabarkan data sebagai inti, seentara garis-garis disekitarnya mempresentasikan
                    koneksi dan proses analisis data"""

print ("Selamat datang!/")
while True:
    print ("1.Tampilkan profil kelompok")
    print ("2.Tampilkan nama bindam")
    print ("3.Tampilkan anggota kelompok")
    print ("4.Menambahkanan anggota kelompok")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        print(profil_kelompok)
    elif pilihan == 2:
        for i in bindam:
            print(i)
    elif pilihan == 3:
        for i in anngota_kelompok:
            print(i)
    elif pilihan == 4:
        anggota_baru = input("Masukkan nama anggota baru: ")
        anngota_kelompok.append(anggota_baru)
        print("Anggota baru berhasil ditambahkan.")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        break