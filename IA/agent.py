import gym
import numpy as np
import pygame
from gym import spaces

class SimpleGameEnv(gym.Env):
    def __init__(self):
        super(SimpleGameEnv, self).__init__()
        
        # Definir tamanho da tela e do jogador
        self.width = 500
        self.height = 500
        self.player_size = 20
        
        # Criar ações (esquerda, direita, cima, baixo)
        self.action_space = spaces.Discrete(4)
        
        # Estado (posição do jogador)
        self.observation_space = spaces.Box(low=0, high=500, shape=(2,), dtype=np.int32)
        
        self.reset()
    
    def reset(self):
        # Posição inicial do jogador
        self.player_x = self.width // 2
        self.player_y = self.height // 2
        return np.array([self.player_x, self.player_y])
    
    def step(self, action):
        if action == 0:  # Esquerda
            self.player_x -= 10
        elif action == 1:  # Direita
            self.player_x += 10
        elif action == 2:  # Cima
            self.player_y -= 10
        elif action == 3:  # Baixo
            self.player_y += 10
        
        # Manter dentro da tela
        self.player_x = np.clip(self.player_x, 0, self.width - self.player_size)
        self.player_y = np.clip(self.player_y, 0, self.height - self.player_size)
        
        # Criar recompensa (exemplo: manter-se no centro)
        reward = -np.sqrt((self.player_x - self.width//2)**2 + (self.player_y - self.height//2)**2)
        
        # O jogo não tem fim por enquanto
        done = False
        
        return np.array([self.player_x, self.player_y]), reward, done, {}
    
    def render(self):
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0, 255, 0), (self.player_x, self.player_y, self.player_size, self.player_size))
        pygame.display.flip()
    
    def close(self):
        pygame.quit()

# Criar ambiente
env = SimpleGameEnv()

# Criar agente aleatório
for _ in range(100):
    action = env.action_space.sample()  # Escolhe uma ação aleatória
    state, reward, done, _ = env.step(action)
    print(f'Ação: {action}, Estado: {state}, Recompensa: {reward}')
    env.render()
    pygame.time.delay(100)

env.close()