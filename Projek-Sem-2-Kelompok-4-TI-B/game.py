import random

# =========================
# DATA GAME
# =========================
PANJANG_JALUR = 35 #panjang kotak jalurnya adalah 35

player_pos = 0 #player dimulai dari baris paling pertama (yaitu indeks ke 0)
komputer_pos = 0 #komper dimulai dari baris paling pertama (yaitu indeks ke 0)

# angka tersedia
kartu_player = [1, 2, 3, 4, 5, 6] #kartu player itu dimulai dari angka 1 - 6
kartu_komputer = [1, 2, 3, 4, 5, 6] #kartu komputer itu dimulai dari angka 1 - 6

# =========================
# FUNCTION LOGIN
# =========================
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

        # =========================
        # PROSES LOGIN
        # =========================
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

                # ambil gmail di file
                if "Gmail :" in data[i]:
                    gmail_file = data[i].split(":")[1].strip()

                    # ambil password di bawahnya
                    password_file = data[i + 1].split(":")[1].strip()

                    # cek cocok atau tidak
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

        # =========================
        # PROSES REGISTER
        # =========================
        elif menu == 2:

            gmail = input("Masukkan Gmail yang ingin didaftarkan : ")
            password = input("Masukkan Password : ")

            with open("penyimpanan.txt", "a") as f:
                f.write("Gmail : " + gmail + "\n" + "Password : " + password + "\n")

            print("\nREGISTER berhasil!")
            print("Silahkan LOGIN terlebih dahulu.\n")

        else:
            print("\nMenu tidak tersedia!")

# =========================
# FUNCTION CEK MENANG
# =========================
def cek_menang(player, komputer): #fungsi dengan nama "cek_menang" yang menerima variabel "player" dan "komputer"

    # aturan khusus
    if player == 1 and komputer == 6: #jika player memilih kartu 1 dan komputer memilih kartu 6
        return True #maka benar atau player menang

    # aturan khusus kebalikannya
    if player == 6 and komputer == 1: #jika player memilih kartu 6 dan komputer memilih kartu 1
        return False #maka salah atau player kalah
 
    # selain itu angka terbesar menang
    return player > komputer #simpan kartu player jika lebih besar dari komputer (player menang) atau simpan kartu player jika lebih kecil dari komputer (player kalah)

# =========================
# FUNCTION TAMPILKAN JALUR
# =========================
def tampilkan_jalur(posisi, simbol): #fungsi dengan nama "tampilkan_jalur" yang menerima variabel "posisi" dan "simbol"
    kiri = "=" * posisi #variabel "kiri" akan menyimpan tanda "=" sebanyak nilai posisi, misalnya posisi = 5,  maka hasilnya "====="
    kanan = "=" * (PANJANG_JALUR - posisi) #variabel "kanan" akan menyimpan sisa "=", panjang jalur dikurangi posisi player/komputer
    print(f"{kiri}{simbol}{kanan}") #menampilkan jalur game, kiri + simbol player/computer + kanan

# =========================
# FUNCTION SKOR
# =========================
def skor(gmail_login):
    with open("penyimpanan.txt", "r") as f:
        data = f.readlines()

    data_baru = []
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail_file = data[i].split(":")[1].strip()
            data_baru.append(data[i])
            data_baru.append(data[i + 1])

            # =========================
            # JIKA USER YANG LOGIN
            # =========================
            if gmail_login == gmail_file:
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    skor_lama = int(data[i + 2].split(":")[1])
                    skor_baru = skor_lama + 1
                    data_baru.append(f"Skor : {skor_baru}\n")
                    i += 3
                else:
                    skor_baru = 1
                    data_baru.append(f"Skor : {skor_baru}\n")
                    i += 2

            # =========================
            # USER LAIN
            # =========================
            else:
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    data_baru.append(data[i + 2])
                    i += 3
                else:
                    i += 2

        else:
            i += 1

    with open("penyimpanan.txt", "w") as f:
        f.writelines(data_baru)

    return skor_baru

