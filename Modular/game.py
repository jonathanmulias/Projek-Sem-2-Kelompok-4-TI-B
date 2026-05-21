import random

from jalur import cek_menang
from jalur import tampilkan_jalur
from jalur import PANJANG_JALUR
from leaderboard import skor
from leaderboard import leaderboard
from history import simpan_history
from history import lihat_history
from stack import push_stack
from stack import lihat_stack


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

            if player == 0:
                lihat_stack()
                continue

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

        old_player = player_pos
        old_komputer = komputer_pos

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
            
        push_stack(player, komputer, old_player, old_komputer)

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

        # =========================
        # MENU AKHIR GAME
        # =========================
            
        if game_selesai:
            while True:
                print("\n1. Main Lagi")
                print("2. Leaderboard")
                print("3. Lihat History")
                print("4. Kembali ke Menu")

                try:
                    pilihan = int(input("Masukkan pilihan : "))
                except ValueError:
                    print("Input harus angka!")
                    continue

                # =========================
                # MAIN LAGI
                # =========================
                if pilihan == 1:

                    player_pos = 0
                    komputer_pos = 0

                    kartu_player = [1,2,3,4,5,6]
                    kartu_komputer = [1,2,3,4,5,6]

                    print("\nGAME DIMULAI ULANG!")

                    break

                # =========================
                # LEADERBOARD
                # =========================
                elif pilihan == 2:
                    leaderboard()

                # =========================
                # HISTORY
                # =========================
                elif pilihan == 3:
                    lihat_history()

                # =========================
                # KEMBALI KE MENU
                # =========================
                elif pilihan == 4:
                    return

                else:
                    print("Pilihan tidak tersedia!")
