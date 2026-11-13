while True:
    nama = input("Masukan nama anda : ")
    kode = input("Masukan kode mainan : [M/P/R]")

    if kode.upper() == "M":
        namamainan ="Mobil-mobilan"
        harga=10000
    elif kode.upper() == "P" :
        namamainan ="Pistol"
        harga=15000
    elif kode.upper() == "R" :
        namamainan ="Robot"
        harga=20000
    else:
        mainan="Kode yang anda masukan salah"
        harga=0

    jumlah = int(input("Masukan jumlah beli : "))
    total = (jumlah*harga)

    print("========Nota Transaksi========")
    print("Masukan nama anda : ",nama)
    print("Masukan kode mainan : ",kode)
    print("Masukan nama mainan : ",namamainan)
    print("Harga mainan tersebut adalah : ",harga)
    print("Masukan jumlah beli : ",jumlah)
    print("Masukan total : ",total)
    ulang = input("Apakah ingin menginput data lagi? (y/t): ")
    if ulang.lower() == "t":
        print("Program selesai. Terima kasih.!")
    