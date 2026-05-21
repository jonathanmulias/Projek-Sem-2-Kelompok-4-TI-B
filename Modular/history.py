def cari_skor():
    cari_nama = input("Masukkan nama yang ingin di cari skor nya : ")
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
                    print(f"\n{nama} : {skor} Kemenangan")
                else:
                    print(f"\n{nama} : {skor} Kemenangan")
                break
        i += 1

    if ditemukan == False:
        print("\nNama tidak ditemukan!")

def lihat_history():
    try:
        with open("history.txt", "r") as f:
            data = f.readlines()

        print("\n===== HISTORY =====")

        for i in range(len(data)):
            print(f"{i+1}. {data[i].strip()}")

    except FileNotFoundError:
        print("Belum ada history!")

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
