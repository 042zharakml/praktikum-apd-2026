username = "izhar"
password = "042"

while True:
    username_input = input("Masukkan username: ")
    password_input = input("Masukkan password: ")

    if username_input == username and password_input == password:
        print("")
        print("Login berhasil!")
        break
    elif username_input != username:
        print("")
        print("Username salah, silahkan ulangi login anda")
    else:
        print("")
        print("Password salah, silahkan ulangi login anda.")


total_kalimantan_gambut = 0
total_kalimantan_mineral = 0
total_sumatera_gambut = 0
total_sumatera_mineral = 0


while True:
    print("")
    pulau = input(
        "Masukkan nama pulau (KALIMANTAN atau SUMATERA): "
    ).upper()

    if pulau == "KALIMANTAN":
        lahan = input(
            "Masukkan jenis lahan (GAMBUT atau MINERAL): "
        ).upper()

        if lahan == "GAMBUT":
            kategori = "Kalimantan-Gambut"
            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5
            total_kalimantan_gambut += luas

        elif lahan == "MINERAL":
            kategori = "Kalimantan-Mineral"
            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5
            total_kalimantan_mineral += luas

        else:
            print("Jenis lahan tidak dikenali.")
            continue

    elif pulau == "SUMATERA":
        lahan = input(
            "Masukkan jenis lahan (GAMBUT atau MINERAL): ").upper()

        if lahan == "GAMBUT":
            kategori = "Sumatera-Gambut"
            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5
            total_sumatera_gambut += luas

        elif lahan == "MINERAL":
            kategori = "Sumatera-Mineral"
            hotspot = int(input("Jumlah Titik Api (Hotspot): "))
            luas = hotspot * 5
            total_sumatera_mineral += luas

        else:
            print("Jenis lahan tidak dikenali.")
            continue

    else:
        print("Nama pulau tidak dikenali.")
        print("Pilih pulau KALIMANTAN atau SUMATERA saja.")
        continue


    print("Kategori:", kategori)
    print("Luas lahan terbakar:", luas, "Hektare")
    print("")

    lagi = input("Apakah anda masih mau input data titik api lagi? (Y/T): ").upper()

    if lagi == "T":
        break
    elif lagi == "Y":
        continue
    else:
        print("Input tidak valid. Program akan mengakhiri input data.")
        break

print("===================================")
print("     RINGKASAN DATA KEBAKARAN")
print("===================================")

print("Kalimantan-Gambut  :", total_kalimantan_gambut, "Hektare")
print("Kalimantan-Mineral :", total_kalimantan_mineral, "Hektare")
print("Sumatera-Gambut    :", total_sumatera_gambut, "Hektare")
print("Sumatera-Mineral   :", total_sumatera_mineral, "Hektare")

total_seluruh = (total_kalimantan_gambut+total_kalimantan_mineral+total_sumatera_gambut+total_sumatera_mineral)

print("-----------------------------------")
print("Total keseluruhan  :", total_seluruh, "Hektare")
print("===================================")