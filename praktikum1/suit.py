import random

def play():
    pemain = int(input("pilih\n 1. batu\n 2. gunting\n 3. kertas\n"))
    if pemain == 1:
        pilihan = "batu"
    elif pemain == 2:
        pilihan = "gunting"
    elif pemain == 3:
        pilihan = "kertas"

    lawan = random.choice(["batu","gunting","kertas"])
    print(f"Komputer adalah {lawan}")

    if pilihan == lawan:
        print("Seimbang, tidak ada yang menang")
    elif (pilihan == "batu") and (lawan == "gunting") or (pilihan == "gunting") and (lawan == "kertas") or (pilihan == "kertas")and (lawan == "batu"):
        print("Kamu menang")
    else:
         print("Kamu kalah")



play()
