# def luas_persegipanjang():
#     luas = 3 * 5
#     return luas
# hasil = luas_persegipanjang()
# print("Luas persegi panjang utama:", hasil)
# print("Luas persegi panjang utama:", luas_persegipanjang())

# def luas_persegi(sisi, lebar=5):
#     luas = sisi * lebar
#     return luas
# sisi = int(input("Masukkan sisi persegi: "))
# hasil = luas_persegi(sisi)
# print("Luas persegi: ", hasil)

# def pengumuman():
#     print("JANGAN LUPA BAHAGIA")

# for i in range(3):
#     pengumuman()

#Membuat variabel global 
# nama = "Larry" 
# prodi = "Informatika" 
 
# #Membuat variabel lokal 
# def data(): 
#     nama = "Teknik Kedokteran" 
#     prodi = "Kedokteran Lanjut" 
#     print("Nama:", nama) 
#     print("Prodi:", prodi) 
#  #Mengakses variabel lokal 
# data() 
# #Mengakses variabel global 
# print("Nama:", nama) 
# print("Prodi:", prodi) 
 
# def faktorial(n): 
#     #Base Case: Kondisi fungsi berhenti 
#     if n == 0 or n == 1: 
#         return 1 
#     #Rekursive Case: Fungsi memanggil dirinya sendiri 
#     else: 
#         return n * faktorial(n - 1) 
#     #Memanggil fungsi 

# hasil_faktorial = faktorial(4) 
# print(f"Hasil dari 4! {hasil_faktorial}") 
#Output 
# Hasil dari faktorial 4! adalah 24 

# umur = int(input('Masukkan Angka : ')) 
# print(umur) 

# try: 
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#       print('input yang anda masukkan bukan Integer (angka)')

# try: 
#     angka = int(input('Masukkan Angka : ')) 
# except ValueError: 
#     print('input yang anda masukkan bukan Integer (angka)') 
# else: 
#     print(f'Angka yang kamu input : {angka}') 
# finally: 
#     print('Blok Try Selesai') 

try: 
    usn = input('Username yang diinginkan : ') 
    if len(usn) < 5: 
        raise ValueError('Nama Minimal Memiliki 5 karakter') 
except ValueError as e: 
    print(e) 