# =========================
# FUNCTION LEADERBOARD
# =========================
def leaderboard():
    while True:     
        data_pemain = []

        # baca file
        with open("penyimpanan.txt", "r") as f:
            data = f.readlines()

        i = 0

        while i < len(data):
            # cek gmail
            if "Gmail :" in data[i]:
                gmail = data[i].split(":")[1].strip()
                nama = gmail.split("@")[0]
                skor = 0

                # cek apakah ada skor
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    skor = int(data[i + 2].split(":")[1])

                # simpan ke list
                data_pemain.append([nama, skor])

            i += 1

        #=========================
        #BUBBLE SORT
        #=========================
        for i in range(len(data_pemain)):
            for j in range(len(data_pemain) - 1 - i):
                if data_pemain[j][1] < data_pemain[j + 1][1]:
                    sementara = data_pemain[j]
                    data_pemain[j] = data_pemain[j + 1]
                    data_pemain[j + 1] = sementara

        # =========================
        # TAMPILKAN LEADERBOARD
        # =========================
        print("\n===== LEADERBOARD =====")

        ranking = 1

        for pemain in data_pemain:
            print(f"{ranking}. {pemain[0]} - {pemain[1]} kemenangan")
            ranking += 1

        print("\n1. Cari skor berdasarkan nama")
        print("2. Kembali")

        pilihan = input("Masukkan pilihan : ")

        if pilihan == "1":
            cari_skor()
        elif pilihan == "2":
            return
        else:
            print("Pilihan tidak tersedia!")

# =========================
# MENCARI SKOR BERDASARKAN NAMA
# =========================
def cari_skor():
    cari_nama = input("Masukkan nama yang ingin di cari skor nya: ")
    with open("penyimpanan.txt", "r") as f:
        data = f.readlines()

    ditemukan = False
    i = 0
    
    # cek gmail
    while i < len(data):
        if "Gmail :" in data[i]:
            gmail = data[i].split(":")[1].strip()
            # ambil nama dari gmail
            nama = gmail.split("@")[0]
            # cek apakah nama cocok
            if cari_nama == nama:
                ditemukan = True
                # cek apakah ada skor
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    skor = data[i + 2].split(":")[1].strip()
                    print(f"\n{nama} : {skor}")
                else:
                    print(f"\n{nama} : {skor}")
                break
        i += 1

    if ditemukan == False:
        print("\nNama tidak ditemukan!")

# =========================
# SIMPAN HISTORY
# =========================
def simpan_history(hasil):

    # baca history lama
    try:
        with open("history.txt", "r") as f:
            data = f.readlines()

    except FileNotFoundError:
        data = []

    # tambah hasil baru
    data.append(hasil + "\n")

    # ambil 6 data terakhir saja
    data = data[-6:]

    # simpan kembali
    with open("history.txt", "w") as f:
        f.writelines(data)

# =========================
# FUNCTION TAMPILKAN HISTORY
# =========================
def tampil_history(data, index=0): #fungsi dengan nama "tampil_history" yang menerima variabel "data" dan "index"
    
    # kondisi berhenti rekursif
    if index >= len(data): #jika nilai index lebih besar atau sama dengan jumlah data history
        return #maka function berhenti

    # tampilkan history
    print(f"{index + 1}. {data[index].strip()}") 
    # index + 1 digunakan agar nomor dimulai dari 1
    # data[index] digunakan untuk mengambil isi list berdasarkan urutan index
    # .strip() digunakan untuk menghapus enter (\n) dari file txt

    # rekursif
    tampil_history(data, index + 1)
    # function memanggil dirinya sendiri
    # index + 1 artinya index akan bertambah 1 setiap pengulangan
    # misalnya:
    # awal index = 0
    # lalu menjadi 1
    # lalu menjadi 2
    # dan seterusnya sampai kondisi berhenti terpenuhi

