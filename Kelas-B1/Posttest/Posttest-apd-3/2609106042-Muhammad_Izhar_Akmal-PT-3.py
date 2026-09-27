nama = "Muhammad Izhar Akmal"
nim = "42"
biaya_langganan = 1500000

username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

if username == nama and password == nim:
    print("")
    print("Selamat datang di ANGKASA, dimana batasan inspirasi musik hanyalah imajinasi.")
    print("")
    print('''
                              ANGKASA
        Dimana batasan inspirasi musik hanyalah imajinasi.
    
      Silahkan pilih salah satu paket langganan di bawah ini :
    Paket "Orbit" dengan biaya admin 1%
    Paket "Nebula" dengan biaya admin 3%
    Paket "Galaxy" dengan biaya admin 5%
    Paket "Supernova" dengan biaya admin 7%''' )
    print("")
    pilihan_paket = str(input("Masukkan paket langganan yang anda pilih: "))
    if pilihan_paket == "Orbit":
        administrasi = 0.01
        total_bayar = biaya_langganan + (biaya_langganan * administrasi)
        print("")
        print("Paket yang anda pilih : Paket Orbit")
        print('''
        Mulai perjalanan musikmu!
        Nikmati akses dasar ke banyak lagu-lagu populer di ANGKASA!
        Selamat menikmati perjalanan musikmu ☺
        ''')
        print("")
        print(f"Total pembayaran berlangganan: Rp. {total_bayar:.2f}")

    elif pilihan_paket == "Nebula":
        administrasi = 0.03
        total_bayar = biaya_langganan + (biaya_langganan * administrasi)
        print("")
        print("Paket yang anda pilih : Paket Nebula")
        print('''
        Atur dunia musikmu!
        Nikmati lagu premium dan buat playlist kustom
        sesuai selera musikmu sendiri ☺
        ''')
        print("")
        print(f"Total pembayaran berlangganan: Rp. {total_bayar:.2f}")
        
    elif pilihan_paket == "Galaxy":
        administrasi = 0.05
        total_bayar = biaya_langganan + (biaya_langganan * administrasi)
        print("")
        print("Paket yang anda pilih : Paket Galaxy")
        print('''
        Ambil kendali dalam musik!
        Temukan berbagai lagu premium, bentuk playlistmu, dan dapatkan akses ke mode offline!
        Akses musikmu tanpa internet!
        ''')
        print("")
        print(f"Total pembayaran berlangganan: Rp. {total_bayar:.2f}")

    elif pilihan_paket == "Supernova":
        administrasi = 0.07
        total_bayar = biaya_langganan + (biaya_langganan * administrasi)
        print("")
        print("Paket yang anda pilih : Paket Supernova")
        print('''
        Rasakan kekuatan musik tanpa batas!
        Nikmati semua fitur, buka playlist kustom, mode offline, dan konten-konten eksklusif dari para artis
        ''')
        print("")
        print(f"Total pembayaran berlangganan: Rp. {total_bayar:.2f}")
    else:
        print("Paket tidak tersedia")
else:
    print("ERROR!")