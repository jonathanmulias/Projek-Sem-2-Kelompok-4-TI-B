from utils.file_handler import baca_file, tulis_file

def tambah_skor(gmail_login):
    data = baca_file("data/penyimpanan.txt")
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
                    i += 2
            else:
                if i + 2 < len(data) and "Skor :" in data[i + 2]:
                    data_baru.append(data[i + 2])
                    i += 3
                else:
                    i += 2
        else:
            i += 1

    tulis_file("data/penyimpanan.txt", data_baru)
    return skor_baru


def leaderboard():
    data = baca_file("data/penyimpanan.txt")
    if len(data) == 0:
        print("\nBelum ada data!")
        return

    pemain = []
    i = 0

    while i < len(data):
        if "Gmail :" in data[i]:
            gmail = data[i].split(":")[1].strip()
            nama = gmail.split("@")[0]
            skor = 0

            if i + 2 < len(data) and "Skor :" in data[i + 2]:
                skor = int(data[i + 2].split(":")[1])
            pemain.append([nama, skor])
        i += 1

    pemain.sort(
        key=lambda item: item[1],
        reverse=True
    )

    print("\n===== LEADERBOARD =====")
    ranking = 1

    for item in pemain:
        print(f"{ranking}. {item[0]} - {item[1]} kemenangan")
        ranking += 1