# =========================
# LIHAT HISTORY
# =========================
def lihat_history():

    try:
        with open("history.txt", "r") as f:
            data = f.readlines()

        print("\n====== 6 HISTORY TERAKHIR ======")

        if len(data) == 0:
            print("Belum ada history")

        else:
            tampil_history(data)

    except FileNotFoundError:
        print("History belum ada!")

    kembali = input("Kembali (y) : ")
    if kembali == "y":
        return
    else:
        print("Pilihan tidak ada")

# =========================
# JIKA SUDAH LOGIN MAKA AKAN MASUK KE GAME NYA
# =========================
gmail_login = login_register()

if gmail_login:
# =========================
# GAME UTAMA
# =========================
    while True:
        # tampilkan jalur
        print("\nPLAYER")
        tampilkan_jalur(player_pos, "P")

        print("\nCOMPUTER")
        tampilkan_jalur(komputer_pos, "C")

        # tampilkan angka tersedia
        print(f"\nAngka tersedia : {kartu_player}")

        # =========================
        # INPUT PLAYER
        # =========================
        try:
            player = int(input("\nMasukkan angka : "))

            # validasi angka tersedia
            if player not in kartu_player:
                print("Angka tidak tersedia atau sudah dipakai!")
                continue

        except ValueError:
            print("Input harus angka!")
            continue

        # =========================
        # PILIHAN COMPUTER
        # =========================
        computer = random.choice(kartu_komputer)

        print(f"Computer memilih : {computer}")

        # hapus angka yang sudah dipakai
        kartu_player.remove(player)
        kartu_komputer.remove(computer)

        # =========================
        # HASIL PERTANDINGAN
        # =========================

        # seri
        if player == computer:

            print("\nHASIL SERI!")

        # player menang
        elif cek_menang(player, computer):

            print(f"\nPLAYER MENANG!")
            print(f"Maju {player} langkah!")

            player_pos += player

        # computer menang
        else:

            print(f"\nCOMPUTER MENANG!")
            print(f"Maju {computer} langkah!")

            komputer_pos += computer

        # =========================
        # BATAS MAKSIMAL
        # =========================
        if player_pos > PANJANG_JALUR:
            player_pos = PANJANG_JALUR

        if komputer_pos > PANJANG_JALUR:
            komputer_pos = PANJANG_JALUR

        # =========================
        # RESET ANGKA JIKA HABIS
        # =========================
        if len(kartu_player) == 0:

            kartu_player = [1, 2, 3, 4, 5, 6]

            print("\nAngka PLAYER di-reset!")

        if len(kartu_komputer) == 0:

            kartu_komputer = [1, 2, 3, 4, 5, 6]

            print("Angka COMPUTER di-reset!")

        # =========================
        # CEK PEMENANG GAME
        # =========================
        game_selesai = False

        if player_pos >= PANJANG_JALUR:
            simpan_history("MENANG")

            print("\nPLAYER MENANG GAME!\n")
            hasil_skor = skor(gmail_login)
            print("SKOR KAMU : ", hasil_skor)
            game_selesai = True

        elif komputer_pos >= PANJANG_JALUR:
            simpan_history("KALAH")

            print("\nKOMPUTER MENANG GAME")
            game_selesai = True

        if game_selesai:
            game_berjalan = True
            while game_berjalan:
                print("\n1. Main Lagi")
                print("2. Lihat Leaderboard")
                print("3. Lihat Histori")
                print("4. Keluar")

                pilihan = input("Masukkan pilihan : ")

                if pilihan == "1":
                    # reset posisi
                    player_pos = 0
                    komputer_pos = 0

                    # reset kartu
                    kartu_player = [1, 2, 3, 4, 5, 6]
                    kartu_komputer = [1, 2, 3, 4, 5, 6]

                    print("\nGAME DIMULAI ULANG!")
                    continue

                elif pilihan == "2":
                    leaderboard()

                elif pilihan == "3":
                    lihat_history()
                    
                elif pilihan == "4":
                    keluar = input("Anda ingin keluar dari permainan (y/t) : ")
                    if keluar == "y":
                        game_berjalan = False
                        exit()
                    elif keluar == "t":
                        continue