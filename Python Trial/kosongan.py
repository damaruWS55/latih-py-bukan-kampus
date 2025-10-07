nama_pengguna = input("masukkan nama anda: ")
nim = input("masukkan nim anda: ")
hari_pinjam = input("masukkan hari: ")
tanggal = int(input("masukkan tanggal: "))
bulan = (input("masukkan bulan: "))
tahun = input("masukkan tahun: ")
judul_buku = input("masukkan judul buku: ")

tanggal_kembali = int(input("Masukkan tanggal pengembalian: "))
bulan_pengembalian = (input("masukkan bulan pengembalian: "))
print()
print("nama anda adalah ", nama_pengguna)
print("anda meminjam pada: ", hari_pinjam + ", ", str(tanggal) + " " + bulan + " " + tahun)
print ("buku yang anda pinjam: ", judul_buku)
print ("target penfembalian: ", str(tanggal_kembali) + "/" + bulan_pengembalian +"/"+ tahun)
bataspinjam = tanggal_kembali - tanggal
print("="*50)
if bataspinjam <= 7:
    print("anda bisa meminjam")
else:
    print("anda tidak bisa meminjam")

