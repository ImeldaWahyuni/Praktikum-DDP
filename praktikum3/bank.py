class Bank:
    nama =""
    norek = ""
    saldo = 0

    def __init__(self, nama,norek,saldo):
        self.nama = nama
        self.norek = norek
        self.saldo = saldo
    
    def withdrawal(self,uang):
        self.saldo -= uang

    def deposit(self,uang):
        self.saldo += uang

    def cetak(self):
        print("------------------")
        print("Nama\t:", self.nama)
        print("No Rekening\t:", self.norek)
        print("Saldo\t:", self.saldo)
        print("------------------")

nasabah = Bank("Bambang Pamungkas","0983675728", 9000000)
nasabah.cetak()
nasabah.deposit(1000000)
nasabah.withdrawal(1000000)
nasabah.cetak()
