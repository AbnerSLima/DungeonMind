import pygame
import numpy as np
from IA.agent import DungeonEnv

pygame.init()

# Definições da tela
LARGURA, ALTURA = 500, 500
TAMANHO_BLOCO = 50

TAMANHO_CELULA = 50
LARGURA_TELA = 10 * TAMANHO_CELULA
ALTURA_TELA = 9 * TAMANHO_CELULA

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("DungeonMind - Explorador de Masmorra")
clock = pygame.time.Clock()

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)
AMARELO = (255, 255, 0)
CINZA = (150, 150, 150)
LARANJA = (255,69,0)

# Cores
CORES = {
    0: (200, 200, 200),  # Caminho livre (cinza claro)
    1: (50, 50, 50),     # Parede (preto)
    2: (255, 215, 0),    # Tesouro (amarelo)
    3: (255, 0, 0),      # Armadilha (vermelho)
    5: (0, 0, 255),      # Jogador (azul)
    6: (0, 255, 0),      # Saída (verde)
}

pygame.font.init()
fonte = pygame.font.Font(None, 36)  # Define o tamanho do texto

mensagem = ""
contador_mensagem = 0

def exibir_mensagem(texto):
    global mensagem, contador_mensagem
    mensagem = texto
    contador_mensagem = 20  # Define tempo de exibição

def desenhar_texto():
    global contador_mensagem, mensagem

    if mensagem and contador_mensagem > 0:
        texto_renderizado = fonte.render(mensagem, True, PRETO)
        tela.blit(texto_renderizado, (10, ALTURA - 40))
        contador_mensagem -= 1  # Reduz o contador a cada frame
    else:
        mensagem = ""

def desenhar_pontuacao(pontos):
    texto_pontos = fonte.render(f"Score: {pontos}", True, (BRANCO))
    tela.blit(texto_pontos, (10, 10))  # Exibe no canto superior esquerdo

# Mapa fixo
mapa = [

]

# Encontra posição inicial do jogador
for linha in range(len(mapa)):
    for coluna in range(len(mapa[linha])):
        if mapa[linha][coluna] == 5:
            jogador_x, jogador_y = coluna, linha
            mapa[linha][coluna] = 0 

# Iniciar ambiente
env = DungeonEnv()

# Função para desenhar o mapa
def desenhar_mapa(mapa):
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
            elif mapa[linha][coluna] == 6:
                pygame.draw.rect(tela, CINZA, (x, y, TAMANHO_BLOCO, TAMANHO_BLOCO))  # Inimigo

# Função para mover o jogador
def rodar_jogo():
# Loop principal
    rodando = True
    clock.tick(10)
    estado = env.reset()

    while rodando:
        tela.fill(BRANCO)
        mapa = env.get_mapa()
        desenhar_mapa(mapa)
        
        # Desenha o jogador
        pygame.draw.circle(
            tela, (0, 0, 255),
            (estado[0] * TAMANHO_CELULA + TAMANHO_CELULA // 2, estado[1] * TAMANHO_CELULA + TAMANHO_CELULA // 2),
            TAMANHO_CELULA // 3
        )

        desenhar_pontuacao(env.pontos)
        desenhar_texto()

        pygame.display.flip()
        clock.tick(5)  # Controla a velocidade do jogo (3 passos por segundo)

        # Escolher ação aleatória
        acao = np.random.choice([0, 1, 2, 3])
        estado, recompensa, game_over, _ = env.step(acao)

        if recompensa == 50 and mapa[estado[1]][estado[0]] == 0:
            exibir_mensagem("Tesouro coletado!")
            mapa[estado[1]][estado[0]] = 0

        elif recompensa == -75:
            exibir_mensagem("Armadilha ativada!")
            mapa[estado[1]][estado[0]] = 0

        if game_over:
            if env.pontos <= 0:
                exibir_mensagem("Game Over! Sem pontos.")
            elif mapa[estado[1]][estado[0]] == 6:
                exibir_mensagem("Você venceu!")
            pygame.display.flip()
            pygame.time.delay(2000)
            rodando = False

    pygame.quit()

if __name__ == "__main__":
    rodar_jogo()