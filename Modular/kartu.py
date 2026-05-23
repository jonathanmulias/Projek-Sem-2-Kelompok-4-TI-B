class Kartu:
    def __init__(self):
        self.kartu = [1, 2, 3, 4, 5, 6]

    def tampilkan(self):
        return self.kartu

    def tersedia(self, angka):
        return angka in self.kartu

    def gunakan(self, angka):
        self.kartu.remove(angka)

    def reset(self):
        self.kartu = [1, 2, 3, 4, 5, 6]
