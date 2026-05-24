from utils.file_handler import baca_file, tulis_file
from utils.constants import BATAS_HISTORY

def lihat_history():
    data = baca_file("data/history.txt")
    if len(data) == 0:
        print("\nBelum ada history!")
        return

    print("\n===== HISTORY =====")
    nomor = 1

    for item in data:
        print(f"{nomor}. {item.strip()}")
        nomor += 1

def simpan_history(hasil):
    data = baca_file("data/history.txt")
    data.append(hasil + "\n")
    data = data[-BATAS_HISTORY:]
    tulis_file("data/history.txt", data)