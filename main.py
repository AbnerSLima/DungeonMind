import pygame

pygame.init()

# Definições da tela
LARGURA, ALTURA = 500, 500
TAMANHO_BLOCO = 50
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("DungeonMind - Explorador de Masmorra")
clock = pygame.time.Clock()

jogador = pygame.image.load("assets/jogador.png")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
AZUL = (0, 0, 255)
CINZA = (150, 150, 150)
LARANJA = (255,69,0)

pygame.font.init()
fonte = pygame.font.Font(None, 36)  # Define o tamanho do texto

mensagem = ""  # Variável para armazenar mensagens do jogo
contador_mensagem = 0  # Timer para remover mensagens após um tempo

def exibir_mensagem(texto):
    global mensagem, contador_mensagem
    mensagem = texto
    contador_mensagem = 50  # Define tempo de exibição (~5 segundos)

def desenhar_texto():
    if mensagem:
        texto_renderizado = fonte.render(mensagem, True, (LARANJA))
        tela.blit(texto_renderizado, (10, ALTURA - 40))  # Exibe no canto inferior esquerdo

# Mapa fixo
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 5, 0, 0, 0, 0, 0, 0, 3, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 3, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 4, 0, 1],
    [1, 0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 0, 4, 0, 0, 1, 0, 1],
    [1, 2, 0, 1, 1, 1, 0, 1, 2, 1],
    [1, 1, 1, 1, 1, 1, 6, 1, 1, 1]
]

# Encontra posição inicial dos inimigos
inimigos = []
for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
        if mapa[linha][coluna] == 4:
            inimigos.append({"x": coluna, "y": linha, "direcao": -1})
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
            exibir_mensagem("Você encontrou um tesouro!")
            mapa[jogador_y][jogador_x] = 0
        elif mapa[jogador_y][jogador_x] == 3:
            print("☠️ Caiu em uma armadilha!")
            exibir_mensagem("Você caiu em uma armadilha!")
            mapa[jogador_y][jogador_x] = 0
        
        mover_inimigos()

# Função para mover os inimigos para cima e para baixo
def mover_inimigos():
    for inimigo in inimigos:
        novo_y = inimigo["y"] + inimigo["direcao"]

        # Verifica se o inimigo pode continuar na mesma direção
        if 0 <= novo_y < len(mapa) and mapa[novo_y][inimigo["x"]] == 0:
            inimigo["y"] = novo_y
        else:
            # Muda de direção ao atingir um obstáculo
            inimigo["direcao"] *= -1

# Loop principal
rodando = True
while rodando:
    clock.tick(10)

    # Guarda posição antiga do jogador
    jogador_x_antigo, jogador_y_antigo = jogador_x, jogador_y
    
    # Guarda posição antiga dos inimigos
    inimigos_anteriores = [{"x": inimigo["x"], "y": inimigo["y"]} for inimigo in inimigos]

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
                exibir_mensagem("Você encontrou a saída!")
                #rodando = False
                
    # Verifica se o jogador encostou ou TROCOU de lugar com um inimigo
    for i, inimigo in enumerate(inimigos):
        if jogador_x == inimigo["x"] and jogador_y == inimigo["y"]:
            print("🚨 Você foi capturado pelo inimigo! 🚨")
            exibir_mensagem("Você foi capturado pelo inimigo!")
            #rodando = False
        elif (jogador_x == inimigos_anteriores[i]["x"] and jogador_y == inimigos_anteriores[i]["y"] and
              jogador_x_antigo == inimigo["x"] and jogador_y_antigo == inimigo["y"]):
            print("🚨 Você foi capturado pelo inimigo! 🚨")
            exibir_mensagem("Você foi capturado pelo inimigo!")
            #rodando = False

    # Desenha o jogo
    desenhar_mapa()

    # Desenha o jogador
    pygame.draw.circle(tela, VERDE, (jogador_x * TAMANHO_BLOCO + 25, jogador_y * TAMANHO_BLOCO + 25), 15)
    
    # Desenha os inimigos
    for inimigo in inimigos:
        pygame.draw.circle(tela, AZUL, (inimigo["x"] * TAMANHO_BLOCO + 25, inimigo["y"] * TAMANHO_BLOCO + 25), 15)

    # Reduz tempo de exibição da mensagem
    if contador_mensagem > 0:
        contador_mensagem -= 1
    else:
        mensagem = ""

    desenhar_texto()
    pygame.display.flip()

pygame.quit()