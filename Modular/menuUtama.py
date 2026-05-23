from login import login_register
from game import mulai_game
from leaderboard import leaderboard

def menu_utama():
    game_berjalan = True
    while game_berjalan:
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
            keluar = input("Anda ingin keluar dari permainan (y/t) : ")
            if keluar == "y":
                game_berjalan = False
                exit()
            elif keluar == "t":
                continue

        else:
            print("\nPilihan tidak tersedia!")

menu_utama()
