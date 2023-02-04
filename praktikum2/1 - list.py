asteng = ["Indonesia", "Malaysia", "Filipina"]

#Mengubah data
asteng[1] = "Singapura"
asteng[2] = "Serbia"

#Menambah data (paling belakang)
asteng.append("Vietnam")
asteng.append("Thailand")

#Menambah data berdasarkan indeks
asteng.insert(3, "Myanmar")
asteng.insert(1, "Malaysia")

#Menghapus data (paling belakang)
asteng.pop()

#Menghapus data berdasarkan indeks
del asteng[3]
del asteng[3]

print(asteng)