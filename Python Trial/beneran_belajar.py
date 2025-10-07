Nama_Pembeli = input("Masukkan Nama Pembeli: ")
Kode_Pembeli = input("masukkkan Kode Mainan: ")
Harga = int(input("Masukkan Harga Satuan: "))
diskon_satuan = Harga * 0.20
Jumlah_Beli = int(input("Masukkan Jumlah Beli: "))
Total_Harga_Belanja = Harga * diskon_satuan * Jumlah_Beli
Uang_Dibayarkan = int(input("Uang Dibayarkan: "))
Total_Kembalian = Uang_Dibayarkan - Total_Harga_Belanja

print("Nama Pembeli: ", Nama_Pembeli)
print("Kode Pembeli: ", Kode_Pembeli)
print("====================================================================================")
print("Total Harga Belanja: ", Total_Harga_Belanja)
print(Uang_Dibayarkan)

if Uang_Dibayarkan >= Total_Harga_Belanja:
    print("terlebih: ", Total_Kembalian)

if Uang_Dibayarkan < Total_Harga_Belanja:
    print("uang anda kurang: ", Total_Kembalian)

if Uang_Dibayarkan == Total_Harga_Belanja:
    print("kembalian anda adalah: ", Total_Kembalian)

print("Total Kembalian: ", Total_Kembalian)
print("Terimakasih telah berbelanja!")
print('=' * 550)