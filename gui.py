import pygame
from constantes import *

def tela_menu(tela, clock):
    botoes = [
        ("Fácil (4x4)", 'multi', 1),
        ("Médio (6x4)", 'multi', 2),
        ("Difícil (6x6)", 'multi', 3),
    ]
    fonte = FONT_MENU
    selecionado = -1

    while True:
        tela.fill(COR_FUNDO)
        titulo = FONT_END.render("Jogo da Memória 🧠", True, COR_TEXTO)
        tela.blit(titulo, ((TAMANHO_TELA[0] - titulo.get_width()) // 2, 100))

        for i, (texto, modo, nivel) in enumerate(botoes):
            rect = pygame.Rect((TAMANHO_TELA[0] // 2 - 150, 250 + i * 80, 300, 50))
            cor = COR_BOTAO_HOVER if i == selecionado else COR_BOTAO
            pygame.draw.rect(tela, cor, rect, border_radius=12)
            txt = fonte.render(texto, True, COR_TEXTO)
            tela.blit(txt, (rect.centerx - txt.get_width() // 2, rect.centery - txt.get_height() // 2))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEMOTION:
                mx, my = event.pos
                selecionado = -1
                for i in range(len(botoes)):
                    rect = pygame.Rect((TAMANHO_TELA[0] // 2 - 150, 250 + i * 80, 300, 50))
                    if rect.collidepoint(mx, my):
                        selecionado = i
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if selecionado != -1:
                    return botoes[selecionado][1], botoes[selecionado][2]

def solicitar_nomes(tela, clock):
    nomes = ["", ""]
    fonte = pygame.font.SysFont(None, 48)
    input_ativo = [True, False]
    caixa_input = [pygame.Rect(300, 200, 400, 50), pygame.Rect(300, 300, 400, 50)]

    while True:
        tela.fill(COR_FUNDO)
        for i in range(2):
            cor_caixa = (80, 80, 80) if input_ativo[i] else (50, 50, 50)
            pygame.draw.rect(tela, cor_caixa, caixa_input[i], border_radius=10)
            texto = fonte.render(nomes[i], True, COR_TEXTO)
            tela.blit(texto, (caixa_input[i].x + 10, caixa_input[i].y + 10))

        titulo = fonte.render("Digite o nome dos jogadores:", True, COR_TEXTO)
        tela.blit(titulo, (280, 100))

        botao_ok = pygame.Rect(350, 400, 200, 50)
        pygame.draw.rect(tela, (60, 120, 60), botao_ok, border_radius=10)
        tela.blit(fonte.render("OK", True, (255, 255, 255)), (botao_ok.x + 60, botao_ok.y + 10))

        pygame.display.flip()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(2):
                    input_ativo[i] = caixa_input[i].collidepoint(event.pos)
                if botao_ok.collidepoint(event.pos) and all(nomes):
                    return nomes
            elif event.type == pygame.KEYDOWN:
                for i in range(2):
                    if input_ativo[i]:
                        if event.key == pygame.K_BACKSPACE:
                            nomes[i] = nomes[i][:-1]
                        elif len(nomes[i]) < 15 and event.unicode.isprintable():
                            nomes[i] += event.unicode

def tela_vitoria(tela, clock, mensagem):
    while True:
        tela.fill(COR_FUNDO)
        texto = FONT_END.render(mensagem, True, COR_VITORIA)
        txt_rect = texto.get_rect(center=(TAMANHO_TELA[0] // 2, TAMANHO_TELA[1] // 2 - 50))
        tela.blit(texto, txt_rect)

        btn = pygame.Rect(TAMANHO_TELA[0] // 2 - 120, TAMANHO_TELA[1] // 2 + 40, 240, 50)
        pygame.draw.rect(tela, COR_BOTAO, btn, border_radius=12)
        txt_btn = FONT_HUD.render("Voltar ao Menu", True, COR_TEXTO)
        tela.blit(txt_btn, (btn.centerx - txt_btn.get_width() // 2, btn.centery - txt_btn.get_height() // 2))

        pygame.display.flip()
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if btn.collidepoint(event.pos):
                    return
