class HashTable:
    def __init__(self):
        self.data = {}

    def tambah_data(self, nama, skor):
        self.data[nama] = skor

    def cari_data(self, nama):
        if nama in self.data:
            return self.data[nama]
        else:
            return None

    def tampilkan(self):
        for nama in self.data:
            print(f"{nama} : {self.data[nama]}")