# nilai = int(input("masukkan nilai anda: "))
# if nilai >= 90:
#     print("nilai anda A")
# elif nilai >= 80:
#     print("maka nilai anda B")
# elif nilai >= 70:
#     print("maka nilai anda C")
# elif nilai >= 60:
#     print("maka nilai anda adalah D")
# else:
#     print("Anda tidak lulus")

ussername = input("username: ")
password = input("password: ")

if ussername == "admin":
        
    if password == "123456":
        print("selamat datang admin")
        print("login berhasil")
    else :
        print("password salah")

else:
    print("username tidak ditemukan")