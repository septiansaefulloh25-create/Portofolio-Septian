# PROGRAM APLIKASI MENGHITUNG LUAS & VOLUME BALOK
print("PROGRAM APLIKASI MENGHITUNG LUAS & VOLUME BALOK")

n = int(input("Mau Input Berapa Kali Mas? "))

data_balok = []

for i in range(1, n + 1):
  print(f"Input Ke- {i}")
  panjang = int(input("Masukan panjang : "))
  lebar = int(input("Masukan lebar : "))
  tinggi = int(input("Masukan tinggi : "))

  # Hitung luas permukaan balok (2*(p*l + p*t + l*t)) atau sesuai rumus di kelas Anda
  luas = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
  volume = panjang * lebar * tinggi

  data_balok.append(
      {"panjang": panjang, "lebar": lebar, "tinggi": tinggi, "luas": luas, "volume": volume}
  )

print("\nHasil Perhitungan Luasnya adalah")
print("=" * 60)
print(f"{'Panjang':<10} {'Lebar':<10} {'Tinggi':<10} {'Luas':<10}")
print("=" * 60)

for item in data_balok:
  print(f"{item['panjang']:<10} {item['lebar']:<10} {item['tinggi']:<10} {item['luas']:<10}")

print("=" * 60)

tanya_vol = input("Mau Tampilkan hasil Volumenya [Y/T] ? ")
if tanya_vol.upper() == "Y":
  print("\nHasil Perhitungan Volumenya adalah")
  print("=" * 60)
  print(f"{'Panjang':<10} {'Lebar':<10} {'Tinggi':<10} {'Volume':<10}")
  print("=" * 60)
  for item in data_balok:
    print(f"{item['panjang']:<10} {item['lebar']:<10} {item['tinggi']:<10} {item['volume']:<10}")
  print("=" * 60)