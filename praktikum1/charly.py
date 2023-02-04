import random
def charlie():
    pertanyaan= ""
    jawaban = ""
    permainan = 1
    choice = ["yes","No","Maybe"]
    while permainan == 1 :
        pertanyaan = str(input("Apa Yang Ingin Kamu Tanyakan\n"))
        jawaban = random.choice(choice)
        print(jawaban)
        permainan = int(input("Tekan 1 jika ingin bertanya lagi"))
    print("goodbye")

charlie()
