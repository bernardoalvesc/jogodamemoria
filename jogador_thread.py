import time

def thread_jogador(jogador_id, semaforo_entrada, semaforo_saida, grid, tabuleiro, visivel, encontradas,
                   pontuacao, vez_jogador, jogadas_pendentes, total_viradas, tempo_ultima_jogada):
    while True:
        semaforo_entrada.acquire()

        while True:
            pos = jogadas_pendentes[jogador_id]
            if pos is not None:
                lin, col = pos
                jogadas_pendentes[jogador_id] = None

                if 0 <= lin < grid[1] and 0 <= col < grid[0]:
                    if not visivel[lin][col] and not encontradas[lin][col]:
                        visivel[lin][col] = True
                        total_viradas.append((lin, col))

                        if len(total_viradas) == 2:
                            (l1, c1), (l2, c2) = total_viradas
                            if tabuleiro[l1][c1] == tabuleiro[l2][c2]:
                                encontradas[l1][c1] = True
                                encontradas[l2][c2] = True
                                pontuacao[jogador_id] += 1
                                total_viradas.clear()
                                semaforo_entrada.release()
                            else:
                                tempo_ultima_jogada[0] = time.time()
                            break
                else:
                    break
