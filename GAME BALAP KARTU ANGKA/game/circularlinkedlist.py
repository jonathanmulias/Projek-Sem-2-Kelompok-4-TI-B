import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
        self.jumlah = 0
        self.terpakai = 0

    def buat_kartu(self, data):
        prev = None
        for angka in data:
            node_baru = Node(angka)
            if self.head is None:
                self.head = node_baru
            else:
                prev.next = node_baru
            prev = node_baru
            self.jumlah += 1

        # node terakhir menunjuk ke head
        prev.next = self.head
        self.current = self.head

    def ambil(self, angka):
        if self.current is None:
            return False
        temp = self.current

        for _ in range(self.jumlah):
            if temp.data == angka:
                temp.data = None
                self.terpakai += 1
                return True
            temp = temp.next
        return False

    def tersedia(self, angka):
        temp = self.head
        for _ in range(self.jumlah):
            if temp.data == angka:
                return True
            temp = temp.next
        return False

    def tampilkan(self):
        hasil = []
        temp = self.head
        for _ in range(self.jumlah):
            if temp.data is not None:
                hasil.append(temp.data)
            temp = temp.next
        return hasil

    def reset(self):
        data_awal = [1, 2, 3, 4, 5, 6]
        temp = self.head
        for angka in data_awal:
            temp.data = angka
            temp = temp.next
        self.terpakai = 0