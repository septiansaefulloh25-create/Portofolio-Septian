'''
angka = 100
if angka > 50:
    print(angka, "adalah bilangan postif")
    print("\n")

angka = -2
if angka < 0:
    print(angka, "adalah bilngan negatif")
    print("\n")

nilai = 70
if nilai > 80:
    print("selamat kamu lulus ujian ini")
    print("grade anda adalah a")
else :
    print("ahahaha mapus lu gak lulus")
    print("grade lu e")
    print("\n")

angka = int(input("masukan angka : "))
if angka > 0 :
    print("bilngan positif")
else :
    print("bilangan negatif")
    print("\n")



status = input("sudah menikah atau belum [menikah/belum]? ")
if status == "menikah":
    print("Selamat Berhagia")
else:
    print("YEUUU MAMPUSSS JOMBLOOO.....")
print("\n")


print("\n")
jawaban = input("WILL YOU MARRY ME...? (Yes/No) : ")
if jawaban.lower() == "yes":
    print("ALHAMDULILLAH.....")
else:
    print("SEMOGA KAMU BAHAGIA SAMA YANG LAIN....")
print("\n")



#contoh if, elif, else
print("\n")
kode = input("Masukan Kode Jurusan : [SI/TI/AK/PR] ")
if kode.upper() == "SI":
    print("Sistem Informasi")
elif kode.upper() == "TI":
    print("Teknik Informatika")
elif kode.upper() == "AK":
    print("Akuntasi")
elif kode.upper() == "AK":
    print("Akuntansi")
elif kode.upper() == "PR":
    print("Perhotelan")
else:
    print("Kode anda masukan SALAH!!!")
'''



nilai = int(input("masukan nilai : "))
if nilai > 100 or nilai < 0:
    print("nilai diluar jangkauan")
elif nilai > 90:
    print("anda lulus dengan grade A")
elif nilai > 80:
    print("anda lulus dengan grade B")
elif nilai > 70:
    print("anda lulu dengan grade C")
elif nilai > 10:
    print("anda lulus dengan grade D")
else :
    print("nilai luar jangkauan")
