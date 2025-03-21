from agent import DungeonEnv
import numpy as np

# Carregar ambiente e Q-table treinada
env = DungeonEnv()
q_table = np.load("q_table.npy")

estado = env.reset()
done = False

while not done:
    env.render()
    acao = np.argmax(q_table[estado[0], estado[1], :])
    estado, _, done, _ = env.step(acao)

print("✅ Agente finalizou a dungeon!")