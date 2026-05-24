class Node:
    def __init__(dataGame,isiHistory):
        dataGame.isiHistory = isiHistory   # # menyimpan isi histori
        dataGame.sambung = None   # penghubung ke node berikutnya



class SingleLinkedList:
    def __init__(game):
         game.awal = None     # histori awal masih kosong

    def tambah_history(game, hasilGame):  # tambah histori permainan

        rondeBaru = Node(hasilGame)    # membuat node baru

        if game.awal == None:       # jika history kosong
            game.awal= rondeBaru     #node baru menjadi history pertama

        else:
            bantu = game.awal    #mulai dari node pertama
            while bantu.sambung != None:    #mencari node terakhri
                bantu = bantu.sambung

            bantu.sambung = rondeBaru  #menyambungkan node terakhir dengan node baru

    # tampilkan histori permainan
    def tampilkan_history(game):

        bantu = game.awal
        nomor = 1

    # jika histori kosong
        if game.awal == None:

            print("Histori kosong")

        else:
            while bantu != None:
                print(str(nomor) + ". " + bantu.isiHistory)
                bantu = bantu.sambung
                nomor += 1


# =========================
# objek SINGLE LINKED LIST
# =========================

history_game = SingleLinkedList()


#===========================
#MENAMBAHKAN HISTORI GAME
#===========================

history_game.tambah_history("PLAYER MENANG")
history_game.tambah_history("COMPUTER MENANG")
history_game.tambah_history("HASIL SERI")


#==========================
#MENAMPILKAN HISTORI
#==========================
print("HISTORI PERMAINAN :")
history_game.tampilkan_history()
