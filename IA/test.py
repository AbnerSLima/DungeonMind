import time
import numpy as np
from IA.agent import DungeonEnv

# Criando o ambiente
env = DungeonEnv()

# Carregando a Tabela Q treinada
q_table = np.load("q_table.npy")

# Rodando o agente treinado no ambiente
estado = env.reset()
done = False

print("🎮 Iniciando visualização do robô treinado...")
time.sleep(2)

while not done:
    env.render()  # Mostra a tela do jogo
    acao = np.argmax(q_table[estado[0], estado[1], :])  # Escolhe a melhor ação aprendida
    estado, recompensa, done, _ = env.step(acao)
    time.sleep(0.5)  # Pequeno delay para ver a movimentação

print("🏆 O robô finalizou o jogo!")
env.close()
