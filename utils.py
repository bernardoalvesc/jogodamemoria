# utils.py

import random
from constantes import EMOJIS

def criar_tabuleiro(grid):
    num_pares = (grid[0] * grid[1]) // 2
    cartas = EMOJIS[:num_pares] * 2
    random.shuffle(cartas)
    tabuleiro = [cartas[i:i+grid[0]] for i in range(0, len(cartas), grid[0])]
    visivel = [[False]*grid[0] for _ in range(grid[1])]
    encontradas = [[False]*grid[0] for _ in range(grid[1])]
    cpu_memoria = {}
    return tabuleiro, visivel, encontradas, cpu_memoria
