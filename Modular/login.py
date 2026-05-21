def login_register():
    while True:
        print("=================================")
        print("   GAME SUIT BALAP KARTU ANGKA   ")
        print("1. LOGIN    >>                   ")
        print("2. REGISTER >>                   ")
        print("=================================")

        print("jika anda belum memiliki akun silahkan REGISTRASI terlebih dahulu")

        try:
            menu = int(input("Masukkan Pilihan anda : "))        
        except ValueError:
            print("Input harus angka!")
            continue

        if menu == 1:
            gmail = input("Masukkan Gmail Anda : ")
            nama = gmail.split("@")[0]
            password = input("Masukkan Password Anda : ")
            try:
                with open("penyimpanan.txt", "r") as f:
                    data = f.readlines()
            except FileNotFoundError:
                print("\nBelum ada akun yang terdaftar!")
                continue
            login_berhasil = False
            i = 0

            while i < len(data):
                if "Gmail :" in data[i]:
                    gmail_file = data[i].split(":")[1].strip()
                    password_file = data[i + 1].split(":")[1].strip()
                    if gmail == gmail_file and password == password_file:
                        login_berhasil = True
                        break
                i += 1

            if login_berhasil:
                print(f"\nSelamat Datang {nama}...")
                return gmail
            else:
                print("\nGmail atau Password salah!")
                print("Silahkan coba lagi.\n")

        elif menu == 2:
            gmail = input("Masukkan Gmail yang ingin didaftarkan : ")
            password = input("Masukkan Password : ")

            with open("penyimpanan.txt", "a") as f:
                f.write("Gmail : " + gmail + "\n" + "Password : " + password + "\n")

            print("\nREGISTER berhasil!")
            print("Silahkan LOGIN terlebih dahulu.\n")
        else:
            print("\nMenu tidak tersedia!")
