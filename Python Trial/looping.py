# for i  in range(5):
#     print(i)

# for i in range(1, 6):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# angka = 1
# while angka <= 5:
#     print(angka)
#     angka += 1
angka_rahasia = 9

while True:
    tebakan = int(input("masukkan tebakan: "))
    if tebakan== angka_rahasia:
        print("selamat tebakan anda benar:")
        break
    else:
        print("salah, coba lagi")
