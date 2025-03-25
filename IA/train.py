import os
import random
import numpy as np
from IA.agent import DungeonEnv

# Criando o ambiente
env = DungeonEnv()
num_episodios = 300
taxa_aprendizado = 0.9
desconto = 0.9
exploracao = 1.0
decaimento_exploracao = 0.995

# Carregar a tabela Q existente
if os.path.exists("q_table.npy"):
    q_table = np.load("q_table.npy")
    print("✅ Tabela Q carregada!")
else:
    q_table = np.zeros((env.largura, env.altura, env.action_space.n))

# Criando a Tabela Q
q_table = np.zeros((env.largura, env.altura, env.action_space.n))

for episodio in range(num_episodios):
    estado = env.reset()
    done = False
    while not done:
        env.render()
        # Escolher ação (exploração vs. exploração)
        if random.uniform(0, 1) < exploracao:
            acao = env.action_space.sample()
        else:
            acao = np.argmax(q_table[estado[0], estado[1], :])

        # Executar ação
        novo_estado, recompensa, done, _ = env.step(acao)

        # Atualizar tabela Q
        q_table[estado[0], estado[1], acao] = (1 - taxa_aprendizado) * q_table[estado[0], estado[1], acao] + \
            taxa_aprendizado * (recompensa + desconto * np.max(q_table[novo_estado[0], novo_estado[1], :]))

        estado = novo_estado

    # Diminuir a exploração ao longo do tempo
    exploracao = max(0.1, exploracao * decaimento_exploracao)

    if episodio % 100 == 0:
        print(f"🏆 Episódio {episodio} - Exploração: {exploracao:.2f}")
    

# Salvar a Tabela Q para continuar treinando depois
np.save("q_table.npy", q_table)
print("💾 Tabela Q salva!")
print("Treinamento concluído! 🚀")