import random
from constantes import EMOJIS

def criar_tabuleiro(grid):
    total = grid[0] * grid[1]
    assert total % 2 == 0, "O número de cartas precisa ser par!"

    num_pares = total // 2
    emojis_usados = random.sample(EMOJIS, num_pares)
    cartas = emojis_usados * 2
    random.shuffle(cartas)

    tabuleiro = [cartas[i:i + grid[0]] for i in range(0, total, grid[0])]
    visivel = [[False] * grid[0] for _ in range(grid[1])]
    encontradas = [[False] * grid[0] for _ in range(grid[1])]
    return tabuleiro, visivel, encontradas, {}
