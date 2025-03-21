from . import agent

env = agent.SimpleGameEnv()  # Criando o ambiente da IA
obs = env.reset()  # Reseta o jogo para o estado inicial
print("Estado inicial:", obs)

for _ in range(10):  # Testando 10 movimentos aleatórios
    action = env.action_space.sample()  # Escolhe uma ação aleatória
    obs, reward, done, _ = env.step(action)  # Aplica a ação no ambiente
    print(f"Ação: {action}, Novo Estado: {obs}, Recompensa: {reward}")
    
    if done:  # Se o jogo acabou (exemplo: pegou um tesouro ou morreu), reinicia
        obs = env.reset()
