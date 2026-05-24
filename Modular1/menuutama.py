from user.login import login
from user.register import register
from user.leaderboard import leaderboard

from game.game import mulai_game

from utils.validator import input_angka

def menu_utama():
    while True:
        print("\n=================================")
        print("      GAME SUIT BALAP KARTU      ")
        print("=================================")
        print("1. LOGIN & MAIN")
        print("2. REGISTER")
        print("3. LEADERBOARD")
        print("4. KELUAR")
        print("=================================")

        pilihan = input_angka("Masukkan pilihan : ")

        if pilihan == 1:
            gmail_login = login()
            if gmail_login:
                mulai_game(gmail_login)
        elif pilihan == 2:
            register()
        elif pilihan == 3:
            leaderboard()
        elif pilihan == 4:
            print("\nTerima kasih telah bermain!")
            break
        else:
            print("\nPilihan tidak tersedia!")