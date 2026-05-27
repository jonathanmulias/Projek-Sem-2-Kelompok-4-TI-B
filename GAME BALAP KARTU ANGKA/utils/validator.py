def input_angka(pesan):
    while True:
        try:
            return int(input(pesan))
        except ValueError:
            print("Input harus angka!")