import pygame

pygame.init()
info = pygame.display.Info()
TAMANHO_TELA = (info.current_w, info.current_h)
TAMANHO_CARTA = (100, 100)
MARGEM = 20
FPS = 60

EMOJIS = [
    '🍕', '🍦', '🍭', '🎮', '🐱', '🐶', '🧸', '🐸',
    '🚀', '🌈', '⚽', '🎲', '🧁', '🎈', '👾', '⭐',
    '🐵', '🐤', '🐢', '🐧', '🍓', '🍇', '💜', '💛',
    '🍉', '🐝', '🦄', '☀️', '🌙', '🎧', '📦', '🦋'
]

pygame.font.init()
FONT_EMOJI = pygame.font.SysFont('Segoe UI Emoji', 64)
FONT_HUD = pygame.font.SysFont('Verdana MS', 28, bold=True)
FONT_END = pygame.font.SysFont('Verdana MS', 52, bold=True)
FONT_MENU = pygame.font.SysFont('Verdana MS', 36)
FONT_TITULO = pygame.font.SysFont('Verdana MS', 56, bold=True)

COR_FUNDO = (40, 40, 100)
COR_CARTA_FECHADA = (80, 80, 160)
COR_CARTA_ABERTA = (160, 200, 240)
COR_TEXTO = (255, 255, 255)
COR_HUD = (240, 240, 240)
COR_VITORIA = (255, 215, 0)
COR_BOTAO = (100, 160, 240)
COR_BOTAO_HOVER = (130, 180, 255)
COR_BORDA = (255, 255, 255)
