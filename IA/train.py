import os
import random
import numpy as np
from IA.agent import DungeonEnv

env = DungeonEnv()
num_episodios = 1000
taxa_aprendizado = 0.9
desconto = 0.9
exploracao = 1.0
decaimento_exploracao = 0.995

# Carregar a tabela Q existente
if os.path.exists("q_table.npy"):
    q_table = np.load("q_table.npy")
    print("\n✅ Tabela Q carregada!\n")
else:
    q_table = np.zeros((env.largura, env.altura, env.action_space.n))

# Criando a Tabela Q
q_table = np.zeros((env.largura, env.altura, env.action_space.n))

# Variáveis para o relatório
total_recompensas = 0
total_passos = 0

# Treinar o agente com Q-Learning
for episodio in range(1, num_episodios + 1):
    estado = env.reset()
    done = False
    recompensa_episodio = 0
    passos = 0

    while not done:
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
        recompensa_episodio += recompensa
        passos += 1

        # Se a pontuação acabar, game over
        if env.pontos <= 0:
            done = True

    # Atualizar métricas do relatório
    total_recompensas += recompensa_episodio
    total_passos += passos

    # Diminuir a exploração ao longo do tempo
    exploracao = max(0.1, exploracao * decaimento_exploracao)

    # Gerar relatório a cada 100 episódios
    if episodio % 100 == 0:
        recompensa_media = total_recompensas / 100
        passos_medios = total_passos / 100
        print(f"🏆 Episódio {episodio}")
        print(f"🔍 Exploração: {exploracao:.2f}")
        print(f"📊 Recompensa Média: {recompensa_media:.2f}")
        print(f"🚶 Passos Médios por Episódio: {passos_medios:.2f}\n")

        # Resetar métricas
        total_recompensas = 0
        total_passos = 0

# Salvar a Tabela Q
np.save("q_table.npy", q_table)
print("💾 Tabela Q salva!\n")
print("Treinamento concluído! 🚀\n")