# batas = 25
# for i in range(batas):
#     print("Perulangan ke-", i)


# game = ["Genshin", 7.0, True] 
# for i in game: 
#     print(i)  


# for i in range(1, 10):
#     print(i)


# for i in range(1, 3):# Mengontrol baris dalam tabel perkalian 
#     for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian 
#         print(f'{i} x {j} = {i * j}') 
#     print('') #biar ada jarak tiap iterasi


# jawab = "ya"  
# hitung = 0 
# while(jawab == "ya"): 
#     hitung += 1 
#     jawab = input("Ulang lagi tidak? ")
# print(f"Total Perulangan : {hitung}")


# for i in range(10): 
#     if i == 6: 
#         break 
#     print(i)


# for i in range(10):
#     if i % 2 == 0: 
#         continue 
#     print(i) 


# angka_benar = 7

# while True:
#     angka = int(input("Tebak angka antara 1-10: "))
#     if angka == angka_benar:
#         print("Selamat, tebakanmu benar!")
#         break
#     elif angka >= 11:
#         print("")
#         print("sampe 10 aja bungul, hangus dah pertanyaannya, betmut gwe")
#         break
#     else:
#         print("Tebakanmu salah, coba lagi.")


# batas = int(input("Masukkan batas bilangan ganjil:"))
# penghitung = 0

# for i in range(batas):
#      if i % 2 == 0:
#         penghitung += 1
#         continue
    
#      print(i)
# print(f'total bilangan ganjil dari 0 sampai {batas} adalah {penghitung}')


saldo = int(input("Masukkan uang saku awal: Rp "))

while saldo > 0:
    pengeluaran = int(input("Masukkan nominal pengeluaran: Rp "))
    alasan = str(input("Masukkan alasan pengeluaran: "))

    if pengeluaran <= saldo:
        saldo -= pengeluaran
        print("Saldo setelah pengeluaran: Rp", saldo)
    else:
        print("Saldo tidak mencukupi untuk pengeluaran tersebut.")
        break

print("Saldo akhir: Rp", saldo)