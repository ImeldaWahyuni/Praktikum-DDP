# negara = {"Azerbaijan","Armenia","Turki","Azebaijan"}

# print(negara)

himpunan1 = {1,2,3,5}
himpunan2 = {1,2,4,6}

#add itu untuk menambahkan  (menambahkan data)
himpunan1.add("enam")
himpunan2.add("enam")

#update itu menambahkan lebih dari satu value (Menambahkan data lebih dari satu)
himpunan1.update([7,8])
himpunan2.update([8,9])

#remove untuk menghapus value(data)
himpunan1.remove("enam")
himpunan2.remove("enam")
print(himpunan1, himpunan2)

#operasi irisan
print(himpunan1 & himpunan2)

#operasi union
print(himpunan1 | himpunan2)
