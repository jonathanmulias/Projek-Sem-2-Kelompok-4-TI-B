from game.jalur import cek_menang

def mainkan_ronde(player, komputer):
    if player == komputer:
        return "SERI"
    if cek_menang(player, komputer):
        return "PLAYER"
    return "KOMPUTER"