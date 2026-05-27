from utils.file_handler import baca_file

def gmail_sudah_ada(gmail):
    data = baca_file("data/penyimpanan.txt")
    for line in data:
        if gmail in line:
            return True
    return False

def cek_login(gmail, password):
    data = baca_file("data/penyimpanan.txt")
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail_file = data[i].split(":")[1].strip()
            if i + 1 < len(data):
                password_file = data[i + 1].split(":")[1].strip()
                if gmail == gmail_file and password == password_file:
                    return True
        i += 1
    return False