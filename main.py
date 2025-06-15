import pygame
import threading
import time
from constantes import *
from utils import criar_tabuleiro
from semaforo import semaforo_p1, semaforo_p2
from gui import tela_menu, tela_vitoria, solicitar_nomes
from jogador_thread import thread_jogador

pygame.init()
tela = pygame.display.set_mode(TAMANHO_TELA, pygame.FULLSCREEN)
pygame.display.set_caption('Jogo da Memória')
clock = pygame.time.Clock()

# Estados globais
jogo_em_execucao = True
jogadas_pendentes = [None, None]
nomes_jogadores = ["Jogador 1", "Jogador 2"]

def rodar_jogo(grid):
    global jogo_em_execucao, jogadas_pendentes, nomes_jogadores

    jogo_em_execucao = True
    tabuleiro, visivel, encontradas, _ = criar_tabuleiro(grid)
    pontuacao = [0, 0]
    vez_jogador = [0]
    total_viradas = []
    tempo_ultima_jogada = [0]

    largura_total = grid[0] * (TAMANHO_CARTA[0] + MARGEM)
    altura_total = grid[1] * (TAMANHO_CARTA[1] + MARGEM)
    offset_x = (TAMANHO_TELA[0] - largura_total) // 2
    offset_y = (TAMANHO_TELA[1] - altura_total) // 2

    botao_sair = pygame.Rect(TAMANHO_TELA[0] - 180, TAMANHO_TELA[1] - 50, 160, 40)

    threading.Thread(target=thread_jogador, args=(0, semaforo_p1, semaforo_p2, grid, tabuleiro, visivel, encontradas, pontuacao, vez_jogador, jogadas_pendentes, total_viradas, tempo_ultima_jogada), daemon=True).start()
    threading.Thread(target=thread_jogador, args=(1, semaforo_p2, semaforo_p1, grid, tabuleiro, visivel, encontradas, pontuacao, vez_jogador, jogadas_pendentes, total_viradas, tempo_ultima_jogada), daemon=True).start()
    semaforo_p1.release()

    while jogo_em_execucao:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if botao_sair.collidepoint(event.pos):
                    return
                x, y = pygame.mouse.get_pos()
                col = (x - offset_x) // (TAMANHO_CARTA[0] + MARGEM)
                lin = (y - offset_y) // (TAMANHO_CARTA[1] + MARGEM)
                if 0 <= lin < grid[1] and 0 <= col < grid[0]:
                    jogadas_pendentes[vez_jogador[0]] = (lin, col)

        if tempo_ultima_jogada[0] and time.time() - tempo_ultima_jogada[0] > 1:
            for l, c in total_viradas:
                visivel[l][c] = False
            total_viradas.clear()
            tempo_ultima_jogada[0] = 0
            vez_jogador[0] = 1 - vez_jogador[0]
            if vez_jogador[0] == 0:
                semaforo_p1.release()
            else:
                semaforo_p2.release()

        desenhar_tabuleiro(tela, tabuleiro, visivel, encontradas, grid, offset_x, offset_y)
        hud = FONT_HUD.render(f"{nomes_jogadores[0]}: {pontuacao[0]}  |  {nomes_jogadores[1]}: {pontuacao[1]}", True, COR_HUD)
        tela.blit(hud, (20, TAMANHO_TELA[1] - 40))
        vez_txt = FONT_HUD.render(f"Vez de {nomes_jogadores[vez_jogador[0]]}", True, COR_TEXTO)
        tela.blit(vez_txt, (TAMANHO_TELA[0] - 320, 20))

        # Botão de sair
        pygame.draw.rect(tela, (100, 30, 30), botao_sair, border_radius=8)
        sair_txt = FONT_HUD.render("Sair da Partida", True, (255, 255, 255))
        tela.blit(sair_txt, (botao_sair.x + 10, botao_sair.y + 8))

        if sum(pontuacao) == (grid[0] * grid[1]) // 2:
            pygame.time.delay(800)
            if pontuacao[0] > pontuacao[1]: msg = f"{nomes_jogadores[0]} venceu!"
            elif pontuacao[1] > pontuacao[0]: msg = f"{nomes_jogadores[1]} venceu!"
            else: msg = "Empate!"
            tela_vitoria(tela, clock, msg)
            jogo_em_execucao = False

        pygame.display.flip()

def desenhar_tabuleiro(tela, tabuleiro, visivel, encontradas, grid, offset_x, offset_y):
    tela.fill(COR_FUNDO)

    for i in range(grid[1]):
        for j in range(grid[0]):
            x = offset_x + j * (TAMANHO_CARTA[0] + MARGEM)
            y = offset_y + i * (TAMANHO_CARTA[1] + MARGEM)
            rect = pygame.Rect(x, y, TAMANHO_CARTA[0], TAMANHO_CARTA[1])
            pygame.draw.rect(tela, COR_CARTA_ABERTA, rect, border_radius=12)
            if visivel[i][j] or encontradas[i][j]:
                emoji = tabuleiro[i][j]
                img = FONT_EMOJI.render(emoji, True, COR_TEXTO)
                img_rect = img.get_rect(center=rect.center)
                tela.blit(img, img_rect)
            else:
                pygame.draw.rect(tela, COR_CARTA_FECHADA, rect, border_radius=12)

# Loop principal
while True:
    modo, nivel = tela_menu(tela, clock)
    if modo == 'multi':
        nomes_jogadores = solicitar_nomes(tela, clock)
        grid_size = {1: (4, 4), 2: (6, 4), 3: (6, 6)}[nivel]
        rodar_jogo(grid=grid_size)
