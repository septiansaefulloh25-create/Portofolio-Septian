def jalankan_kasir():
    print("=" * 40)
    print("    PROGRAM KASIR SEDERHANA UMKM")
    print("=" * 40)

    # List untuk menyimpan data barang yang dibeli
    daftar_belanja = []

    # 1. Bagian INPUT: Memasukkan item belanjaan
    while True:
        nama_barang = input("Nama barang (ketik 'selesai' jika habis): ")
        if nama_barang.lower() == "selesai":
            break

        try:
            harga = float(input(f"Harga {nama_barang} (Rp): "))
            jumlah = int(input(f"Jumlah {nama_barang} yang dibeli: "))
        except ValueError:
            print("Input harga atau jumlah harus angka! Silakan ulangi.")
            continue

        subtotal = harga * jumlah

        # Menyimpan data ke dalam list (dalam bentuk dictionary)
        item = {"nama": nama_barang, "harga": harga, "jumlah": jumlah, "subtotal": subtotal}
        daftar_belanja.append(item)
        print(f"-> Berhasil menambahkan {nama_barang}\n")

    # Jika list kosong, program berhenti
    if not daftar_belanja:
        print("\nBelum ada barang yang dibeli.")
        return

    # 2. Perhitungan Total Awal
    total_harga = sum(item["subtotal"] for item in daftar_belanja)

    # 3. Bagian PERSEN: Contoh diskon berdasarkan total belanja
    persen_diskon = 0
    if total_harga >= 100000:
        persen_diskon = 10  # Diskon 10% jika belanja di atas 100rb
    elif total_harga >= 50000:
        persen_diskon = 5  # Diskon 5% jika belanja di atas 50rb

    jumlah_diskon = total_harga * (persen_diskon / 100)
    total_akhir = total_harga - jumlah_diskon

    # 4. Menampilkan Struk / LIST Belanja
    print("\n" + "=" * 40)
    print("                STRUK BELANJA")
    print("=" * 40)
    for i, item in enumerate(daftar_belanja, start=1):
        print(f"{i}. {item['nama']} ({item['jumlah']}x) - Rp {item['subtotal']:,.0f}")

    print("-" * 40)
    print(f"Total Belanja : Rp {total_harga:,.0f}")
    print(f"Diskon ({persen_diskon}%)  : Rp {jumlah_diskon:,.0f}")
    print(f"Total Bayar   : Rp {total_akhir:,.0f}")
    print("=" * 40)
    print("      TERIMA KASIH TELAH BERBELANJA!")
    print("=" * 40)


# Menjalankan program
jalankan_kasir()