from warung import *

pembeli = Warung("Pembeli",1000)

daftar = []
def strukk():
    print("STRUK MAKANAN")
    print("-------------")
    for makanan in daftar:
        print(makanan)
    print("-------------")

while True:
    print("# Menu")
    print("1. Nasi Kuninng\t- 5000")
    print("2. Kopi Susu\t- 3500")
    print("3. Roti\t- 4000")
    print("4. Keluar")
    print("Sisa saldo: ",pembeli.uang)
    menu = int(input("Pilih Menu yang ingin dipesan: "))
    if menu == 1:
        pembeli.uang -= 5000
        daftar.append("Nasi Kuning\t- 5000")
        print("Sisa uang:", pembeli.uang)
    elif menu == 2:
        pembeli.uang -= 3500
        daftar.append("Kopi Susu\t- 3500")
        print("Sisa uang:", pembeli.uang)
    elif menu == 3:
        pembeli.uang -= 4000
        daftar.append("Roti\t- 4000")
        print("Sisa uang:", pembeli.uang)
    elif menu == 4 or pembeli.uang <= 0:
        break