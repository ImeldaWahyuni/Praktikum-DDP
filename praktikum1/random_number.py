import random

def tebak(x):
    angka = random.randint(1,x)
    tebak = 0
    while tebak != angka :
        tebak = int(input(f"tebak angka antara 1 sampai {x}\n"))
        if tebak < angka :
            print("angka yang kamu tebak, terlalu rendah, silahkan coba lagi\n")
        elif tebak > angka:
            print("angka yang kamu tebak, terlalu tinggi, silahkan coba lagi\n")
    print(f"tebakan mu benar! angka yang benar adalah {angka}")

x = int(input("tentukan batasan angka\n"))
tebak(x)