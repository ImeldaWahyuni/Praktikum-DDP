class Warung:
    nama = ""
    uang = 0

    def __init__(self,nama,uang):
        self.nama = nama
        self.uang = uang

    def beli(self,biaya):
        self.uang -= biaya