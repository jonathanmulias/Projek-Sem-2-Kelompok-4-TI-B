from login import login_register
from game import mulai_game
from leaderboard import leaderboard

def menu_utama():
    while True:
        print("\n=================================")
        print("      GAME SUIT BALAP KARTU      ")
        print("=================================")
        print("1. LOGIN & MAIN")
        print("2. LEADERBOARD")
        print("3. KELUAR")
        print("=================================")

        pilihan = int(input("Masukkan pilihan : "))

        if pilihan == 1:
            gmail_login = login_register()
            if gmail_login:
                mulai_game(gmail_login)

        elif pilihan == 2:
            leaderboard()

        elif pilihan == 3:
            print("\nTerima kasih sudah bermain!")
            break

        else:
            print("\nPilihan tidak tersedia!")

menu_utama()
