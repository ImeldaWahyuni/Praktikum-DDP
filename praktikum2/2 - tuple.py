#tuple1
# nama = "Mahasiswa A"
# usia = 17
# nilai = 98
# status = ("gagal","lulus")[nilai > 80]

# print(status)

# dunia = (
#     ("Arab Saudi","China","Filipina"),
#     ("Prancis","Jerman","Italia"),
#     ("Maroko","Pantai Gading","Senegal")
# )

# for benua in dunia:
#     for negara in benua:
#         print(negara, end=",")


#khusus print indeks
# dunia = (
#     ("Arab Saudi","China","Filipina"),
#     ("Prancis","Jerman","Italia"),
#     ("Maroko","Pantai Gading","Senegal")
# )

# print(dunia[2][0])

# for benua in dunia:
#     for negara in benua:
#         print(negara, end=",")


bumi = ((
    ("Arab Saudi","China","Filipina"),
    ("Prancis","Jerman","Italia"),
    ("Maroko","Pantai Gading","Senegal")
),
(
    ("Depok","Bekasi","Bogor"),
    ("Jakarta","Cikarang","Cibubur"),
    ("Jaktim","Jonggol","Karawang")
))

print()

for benua in bumi:
    for negara in benua:
        print(negara, end="-")