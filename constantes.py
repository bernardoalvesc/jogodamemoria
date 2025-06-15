# constantes.py

import pygame

# Tela
TAMANHO_TELA = (1000, 800)
TAMANHO_CARTA = (100, 100)
MARGEM = 20

# FPS
FPS = 60

# Emojis
EMOJIS = [
    '🍎', '🍇', '🐱', '🐶',
    '🌊', '⭐', '🚀', '☀️',
    '🌸', '🌼', '🍄', '🍓',
    '💜', '💛', '💙', '💚',
    '🦋', '🐸', '🧊', '🧠'
]

# Fontes
pygame.font.init()
FONT_EMOJI = pygame.font.SysFont('Segoe UI Emoji', 64)
FONT_HUD = pygame.font.SysFont('Arial', 24, bold=True)
FONT_END = pygame.font.SysFont('Arial', 48, bold=True)
FONT_MENU = pygame.font.SysFont('Arial', 36)

# Cores
COR_FUNDO = (18, 18, 18)
COR_CARTA_FECHADA = (50, 50, 50)
COR_CARTA_ABERTA = (80, 80, 80)
COR_TEXTO = (240, 240, 240)
COR_HUD = (200, 200, 200)
COR_VITORIA = (255, 215, 0)
COR_BOTAO = (70, 70, 70)
COR_BOTAO_HOVER = (100, 100, 100)
COR_BORDA = (130, 130, 130)
