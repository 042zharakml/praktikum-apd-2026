# import math # Mengimpor semua fungsi yang ada di dalam library math 
# from math import sqrt # Hanya mengimpor fungsi sqrt() dari library math 
# import math as m # Mendefinisikan math dengan nama m

# from datetime import datetime 
# print(datetime.now()) 

# import calendar as kalender 
# print(kalender.calendar(2026))

# import random 
 
# # Menghasilkan satu bilangan bulat acak dari 1 sampai 5 (inklusif) 
# print(random.randint(1, 5)) 
 
# # Memilih 1 elemen acak dari list atau string 
# buah = ["pisang", "rambutan", "manggis"] 
# huruf = "abcd" 
# print(random.choice(buah))   # memilih 1 item acak pada list 
# print(random.choice(huruf))  # memilih 1 karakter acak pada string 
 
# Menyusun 4 angka PIN acak menggunakan perulangan 
# kumpulan_angka = "0123456789" 
# pin_acak = "" 
# for i in range(4): 
#     pin_acak += random.choice(kumpulan_angka) 
# print(pin_acak) 
 
# # Mengacak urutan elemen di dalam list secara langsung 
# kartu = ["As Wajik", "3 Hati", "7 Sekop"] 
# random.shuffle(kartu) 
# print(kartu) 