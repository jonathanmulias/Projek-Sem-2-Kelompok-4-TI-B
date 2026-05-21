def skor(gmail_login):
    with open("penyimpanan.txt", "r") as f:
        data = f.readlines()

    data_baru = []
    skor_baru = 1
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail_file = data[i].split(":")[1].strip()
            data_baru.append(data[i])
            data_baru.append(data[i + 1])

            if gmail_login == gmail_file:
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    skor_lama = int(data[i + 2].split(":")[1])
                    skor_baru = skor_lama + 1
                    data_baru.append(f"Skor : {skor_baru}\n")
                    i += 3

                else:
                    data_baru.append("Skor : 1\n")
                    skor_baru = 1
                    i += 2

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

def leaderboard():
    try:
        with open("penyimpanan.txt", "r") as f:
            data = f.readlines()
    except FileNotFoundError:
        print("\nBelum ada data!")
        return

    data_pemain = []
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail = data[i].split(":")[1].strip()
            nama = gmail.split("@")[0]
            skor = 0
            if i + 2 < len(data) and "Skor :" in data[i + 2]:
                skor = int(data[i + 2].split(":")[1])
            data_pemain.append([nama, skor])
        i += 1

    for i in range(len(data_pemain)):
        for j in range(len(data_pemain) - 1 - i):
            if data_pemain[j][1] < data_pemain[j + 1][1]:
                sementara = data_pemain[j]
                data_pemain[j] = data_pemain[j + 1]
                data_pemain[j + 1] = sementara

    print("\n===== LEADERBOARD =====")
    ranking = 1
    for pemain in data_pemain:
        print(f"{ranking}. {pemain[0]} - {pemain[1]} kemenangan")
        ranking += 1