import pygame
import threading
import time
from constantes import *
from utils import criar_tabuleiro
from semaforo import semaforo_p1, semaforo_p2
from jogador_thread import thread_jogador
from gui import tela_menu, tela_vitoria

# Inicialização
pygame.init()
tela = pygame.display.set_mode(TAMANHO_TELA)
pygame.display.set.caption('Click & Pair')
clock = pygame.time.Clock()

# Função para rodar a partida
def rodar_jogo(modo_vs_cpu, nivel_cpu, grid):
  global carta_virada, tempo_ultima_jogada, vez_jogador

  tabuleiro, visivel, encontradas, cpu_memoria = criar_tabuleiro(grid)
  jogadas_pendentes = []
  pontuacao = [0, 0]

  carta_virada = []
  tempo_ultima_jogada = 0
  vez_jogador = 0
  fim_de_jogo = False

  # Inicia as threads dos jogadores
  threading.Thread(target=thread_jogador, args=(0, semaforo_p1, semaforo_p2, jogadas_pendentes, modo_vs_cpu, grid, visivel, encontradas, cpu_memoria, nivel_cpu), daemon=True).start()
  threading.Thread(target=thread_jogador, args=(1, semaforo_p2, semaforo_p1, jogadas_pendentes, modo_vs_cpu, grid, visivel, encontradas, cpu_memoria, nivel_cpu), daemon=True).start()

  # Loop da partida

  while not fim_de_jogo:
    clock.tick (FPS)

    # Eventos
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
      elif event.type == pygame.MOUSEBUTTONDOWN and vez_jogador == 0 and not modo_vs_cpu:
        x, y = event.pos
        col = x // (TAMANHO_CARTA[0] + MARGEM)
        lin = y // (TAMANHO_CARTA[1] + MARGEM)
        if 0 <= lin < grid[1] and 0 <= col < grid [0]:
          if not visivel[lin][col] and not encontradas [lin][col]:
            jogadas_pendentes.append((0, (lin,col)))
            SOUND_CLICK.play()

    # Verifica jogada pendente
    if len (jogadas_pendentes) > 0:
      jogador_id, (lin, col) = jogadas_pendentes.pop(0)

      if not visivel[lin][col] and not encontradas[lin][col]:
        # Animação de flip simples (escala de 0.5 a 1.0)
        for scale in [0.5, 0.7, 0.9, 1.0]:
          desenhar_tabuleiro(tela, tabuleiro, visivel, encontradas, grid, scale)
          pygame.display.flip()
          clock.tick(60)

        visivel[lin][col] = True
        carta_virada.append((lin,col))

        emoji_carta = tabuleiro[lin][col]
        if emoji_carta not in cpu_memoria:
          cpu_memoria[emoji_carta] = []
        if (lin, col) not in cpu_memoria[emoji_carta]:
          cpu_memoria[emoji_carta].append((lin, col))

        if len(carta_virada) == 2:
          l1, c1 = carta_virada[0]
          l2,c2 = carta_virada[1]
          if tabuleiro[l1][c1] == tabuleiro[l2][c2]
          encontradas[l1][c1] = True
          encontradas[l2][c2] = True
          pontuacao[jogador_id] += 1
          SOUND_MATCH.play()
        else:
          tempo_ultima_jogada = time.time ()
        carta_virada = []

        vez_jogador = 1 - vez_jogador

  # Esconde cartas erradas
  if tempo_ultima_jogada > 0 and time.time() - tempo_ultima_jogada > 1:
    for i in rage (grid[1]):
      for j in range (grid[0]):
        if visivel[i][j] and not encontradas [i][j]:
          visivel[i][j] = False
        tempo_ultima_jogada = 0

 # Renderiza
        desenhar_tabuleiro(tela, tabuleiro, visivel, encontradas, grid)
        hud_text = FONT_HUD.render(f'Jogador 1: {pontuacao[0]}  |  Jogador 2: {pontuacao[1]}', True, COR_HUD)
        tela.blit(hud_text, (20, TAMANHO_TELA[1] - 40))

 # Fim de jogo
        total_pares = (grid[0] * grid[1]) // 2
        if pontuacao[0] + pontuacao[1] == total_pares:
            fim_de_jogo = True
            SOUND_WIN.play()
            pygame.time.delay(500)

            # Mensagem
            if pontuacao[0] > pontuacao[1]:
                mensagem = "Jogador 1 venceu!"
            elif pontuacao[1] > pontuacao[0]:
                mensagem = "Jogador 2 venceu!"
            else:
                mensagem = "Empate!"

            tela_vitoria(tela, clock, mensagem)

        pygame.display.flip()

# --- Função desenhar tabuleiro ---
def desenhar_tabuleiro(tela, tabuleiro, visivel, encontradas, grid, scale=1.0):
    tela.fill(COR_FUNDO)

    for i in range(grid[1]):
        for j in range(grid[0]):
            x = j * (TAMANHO_CARTA[0] + MARGEM) + MARGEM
            y = i * (TAMANHO_CARTA[1] + MARGEM) + MARGEM

            rect = pygame.Rect(x, y, TAMANHO_CARTA[0], TAMANHO_CARTA[1])
            pygame.draw.rect(tela, COR_CARTA_ABERTA, rect)

            if visivel[i][j] or encontradas[i][j]:
                emoji = tabuleiro[i][j]
                img = FONT_EMOJI.render(emoji, True, COR_TEXTO)
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                img_rect = img.get_rect(center=rect.center)
                tela.blit(img, img_rect)
            else:
                pygame.draw.rect(tela, COR_CARTA_FECHADA, rect)

# --- Loop principal geral ---
while True:
    modo, nivel = tela_menu(tela, clock)

    if modo == 'cpu':
        if nivel == 1:
            grid = (4, 4)
        elif nivel == 2:
            grid = (6, 6)
        elif nivel == 3:
            grid = (8, 8)
        rodar_jogo(modo_vs_cpu=True, nivel_cpu=nivel, grid=grid)

    elif modo == 'multi':
        rodar_jogo(modo_vs_cpu=False, nivel_cpu=1, grid=(4, 4))


