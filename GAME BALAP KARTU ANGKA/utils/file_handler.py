def baca_file(nama_file):
    try:
        with open(nama_file, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def tulis_file(nama_file, data):
    with open(nama_file, "w") as file:
        file.writelines(data)

def tambah_file(nama_file, data):
    with open(nama_file, "a") as file:
        file.write(data)