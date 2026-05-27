class Node:
    def __init__(self, history):
        self.history = history
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.current = None
    
    # Tambah History
    def tambah_history(self, hasil):
        node_baru = Node(hasil)

        # JIKA KOSONG
        if self.head is None:
            self.head = node_baru
            self.current = node_baru

        else:
            bantu = self.head
            while bantu.next is not None:
                bantu = bantu.next
            bantu.next = node_baru
            node_baru.prev = bantu

    # Tampilkan History Sekarang
    def tampilkan_current(self):
        if self.current is not None:
            print(f"\nHistory sekarang : {self.current.history}")
        else:
            print("History kosong")

    # Next History
    def next_history(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next
            self.tampilkan_current()
        else:
            print("Tidak ada history berikutnya")

    # Previous History
    def prev_history(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev
            self.tampilkan_current()
        else:
            print("Tidak ada history sebelumnya")