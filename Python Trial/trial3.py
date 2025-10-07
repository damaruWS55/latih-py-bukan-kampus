#buat algoritma untuk mengirim email kepada teman dengan asumsi sudah mempunyai alamat email teman anda
main_email = input("masukkan email anda: ")
to_Email = input("masukkan email tertuju: ")
Subject = input("masukkan topik email anda: ")
main = input("masukkan isi email anda: ")
cc = input("tambahkan email yg dituju: ")

print()
print('=========================================================')
print("dari: ", main_email)
print("kepada: ", to_Email)
print("Subjek", Subject)
print()
print(main)
print()
print("forward: ", cc)
print('******************************************************')
print()


#algoritma meminjam buku di perpustakaan
nama_depan = input("masukkan nama depan anda: ")
nama_Tengah = input("masukkan nama tengah anda: ")
nama_belakang = input("masukkan nama belakang anda: ")
tanggal_peminjaman = int(input("tanggal meminjam: "))
x = +5
batas_pengembalian = int(input("masukkan lama peminjaman buku: "))
nama_lenkap = nama_depan + nama_Tengah + nama_belakang
print("nama anda adalah: ", nama_lenkap)
print("tanggal anda meminjam buku: ", tanggal_peminjaman)

if batas_pengembalian > x:
    print("mohon maaf anda tidak bisa meminjam")

if batas_pengembalian < x:
    print("anda bisa meminjam")

if batas_pengembalian == x:
    print("anda bisa meminjam")