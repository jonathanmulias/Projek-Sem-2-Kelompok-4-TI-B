from utils.constants import PANJANG_JALUR

def tampilkan_jalur(posisi, simbol):
    kiri = "=" * posisi
    kanan = "=" * (PANJANG_JALUR - posisi)
    print(f"{kiri}{simbol}{kanan}")

def cek_menang(player, komputer):
    if player == 1 and komputer == 6:
        return True
    if player == 6 and komputer == 1:
        return False
    return player > komputer