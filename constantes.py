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
    '💜', '💛', '💙', '💚'
]

# Fontes
pygame.font.init()
FONT_EMOJI = pygame.font.SysFont('Segoe UI Emoji', 64)
FONT_HUD = pygame.font.SysFont('Arial', 24)
FONT_END = pygame.font.SysFont('Arial', 48)
FONT_MENU = pygame.font.SysFont('Arial', 36)

# Cores
COR_FUNDO = (30, 30, 30)
COR_CARTA_FECHADA = (80, 80, 80)
COR_CARTA_ABERTA = (50, 50, 50)
COR_TEXTO = (255, 255, 255)
COR_HUD = (200, 200, 200)
COR_VITORIA = (255, 215, 0)
COR_BOTAO = (70, 70, 70)
COR_BOTAO_HOVER = (100, 100, 100)

# Sons
pygame.mixer.init()
SOUND_CLICK = pygame.mixer.Sound('sounds/click.wav')
SOUND_MATCH = pygame.mixer.Sound('sounds/match.wav')
SOUND_WIN = pygame.mixer.Sound('sounds/win.wav')
