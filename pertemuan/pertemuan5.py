# infor26 = ["Herul", 26, 7.30, ["cello kost", 3]]
# print(infor26)
# # print(infor26[3][1])

# # infor26.append("Ketua angkatan")
# # print(infor26)

# # infor26.extend(["Ketua kelas", "Ketua Panitia"])
# # print(infor26)

# # infor26.insert(1, "Mahasiswa unmul")
# # print(infor26)

# # infor26[0] = "Muhammad Khairul Anaam"
# # print(infor26)

# infor26[0:2] = ["Muhammad Izhar Akmal", 42,]
# print(infor26)

# b2026 = ["fadil", "ichal", "tofa", "ilyas", "juna", "falih", "gabriel"]
# # print(b2026[0:7:2])

# juara_review_b1 = ["fadil", "gabriel"]
# juara = juara_review_b1 * 3
# print(juara)

# line_up = [ 
#     ["Ferrari", "Leclerc", 16], 
#     ["Mercedes", "Hamilton", 44], 
#     ["Red Bull", "Verstappen", 1], 
#     ["McLaren", "Norris", 4] 
# ] 
 
# for i in line_up: 
#     for j in i: 
#          print(j, end = " ")
#     print()  # print garis baru setelah setiap baris selesai

chara = ("Yukari", 20, True, 150.4, ["Odette", 25], ("Yukino", 22))
# print(chara[-2])

listchara = list(chara)
listchara.append("Yui")
nama_baru = input("Masukkan nama karakter baru: ")
listchara.extend([nama_baru]) 
chara = tuple(listchara) 
print(chara) 
# print(chara[1:5])

# chara = ("Yukari", "Yukino", "Odette", "Senku", "Rover", "hoshino") 
# # (Persona, Oregairu, Genshin, DrStone) = chara 
# (Persona, Oregairu, *anime, wuwa) = chara
# print(Persona) 
# # print(Oregairu) 
# print(anime)
# print(wuwa)


# profil_karakter = ("Arthur", 50, True, ["Pedang Suci", "Tameng Naga"]) 