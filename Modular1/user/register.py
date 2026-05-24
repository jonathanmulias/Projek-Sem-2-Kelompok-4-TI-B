from utils.file_handler import tambah_file
from user.akun import gmail_sudah_ada

def register():
    gmail = input("Masukkan Gmail : ")
    if gmail_sudah_ada(gmail):
        print("\nGmail sudah terdaftar!")
        return

    password = input("Masukkan Password : ")

    if len(password) < 6:
        print("Password minimal 6 karakter!")
        return

    data = (
        f"Gmail : {gmail}\n"
        f"Password : {password}\n"
    )

    tambah_file("data/penyimpanan.txt", data)
    print("\nREGISTER berhasil!")