import random

soal = (
    ["Apa nama ibukota Vietnam ?","A. Ho Chi Minh city B. Saigon C. Hanoi D. Kebumen","C"],
    ["Siapa pemenang piala dunia semalam?","A. Maroko B. Argentina C. Kamerun D.Portugal","B"],
    ["Berapa usia Indonesia?","A. 77 B.80 C.76 D.78","A"]
)

pertanyaan = random.choice(soal)
print(pertanyaan[0])
print(pertanyaan[1])
jawab = str(input("Jawab: ")).upper()
if jawab == pertanyaan[2]:
    print("Kamu benar! Silakan lewat")
else:
    print("Kamu salah! silakan tewas")

