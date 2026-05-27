from user.akun import cek_login

def login():
    gmail = input("Masukkan Gmail : ")
    password = input("Masukkan Password : ")
    berhasil = cek_login(gmail, password)

    if berhasil:
        nama = gmail.split("@")[0]
        print(f"\nSelamat Datang {nama}!")
        return gmail
    print("\nGmail atau Password salah!")
    return None