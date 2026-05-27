from game.circularlinkedlist import CircularLinkedList

class Kartu:
    def __init__(self):
        self.kartu = CircularLinkedList()
        self.kartu.buat_kartu([1,2,3,4,5,6])

    def tampilkan(self):
        return self.kartu.tampilkan()

    def tersedia(self, angka):
        return self.kartu.tersedia(angka)

    def gunakan(self, angka):
        self.kartu.ambil(angka)

    def reset(self):
        self.kartu.reset()