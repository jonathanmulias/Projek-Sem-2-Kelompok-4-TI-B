class Stack:
    def __init__(self):
        self.data = []

    def push(self, player, komputer, player_pos, komputer_pos):
        histori = (
            f"Player memilih : {player}, "
            f"Posisi Player : {player_pos}, "
            f"Computer memilih : {komputer}, "
            f"Posisi Computer : {komputer_pos}"
        )

        self.data.append(histori)

    def tampilkan(self):
        print("\n===== HISTORI STACK =====")
        if len(self.data) == 0:
            print("Belum ada histori")
        else:
            for item in reversed(self.data):
                print(item)