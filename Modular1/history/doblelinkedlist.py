# node untuk menyimpan histori
class Node:

    def __init__(dataGame, isiHistory):

        dataGame.isiHistory = isiHistory    # menyimpan isi histori
        dataGame.next = None                # penghubung ke node berikutnya
        dataGame.prev = None                # penghubung ke node sebelumnya


# double linked list
class DoubleLinkedList:

    def __init__(game):
        game.awal = None                    # node awal
        game.akhir = None                   # node akhir

    # tambah histori
    def tambah_history(game, hasilGame):
        rondeBaru = Node(hasilGame)            # membuat node baru

        if game.awal == None:                # jika histori kosong

            game.awal = rondeBaru          # node baru jadi awal dan akhir
            game.akhir = rondeBaru

        else:
            game.akhir.next = rondeBaru       # hubungkan node akhir ke node baru

            rondeBaru.prev = game.akhir       # hubungkan node baru ke node sebelumnya

            game.akhir = rondeBaru              # pindahkan node akhir

    # tampil histori dari awal
    def tampil_next(game):

        bantu = game.awal                     # mulai dari node awal
        nomor = 1

        print("\nHistory Next")

        # perulangan sampai node habis
        while bantu != None:

            print(str(nomor) + ". " + bantu.isiHistory)

            bantu = bantu.next        # pindah ke node berikutnya
            nomor += 1

    # tampil histori dari akhir
    def tampil_prev(game):

        bantu = game.akhir            # mulai dari node akhir
        nomor = 1

        print("\nHistory Previous")

        # perulangan sampai node habis
        while bantu != None:

            print(str(nomor) + ". " + bantu.isiHistory)
            bantu = bantu.prev     # pindah ke node sebelumnya
            nomor += 1


# object double linked list
history_game = DoubleLinkedList()


# menambahkan histori
history_game.tambah_history("PLAYER MENANG")
history_game.tambah_history("COMPUTER MENANG")
history_game.tambah_history("HASIL SERI")


# tampil dari awal ke akhir
history_game.tampil_next()

# tampil dari akhir ke awal
history_game.tampil_prev()
