from user.login import login
from user.register import register
from user.leaderboard import leaderboard
from history.singlelinkedlist import SingleLinkedList
from history.doublelinkedlist import DoubleLinkedList

history_game = SingleLinkedList()
history_double = DoubleLinkedList()

from game.game import mulai_game

from utils.validator import input_angka

def menu_utama():
    while True:
        print("\n======================================")
        print("        GAME SUIT BALAP KARTU         ")
        print(" ----- ----- ----- ----- ----- -----  ")
        print(" | 1 | | 2 | | 3 | | 4 | | 5 | | 6 |  ")
        print(" ----- ----- ----- ----- ----- -----  ")
        print("======================================")
        print("1. LOGIN & MAIN")
        print("2. REGISTER")
        print("3. LEADERBOARD")
        print("4. RIWAYAT HISTORY")
        print("5. NAVIGASI HISTORY ")
        print("6. KELUAR")
        print("======================================")

        print("\nSILAHKAN REGISTER TERLEBIH DAHULU JIKA BELUM MENDAFTARKAN AKUN!")

        pilihan = input_angka("Masukkan pilihan : ")

        if pilihan == 1:
            gmail_login = login()
            if gmail_login:
                mulai_game(gmail_login, history_game, history_double)

        elif pilihan == 2:
            register()

        elif pilihan == 3:
            leaderboard()

        elif pilihan == 4:
            print("\n========== HASIL PEMILIHAN KARTU ===========")
            print("===== (pada satu permainan sebelumnya) =====\n")
            history_game.tampilkan_history()

        elif pilihan == 5:
            while True:
                print("\n===== DOUBLE LINKED LIST =====")
                print("1. Lihat History Sekarang")
                print("2. Next History")
                print("3. Previous History")
                print("4. Kembali")

                pilih = input("Masukkan pilihan : ")

                if pilih == "1":
                    history_double.tampilkan_current()
                elif pilih == "2":
                    history_double.next_history()
                elif pilih == "3":
                    history_double.prev_history()
                elif pilih == "4":
                    break
                else:
                    print("Pilihan tidak tersedia!")

        elif pilihan == 6:
            print("\nTerima kasih telah bermain!")
            break

        else:
            print("\nPilihan tidak tersedia!")