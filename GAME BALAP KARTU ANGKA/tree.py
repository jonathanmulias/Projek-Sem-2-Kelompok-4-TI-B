class TreeNode:
    def __init__(self, data):
        self.data = data
        self.cabang = []

    def tambah_bagian(self, bagian):
        self.cabang.append(bagian)

    def tampilkan(self, level=0):
        indent = "   " * level
        print(indent + self.data)

        for bagian in self.cabang:
            bagian.tampilkan(level + 1)