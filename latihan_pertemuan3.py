'''
print("============ KALKULATOR SEDERHANA ============")
#Input Data Diri Pengguna
nim = input("NIM : ")
nama = input("Nama Lengkap : ")
nilai1 = int(input("Masukan Nilai 1 :"))
nilai2 = int(input("Masukan Nilai 2 : "))
nilai3 = int(input("Masukan Nilai 3 : "))
#Proses Perhitungan
hasiljumlah = nilai1 + nilai2 + nilai3
hasilkurang = nilai1 - nilai2 + nilai3
#output hasil
print("\n")
print("============ HASIL OPERASIONAL ============")
print("nim : ", nim)
print("nama : ", nama)
print("hasil penjumlahan ",nilai1, "+" ,nilai2, "+" ,nilai3 , "=" ,hasiljumlah)
print("hasil pengurangan ",nilai1, "-" ,nilai2, "-" ,nilai3 , "=" ,hasilkurang)
print("\n")
print("Selamat Menikmati...:-")
print("\n")
'''

'''
#index
var1 = 'Hello Python'
var2 = "I Love You"
var3 = "BSI TSK"
print("\n")
print("var1[0]",var1[7])
print("var2[2:6]",var2[4:8])
print("var3[0:4]",var3[1:4])
print("\n")
'''

print("\n")
nama = "{}, {}, dan {},".format("Asep", "Budi", "Cecep")
print(nama)

print("\n")
nama = "{0}, {2}, dan {1}".format("Asep", "Budi", "Cecep")
print(nama)

print("\n")

nomor = "{0}, {4}, {2}, {3}, {1}".format("1","2","3","4","5")
print(nomor)
print("\n")

print("|{:<10}|{:^10}|{:>10}|".format('beras','gula','garam'))
print("\n")