<<<<<<< HEAD

# DungeonMind - Explorador de Masmorra com Inteligência Artificial

## 💡 Ideia do Projeto

O DungeonMind é um projeto educacional que combina jogos e inteligência artificial. O objetivo é treinar um agente para explorar uma masmorra, encontrar tesouros e evitar armadilhas usando algoritmos de aprendizado por reforço.

## ✨ Funcionalidades e Alterações

- Ambiente personalizado baseado em uma grade (dungeon).
- Treinamento de agente com Q-Learning.
- Visualização do ambiente com Pygame.
- Renderização do ambiente e estados do agente.
- Integração entre IA e interface gráfica.

## 🧠 Como Treinar e Testar o Agente

### Treinar o Agente

```bash
python -m IA.train
```

### Executar o Jogo com Controle Manual (Setas)

```bash
python main.py
```

## 📚 Bibliotecas Utilizadas

- `numpy`
- `pygame`
- `gym`

## ⚙️ Algoritmo Aplicado

- Q-Learning (Aprendizado por Reforço)
  - Política epsilon-greedy
  - Tabela Q-Table com atualizações iterativas

## 📐 Cálculos Realizados

- Atualização da Q-table:
  ```python
  Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state]))
  ```
- Cálculo de recompensa com base em eventos (tesouro, armadilha, saída).

## 🚧 Dificuldades Encontradas

- Integração entre ambiente de IA e visualização com Pygame.
- Tratamento de ações inválidas nas bordas da masmorra.
- Controle de exibição e lógica de eventos.

## 📊 Resultados Obtidos

- Treinamento mostra aumento progressivo da recompensa média.
- Agente aprende a evitar armadilhas e alcançar a saída eficientemente.
- Pode ser estendido para níveis mais complexos, múltiplos inimigos e obstáculos dinâmicos.

---

Criado para fins acadêmicos na disciplina de Aprendizado de Máquina.
=======

# DungeonMind - Explorador de Masmorra com Inteligência Artificial

## 💡 Ideia do Projeto

O DungeonMind é um projeto educacional que combina jogos e inteligência artificial. O objetivo é treinar um agente para explorar uma masmorra, encontrar tesouros e evitar armadilhas usando algoritmos de aprendizado por reforço.

## ✨ Funcionalidades e Alterações

- Ambiente personalizado baseado em uma grade (dungeon).
- Treinamento de agente com Q-Learning.
- Visualização do ambiente com Pygame.
- Renderização do ambiente e estados do agente.
- Integração entre IA e interface gráfica.

## 🧠 Como Treinar e Testar o Agente

### Treinar o Agente

```bash
python -m IA.train
```

### Executar o Jogo com Controle Manual (Setas)

```bash
python main.py
```

## 📚 Bibliotecas Utilizadas

- `numpy`
- `pygame`
- `gym`

## ⚙️ Algoritmo Aplicado

- Q-Learning (Aprendizado por Reforço)
  - Política epsilon-greedy
  - Tabela Q-Table com atualizações iterativas

## 📐 Cálculos Realizados

- Atualização da Q-table:
  ```python
  Q[state, action] = (1 - alpha) * Q[state, action] + alpha * (reward + gamma * np.max(Q[new_state]))
  ```
- Cálculo de recompensa com base em eventos (tesouro, armadilha, saída).

## 🚧 Dificuldades Encontradas

- Integração entre ambiente de IA e visualização com Pygame.
- Tratamento de ações inválidas nas bordas da masmorra.
- Controle de exibição e lógica de eventos.

## 📊 Resultados Obtidos

- Treinamento mostra aumento progressivo da recompensa média.
- Agente aprende a evitar armadilhas e alcançar a saída eficientemente.
- Pode ser estendido para níveis mais complexos, múltiplos inimigos e obstáculos dinâmicos.

---

Criado para fins acadêmicos na disciplina de Aprendizado de Máquina.
>>>>>>> b6f05890cf34dcf5b2495004601b651395be2be4
