from utils.constants import JUMLAH_KARTU

class Kartu:
    def __init__(self):
        self.kartu = []
        self.reset()

    def tampilkan(self):
        return self.kartu.copy()

    def tersedia(self, angka):
        return angka in self.kartu

    def gunakan(self, angka):
        if angka in self.kartu:
            self.kartu.remove(angka)

    def reset(self):
        self.kartu = []
        for i in range(1, JUMLAH_KARTU + 1):
            self.kartu.append(i)