import gym
import numpy as np
from gym import spaces

class DungeonEnv(gym.Env):
    def __init__(self):
        super(DungeonEnv, self).__init__()

        self.mapa = [
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

        self.altura = len(self.mapa)
        self.largura = len(self.mapa[0])

        # Encontrar posição inicial do jogador
        for linha in range(self.altura):
            for coluna in range(self.largura):
                if self.mapa[linha][coluna] == 5:
                    self.jogador_x, self.jogador_y = coluna, linha
                    self.mapa[self.jogador_y][self.jogador_x] = 0 

        # Definir espaço de ações (4 direções)
        self.action_space = spaces.Discrete(4)

        # Espaço de observação (posição do jogador)
        self.observation_space = spaces.Box(low=0, high=max(self.largura, self.altura), shape=(2,), dtype=np.int32)

    def reset(self):
        """ Reinicia o jogo e retorna o estado inicial """
        self.jogador_x, self.jogador_y = 1, 1  # Posição inicial do jogador
        return np.array([self.jogador_x, self.jogador_y])

    def step(self, action):
        """ Executa um passo no ambiente """
        if action == 0:  # Cima
            nova_x, nova_y = self.jogador_x, self.jogador_y - 1
        elif action == 1:  # Baixo
            nova_x, nova_y = self.jogador_x, self.jogador_y + 1
        elif action == 2:  # Esquerda
            nova_x, nova_y = self.jogador_x - 1, self.jogador_y
        elif action == 3:  # Direita
            nova_x, nova_y = self.jogador_x + 1, self.jogador_y
        else:
            nova_x, nova_y = self.jogador_x, self.jogador_y

        # Checa se a nova posição é válida (não é parede)
        if self.mapa[nova_y][nova_x] != 1:
            self.jogador_x, self.jogador_y = nova_x, nova_y

        # Definir recompensa
        recompensa = -0.1  # Pequena penalidade para evitar movimentos aleatórios

        if self.mapa[self.jogador_y][self.jogador_x] == 2:
            recompensa = 10  # Pegou tesouro
        elif self.mapa[self.jogador_y][self.jogador_x] == 3:
            recompensa = -10  # Caiu em armadilha
        elif self.mapa[self.jogador_y][self.jogador_x] == 4:
            recompensa = -60  # Foi capturado
        elif self.mapa[self.jogador_y][self.jogador_x] == 6:
            recompensa = 50  # Saiu do labirinto!

        estado = np.array([self.jogador_x, self.jogador_y])
        game_over = self.mapa[self.jogador_y][self.jogador_x] == 6  # Saiu do mapa
        return estado, recompensa, game_over, {}

    def render(self):
        """ Renderiza o estado atual (apenas para depuração) """
        for y, linha in enumerate(self.mapa):
            linha_str = ""
            for x, valor in enumerate(linha):
                if x == self.jogador_x and y == self.jogador_y:
                    linha_str += "J "
                else:
                    linha_str += str(valor) + " "
            print(linha_str)
        print("\n")