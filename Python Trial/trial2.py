#int
nama = input("masukkan nama anda: ")
umur = 20
tahun_lahir = 2005
saldo = int(input("masukkan uang anda: "))
nol = 0

print(umur)

print(type(umur))
print(type(saldo))
print()
print(f"halo  nama saya {nama.upper()}, umur saya {umur}\nsalam kenal\!")
print(" ")
hutang = int(input("masukkan hutang anda: "))
sisa_saldo = saldo - hutang
print()
jatah_bulanan = sisa_saldo / 12
pengeluaran_harian = int(input("masukkan pengeluaran perhari: "))
pengeluaran_30_hari = print("pengeluaran bulanan anda adalah: ", pengeluaran_harian * 30)
sisa_uang_yang_ditabung = print("uang yang bisa ditabung anda adalah: ", jatah_bulanan % pengeluaran_harian)
print()
print(sisa_saldo)
print(type(hutang))
print(hutang)
#1e5
#e adalah 10^n

#string
puisi = """
aku\\adalah\\aku\\\\
kamu\tadalah\"kamu\"
dia adalah dia
"""

print(puisi)
print(type(puisi))

#boolean
is_student = True
is_married = False
has_license = False

print(type(is_married))
nama = "python"
nama_title = nama.title()
print(nama_title)
print(nama[0])
print(nama[1])
print(nama[2])
print(nama[3])
print(nama[4])
print(nama[5])
print()
print(nama[-1])
print()
print(nama[0:3])
print(nama[2:5])
print(nama[1:4])


kalimat = "i can stop"
jumlah_a = kalimat.count("a")
kalimat_baru = kalimat.replace("stop", "python")
print(kalimat)
print(jumlah_a)
print(kalimat_baru)

