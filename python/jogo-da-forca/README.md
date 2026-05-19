# Jogo da Forca - Python

Um jogo interativo e educacional da forca implementado em Python puro, com foco em boas práticas de programação e código limpo.

## Descrição

O Jogo da Forca é um clássico jogo de adivinhação onde o jogador tenta adivinhar uma palavra secreta revelando uma letra por vez. O jogador tem um número limitado de tentativas (6) para descobrir a palavra completa antes de perder o jogo.

### Características Principais

- Totalmente funcional - Jogo interativo com validação de entrada
- Código limpo - Segue PEP 8 e convenções Python
- Bem documentado - Docstrings completas em todas as funções
- Estrutura modular - Funções separadas por responsabilidade
- Eficiente - Uso otimizado de estruturas de dados (Sets)
- Educacional - Ideal para aprender Python OOP e lógica de programação

## Como Executar

### Pré-requisitos
- Python 3.7+
- Nenhuma dependência externa (apenas biblioteca padrão)

### Instalação e Execução

```bash
# 1. Clone o repositório (ou faça download dos arquivos)
git clone https://github.com/rafaeldominguess/estudos.git
cd estudos/python/jogo-da-forca

# 2. Execute o jogo
python jogo_forca.py
```

## Estrutura do Código

### Funções Principais

- inicializar_jogo() - Preparação inicial - sorteia palavra e cria estruturas de dados
- processar_tentativa() - Processa o palpite do jogador e atualiza o estado
- validar_entrada() - Valida se a entrada é uma letra válida e não foi tentada
- exibir_estado_jogo() - Exibe o estado atual do jogo na tela
- verificar_vitoria() - Verifica se o jogador ganhou
- main() - Loop principal que controla o fluxo do jogo

## Detalhes de Implementação

### Uso Eficiente de Sets

A estrutura de dados Set foi escolhida para letras_tentadas por suas vantagens:

- Busca O(1) vs O(n) em lista
- Ignora automaticamente duplicatas
- Operações otimizadas em C
- Semanticamente representa "valores únicos"

### Nomenclatura
- snake_case para variáveis e funções: palavra_secreta, letras_tentadas
- UPPER_CASE para constantes: PALAVRAS_SECRETAS

### Identação
- 4 espaços por nível de indentação (padrão PEP 8)
- Sem tabulações (apenas espaços)

## Requisitos Atendidos

- Lista pré-definida de palavras (PALAVRAS_SECRETAS)
- Sorteio aleatório com random.choice()
- Importação correta de módulos (import random)
- Validação de entrada do jogador
- Lógica de jogo completa (vitória/derrota)
- Interface amigável com feedback visual
- Código documentado e bem estruturado

## Autor

Rafael Domingues  
Repositório: https://github.com/rafaeldominguess/estudos

---

Status: Completo e Pronto para Produção