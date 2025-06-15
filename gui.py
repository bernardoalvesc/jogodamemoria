import pygame
from constantes import *

# --- Tela de Menu Principal ---
def tela_menu(tela, clock):
    botoes = [
        ("5x5 (Fácil)", 1),
        ("6x6 (Médio)", 2),
        ("7x7 (Difícil)", 3),
        ("8x8 (Insano)", 4),
    ]

    largura_botao = 300
    altura_botao = 60
    espaco = 20
    total_altura = len(botoes) * (altura_botao + espaco) - espaco
    start_y = (TAMANHO_TELA[1] - total_altura) // 2

    while True:
        tela.fill(COR_FUNDO)

        titulo = FONT_HUD.render("Jogo da Memória - Multiplayer", True, COR_TEXTO)
        tela.blit(titulo, (TAMANHO_TELA[0] // 2 - titulo.get_width() // 2, 100))

        mouse = pygame.mouse.get_pos()

        for i, (texto, nivel) in enumerate(botoes):
            x = TAMANHO_TELA[0] // 2 - largura_botao // 2
            y = start_y + i * (altura_botao + espaco)
            rect = pygame.Rect(x, y, largura_botao, altura_botao)
            cor = (70, 70, 70) if rect.collidepoint(mouse) else COR_CARTA_FECHADA
            pygame.draw.rect(tela, cor, rect, border_radius=12)

            label = FONT_HUD.render(texto, True, COR_TEXTO)
            tela.blit(label, (x + largura_botao // 2 - label.get_width() // 2, y + altura_botao // 2 - label.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, (_, nivel) in enumerate(botoes):
                    x = TAMANHO_TELA[0] // 2 - largura_botao // 2
                    y = start_y + i * (altura_botao + espaco)
                    rect = pygame.Rect(x, y, largura_botao, altura_botao)
                    if rect.collidepoint(event.pos):
                        return 'multi', nivel

        pygame.display.flip()
        clock.tick(60)

# --- Tela de Vitória ---
def tela_vitoria(tela, clock, mensagem):
    while True:
        tela.fill(COR_FUNDO)

        texto = FONT_HUD.render(mensagem, True, COR_TEXTO)
        voltar = FONT_HUD.render("Clique para voltar ao menu", True, COR_HUD)

        tela.blit(texto, (TAMANHO_TELA[0] // 2 - texto.get_width() // 2, TAMANHO_TELA[1] // 2 - 50))
        tela.blit(voltar, (TAMANHO_TELA[0] // 2 - voltar.get_width() // 2, TAMANHO_TELA[1] // 2 + 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.flip()
        clock.tick(60)
