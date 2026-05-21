import random

from jalur import cek_menang
from jalur import tampilkan_jalur
from jalur import PANJANG_JALUR
from leaderboard import skor
from leaderboard import leaderboard

def mulai_game(gmail_login):
    player_pos = 0
    komputer_pos = 0
    kartu_player = [1,2,3,4,5,6]
    kartu_komputer = [1,2,3,4,5,6]

    while True:
        print("\nPLAYER")
        tampilkan_jalur(player_pos, "P")

        print("\nCOMPUTER")
        tampilkan_jalur(komputer_pos, "C")

        print(f"\nKartu tersedia : {kartu_player}")

        try:
            player = int(input("\nMasukkan angka : "))

            if player not in kartu_player:
                print("Angka tidak tersedia!")
                continue

        except ValueError:
            print("Input harus angka!")
            continue

        komputer = random.choice(kartu_komputer)

        print(f"Computer memilih : {komputer}")

        kartu_player.remove(player)
        kartu_komputer.remove(komputer)

        if player == komputer:
            print("\nHASIL SERI!")
        elif cek_menang(player, komputer):
            print("\nPLAYER MENANG!")
            print(f"Maju {player} langkah!")
            player_pos += player
        else:
            print("\nCOMPUTER MENANG!")
            print(f"Maju {komputer} langkah!")
            komputer_pos += komputer

        if player_pos > PANJANG_JALUR:
            player_pos = PANJANG_JALUR

        if komputer_pos > PANJANG_JALUR:
            komputer_pos = PANJANG_JALUR

        if len(kartu_player) == 0:
            kartu_player = [1,2,3,4,5,6]
            print("\nKartu PLAYER di-reset!")

        if len(kartu_komputer) == 0:
            kartu_komputer = [1,2,3,4,5,6]
            print("Kartu COMPUTER di-reset!")

        if player_pos >= PANJANG_JALUR:
            print("\nPLAYER MENANG GAME!")
            hasil_skor = skor(gmail_login)
            print(f"SKOR KAMU : {hasil_skor}")

            print("\n1. Main Lagi")
            print("2. Leaderboard")
            print("3. Kembali ke Menu")

            pilihan = int(input("Masukkan pilihan : "))

            if pilihan == 1:
                player_pos = 0
                komputer_pos = 0
                kartu_player = [1,2,3,4,5,6]
                kartu_komputer = [1,2,3,4,5,6]
                print("\nGAME DIMULAI ULANG!")
            elif pilihan == 2:
                leaderboard()
                break
            elif pilihan == 3:
                break