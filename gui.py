import pygame
from constantes import *

def tela_menu(tela, clock):
    botoes = [
        ("Fácil (4x4)", 'multi', 1),
        ("Médio (6x4)", 'multi', 2),
        ("Difícil (6x6)", 'multi', 3),
    ]

    while True:
        tela.fill(COR_FUNDO)

        titulo = FONT_END.render("Jogo da Memória", True, COR_TEXTO)
        tela.blit(titulo, (TAMANHO_TELA[0] // 2 - titulo.get_width() // 2, 100))

        for i, (texto, modo, nivel) in enumerate(botoes):
            rect = pygame.Rect(TAMANHO_TELA[0] // 2 - 150, 200 + i * 80, 300, 60)
            cor = COR_BOTAO_HOVER if rect.collidepoint(pygame.mouse.get_pos()) else COR_BOTAO
            pygame.draw.rect(tela, cor, rect, border_radius=10)
            pygame.draw.rect(tela, (255, 255, 255), rect, width=1, border_radius=10)

            txt = FONT_MENU.render(texto, True, COR_TEXTO)
            tela.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for _, modo, nivel in botoes:
                    rect = pygame.Rect(TAMANHO_TELA[0] // 2 - 150, 200 + botoes.index((_, modo, nivel)) * 80, 300, 60)
                    if rect.collidepoint(event.pos):
                        return modo, nivel

def solicitar_nomes(tela, clock):
    nomes = ["", ""]
    campo_ativo = 0
    while True:
        tela.fill(COR_FUNDO)

        instr = FONT_MENU.render("Digite os nomes dos jogadores e pressione ENTER", True, COR_TEXTO)
        tela.blit(instr, (TAMANHO_TELA[0] // 2 - instr.get_width() // 2, 100))

        for i in range(2):
            cor_fundo = (80, 80, 110) if campo_ativo == i else (50, 50, 70)
            rect = pygame.Rect(TAMANHO_TELA[0] // 2 - 200, 200 + i * 100, 400, 60)
            pygame.draw.rect(tela, cor_fundo, rect, border_radius=10)
            pygame.draw.rect(tela, (255, 255, 255), rect, width=1, border_radius=10)

            texto = FONT_MENU.render(nomes[i] or f"Jogador {i+1}", True, COR_TEXTO)
            tela.blit(texto, (rect.x + 10, rect.y + 15))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(2):
                    rect = pygame.Rect(TAMANHO_TELA[0] // 2 - 200, 200 + i * 100, 400, 60)
                    if rect.collidepoint(event.pos):
                        campo_ativo = i
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if all(n.strip() != "" for n in nomes):
                        return nomes
                elif event.key == pygame.K_BACKSPACE:
                    nomes[campo_ativo] = nomes[campo_ativo][:-1]
                else:
                    if len(nomes[campo_ativo]) < 15:
                        nomes[campo_ativo] += event.unicode

def tela_vitoria(tela, clock, mensagem):
    while True:
        tela.fill(COR_FUNDO)

        texto = FONT_END.render(mensagem, True, COR_VITORIA)
        tela.blit(texto, (TAMANHO_TELA[0] // 2 - texto.get_width() // 2, TAMANHO_TELA[1] // 2 - 100))

        btn = pygame.Rect(TAMANHO_TELA[0] // 2 - 150, TAMANHO_TELA[1] // 2 + 20, 300, 60)
        pygame.draw.rect(tela, COR_BOTAO, btn, border_radius=10)
        pygame.draw.rect(tela, (255, 255, 255), btn, width=1, border_radius=10)

        txt_btn = FONT_MENU.render("Voltar ao Menu", True, COR_TEXTO)
        tela.blit(txt_btn, (btn.centerx - txt_btn.get_width() // 2, btn.centery - txt_btn.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and btn.collidepoint(event.pos):
                return
