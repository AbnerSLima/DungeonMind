import pygame

pygame.init()

# Definições da tela
LARGURA, ALTURA = 500, 500
TAMANHO_BLOCO = 50
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("DungeonMind - Explorador de Masmorra")
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
CINZA = (150, 150, 150)

# Mapa fixo
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, 0, 0, 0, 0, 0, 4, 2, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 4, 0, 0, 1, 0, 1],
    [1, 2, 0, 1, 1, 1, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 6, 1, 1, 1]
]

# Encontra posição inicial dos inimigos
inimigos = []
for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
        if mapa[linha][coluna] == 4:
            inimigos.append([coluna, linha])
            mapa[linha][coluna] = 0

# Encontra posição inicial do jogador
for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
        if mapa[linha][coluna] == 5:
            jogador_x, jogador_y = coluna, linha
            mapa[linha][coluna] = 0 

# Função para desenhar o mapa
def desenhar_mapa():
    tela.fill(BRANCO)
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[linha])):
            x = coluna * TAMANHO_BLOCO
            y = linha * TAMANHO_BLOCO

            if mapa[linha][coluna] == 1:
                pygame.draw.rect(tela, PRETO, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))
            elif mapa[linha][coluna] == 2:
                pygame.draw.circle(tela, AMARELO, (x + 25, y + 25), 10)  # Tesouro
            elif mapa[linha][coluna] == 3:
                pygame.draw.rect(tela, VERMELHO, (x + 15, y + 15, 20, 20))  # Armadilha
            elif mapa[linha][coluna] == 4:
                pygame.draw.circle(tela, AZUL, (x + 25, y + 25), 15)  # Inimigo
            elif mapa[linha][coluna] == 6:
                pygame.draw.rect(tela, CINZA, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))  # Inimigo

# Função para mover o jogador
def mover_jogador(dx, dy):
    global jogador_x, jogador_y

    nova_x = jogador_x + dx
    nova_y = jogador_y + dy

    # Verifica se o movimento é permitido
    if 0 <= nova_x < len(mapa[0]) and 0 <= nova_y < len(mapa) and mapa[nova_y][nova_x] != 1:
        jogador_x, jogador_y = nova_x, nova_y

        # Interação com tesouros e armadilhas
        if mapa[jogador_y][jogador_x] == 2:
            print("💰 Pegou um tesouro!")
            mapa[jogador_y][jogador_x] = 0
        elif mapa[jogador_y][jogador_x] == 3:
            print("☠️ Caiu em uma armadilha!")
            mapa[jogador_y][jogador_x] = 0
        
        mover_inimigos()

# Função para mover os inimigos aleatoriamente
def mover_inimigos():
    direcoes = [(0, 1), (0, -1)]
    
    for i in range(len(inimigos)):
        x, y = inimigos[i]

        for dx, dy in direcoes:
            novo_x, novo_y = x + dx, y + dy
            if 0 <= novo_x < len(mapa[0]) and 0 <= novo_y < len(mapa) and mapa[novo_y][novo_x] == 0:
                inimigos[i] = [novo_x, novo_y]
                break 
# Loop principal
rodando = True
while rodando:
    clock.tick(10)

    # Captura eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                mover_jogador(0, -1)
            if evento.key == pygame.K_DOWN:
                mover_jogador(0, 1)
            if evento.key == pygame.K_LEFT:
                mover_jogador(-1, 0)
            if evento.key == pygame.K_RIGHT:
                mover_jogador(1, 0)
            if mapa[jogador_y][jogador_x] == 6:
                print("✅ Você encontrou a saída!")
                rodando = False

    # Movimenta os inimigos
    #mover_inimigos()

    # Desenha o jogo
    desenhar_mapa()

    # Desenha o jogador
    pygame.draw.circle(tela, VERDE, (jogador_x * TAMANHO_BLOCO + 25, jogador_y * TAMANHO_BLOCO + 25), 15)
    
    # Desenha os inimigos
    for inimigo_x, inimigo_y in inimigos:
        pygame.draw.circle(tela, AZUL, (inimigo_x * TAMANHO_BLOCO + 25, inimigo_y * TAMANHO_BLOCO + 25), 15)

    pygame.display.flip()

pygame.quit()