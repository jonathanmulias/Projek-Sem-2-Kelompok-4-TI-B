class Node:
    def __init__(self, isiHistory):
        self.isiHistory = isiHistory
        self.sambung = None

class SingleLinkedList:
    def __init__(self):
        self.awal = None
    
    def tambah_history(self, hasilGame):
        rondeBaru = Node(hasilGame)
        if self.awal is None:
            self.awal = rondeBaru
        else:
            bantu = self.awal
            while bantu.sambung is not None:
                bantu = bantu.sambung
            bantu.sambung = rondeBaru

    def tampilkan_history(self):
        bantu = self.awal
        nomor = 1
        if self.awal is None:
            print("History kosong")
        else:
            while bantu is not None:
                print(f"{nomor}. {bantu.isiHistory}")
                bantu = bantu.sambung
                nomor += 1