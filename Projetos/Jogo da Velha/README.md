# Jogo da Velha em Python 🕹️

Este repositório contém duas versões de um **Jogo da Velha desenvolvido em Python**, criado como parte do meu processo de aprendizado em programação.

O projeto teve início como um **desafio final do curso _“Fundamentos de Python 1” da Cisco Networking Academy_**, sendo posteriormente **refatorado e modularizado** com o objetivo de melhorar organização, legibilidade e manutenção do código.

---

## 📌 Objetivo do Projeto

- Consolidar conceitos fundamentais de Python
- Exercitar lógica de programação
- Evoluir de um código linear para uma estrutura modular
- Aplicar boas práticas iniciais de organização de projetos
- Servir como base para futuras refatorações usando **Programação Orientada a Objetos (POO)**

---

## 🧩 Estrutura do Projeto
# projeto1.py - projeto inicial desenvolvido antes de aprender sobre modularização

# refactor
├── main.py - arquivo principal
├── rule.py - regras do jogo
└── README.md

### `main.py`
Responsável pelo:
- Controle do fluxo principal do jogo
- Loop de execução
- Interação entre jogador e computador
- Chamadas às funções definidas em `rule.py`

### `rule.py`
Responsável por:
- Regras do jogo
- Manipulação do tabuleiro
- Verificação de vitória e empate
- Controle de placar
- Funções auxiliares (exibição do tabuleiro, reset, jogadas)



## 🔄 Evolução do Projeto

### 🔹 Versão 1 — Código Linear
- Código único em um arquivo
- Uso intensivo de variáveis globais
- Funções misturando lógica, exibição e controle
- Foco em resolver o problema funcionalmente

👉 **Objetivo:** aprender a programar e concluir o desafio do curso.


### 🔹 Versão 2 — Código Modular (Atual)
- Separação clara entre lógica (`rule.py`) e controle (`main.py`)
- Redução de responsabilidades por função
- Melhor legibilidade e manutenção
- Estrutura mais próxima de projetos reais em Python
- Preparação para futura migração para POO

👉 **Objetivo:** melhorar qualidade do código e aplicar conceitos de modularização.


## 🧠 Conceitos Trabalhados

- Estruturas de controle (`if`, `while`, `for`)
- Listas e matrizes
- Funções e parâmetros
- Modularização em Python
- Importação de módulos
- Lógica de jogos
- Validação de entrada do usuário

---

## 🚀 Próximos Passos - Versão 3

Este projeto **não está finalizado**.

As próximas evoluções planejadas incluem:
- Refatoração completa utilizando **Programação Orientada a Objetos (POO)**
- Criação de classes como `Jogo`, `Tabuleiro` e `Jogador`
- Remoção de variáveis globais
- Implementação de uma IA mais estratégica para o computador
- Expansão para outras variações do jogo

Essas melhorias serão realizadas em um **novo projeto**, mantendo este repositório como registro da evolução inicial.

---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/jogo-da-velha-python.git
