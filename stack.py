stack_history = []

def push_stack(player, computer, player_pos, komputer_pos):
    stack_history.append(f"Player memilih kartu : {player} Player maju : {player_pos}, Komputer memilih Kartu : {computer} Komputer maju : {komputer_pos}")

def lihat_stack():
    print("\n===== HISTORI STACK =====")

    if len(stack_history) == 0:
        print("Belum ada histori")
    else:
        for data in reversed(stack_history):
            print(data)
