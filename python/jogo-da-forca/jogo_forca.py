"""
JOGO DA FORCA - Versão Final
Implementação completa do clássico jogo da forca em Python.

Descrição:
    Jogo interativo onde o jogador tenta adivinhar uma palavra secreta
    letterizada, tendo um número limitado de tentativas. A cada letra
    correta, ela aparece revelada na palavra. Ao alcançar o limite de
    erros, o jogo termina com derrota.

Requisitos Atendidos:
    ✓ Convenções Python (snake_case)
    ✓ Docstrings detalhadas em todas as funções
    ✓ Comentários justificando o uso de Sets
    ✓ Lógica sem erros de sintaxe
    ✓ Estrutura modular e reutilizável
"""

import random


# ============================================================================
# DADOS GLOBAIS - PALAVRAS PRÉ-DEFINIDAS
# ============================================================================

PALAVRAS_SECRETAS = [
    "PYTHON",
    "PROGRAMACAO",
    "ESTRUTURA",
    "ALGORITMO",
    "VARIAVEL",
    "FUNCAO",
    "COMPUTADOR",
    "DESENVOLVIMENTO"
]


# ============================================================================
# FUNÇÃO: INICIALIZAR JOGO
# ============================================================================

def inicializar_jogo(lista_de_palavras):
    """
    Inicializa uma nova partida do jogo da forca.
    
    Seleciona aleatoriamente uma palavra da lista fornecida e prepara
    as estruturas de dados necessárias para rastrear o progresso do jogo.
    
    Args:
        lista_de_palavras (list): Lista de palavras candidatas ao sorteio.
        
    Returns:
        tuple: Uma tupla contendo:
            - palavra_secreta (str): A palavra que deve ser adivinhada
            - palavra_mascarada (list): Lista de caracteres revelados/ocultos
            - letras_tentadas (set): Conjunto de letras já tentadas
            
    Exemplo:
        >>> palavra, máscara, tentadas = inicializar_jogo(PALAVRAS_SECRETAS)
        >>> print(máscara)  # ['_', '_', '_', '_', '_', '_']
    """
    # Sorteia uma palavra aleatória da lista fornecida
    palavra_secreta = random.choice(lista_de_palavras)
    
    # Cria uma lista com underscores para cada letra da palavra
    # Inicialmente, todas as letras estão ocultas
    palavra_mascarada = ["_"] * len(palavra_secreta)
    
    # Inicializa um conjunto vazio para rastrear as letras tentadas
    # JUSTIFICATIVA - USO DE SET: Um conjunto (set) é mais eficiente que uma
    # lista para esta finalidade porque:
    #   1. Busca O(1): verify se uma letra foi tentada em tempo constante
    #      vs lista que seria O(n)
    #   2. Sem duplicatas: o set automaticamente ignora duplicatas,
    #      evitando lógica adicional
    #   3. Operações: operações com conjuntos (union, intersection) são
    #      otimizadas em C no interpretador Python
    #   4. Legibilidade: semanticamente, um conjunto representa melhor
    #      "um grupo de valores únicos" do que uma lista
    letras_tentadas = set()
    
    return palavra_secreta, palavra_mascarada, letras_tentadas


# ============================================================================
# FUNÇÃO: PROCESSAR TENTATIVA
# ============================================================================

def processar_tentativa(letra, palavra_secreta, palavra_mascarada, letras_tentadas):
    """
    Processa um palpite do jogador e atualiza o estado do jogo.
    
    Verifica se a letra fornecida existe na palavra secreta. Se existir,
    revela todas as posições onde a letra aparece. Se não existir, apenas
    registra a tentativa como erro.
    
    Args:
        letra (str): A letra que o jogador está tentando adivinhar.
        palavra_secreta (str): A palavra que deve ser descoberta.
        palavra_mascarada (list): Lista atual com a palavra parcialmente revelada.
        letras_tentadas (set): Conjunto de letras já tentadas (atualizado nesta função).
        
    Returns:
        bool: True se a letra está na palavra (acerto), False caso contrário (erro).
        
    Efeitos Colaterais:
        - Modifica `palavra_mascarada` revelando novas letras se houver acerto
        - Modifica `letras_tentadas` adicionando a nova letra
        
    Exemplo:
        >>> acertou = processar_tentativa('A', 'PYTHON', ['_','_','_','_','_','_'], set())
        >>> print(acertou)  # False (pois 'A' não está em 'PYTHON')
    """
    # Adiciona a letra ao conjunto de tentativas
    # Se ela já existir, o set ignora silenciosamente (sem duplicatas)
    letras_tentadas.add(letra)
    
    # Verifica se a letra existe na palavra secreta
    if letra in palavra_secreta:
        # Itera sobre cada posição e caractere da palavra
        for indice, caractere in enumerate(palavra_secreta):
            # Se o caractere nessa posição coincide com a letra tentada:
            if caractere == letra:
                # Revela o caractere na palavra_mascarada
                palavra_mascarada[indice] = letra
        
        # Retorna True indicando que houve acerto
        return True
    
    # Se chegou aqui, a letra NÃO está na palavra
    return False


# ============================================================================
# FUNÇÃO: EXIBIR ESTADO DO JOGO
# ============================================================================

def exibir_estado_jogo(palavra_mascarada, letras_tentadas, tentativas_restantes):
    """
    Exibe o estado atual da partida na tela do jogador.
    
    Mostra a palavra parcialmente revelada, as letras já tentadas e
    o número de tentativas ainda disponíveis. Fornece feedback visual
    claro sobre o progresso do jogo.
    
    Args:
        palavra_mascarada (list): Lista com a palavra parcialmente revelada.
        letras_tentadas (set): Conjunto de letras já tentadas.
        tentativas_restantes (int): Número de tentativas que ainda restam.
        
    Returns:
        None (apenas exibe informações)
        
    Exemplo:
        >>> exibir_estado_jogo(['P','_','_','H','O','N'], {'P','O','N'}, 4)
        # Exibe formatado com bordas
    """
    # Cabeçalho formatado
    print("\n" + "=" * 50)
    
    # Exibe a palavra com espaço entre as letras para melhor legibilidade
    print("Palavra: " + " ".join(palavra_mascarada))
    
    # Exibe quantas tentativas ainda restam
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Exibe as letras já tentadas (ordenadas para padronização)
    # Se nenhuma letra foi tentada, exibe "nenhuma"
    letras_str = ', '.join(sorted(letras_tentadas)) if letras_tentadas else 'nenhuma'
    print(f"Letras já tentadas: {letras_str}")
    
    # Rodapé formatado
    print("=" * 50)


# ============================================================================
# FUNÇÃO: VALIDAR ENTRADA DO JOGADOR
# ============================================================================

def validar_entrada(letra, letras_tentadas):
    """
    Valida a entrada do jogador antes de processá-la.
    
    Verifica se:
        1. É exatamente um caractere
        2. É uma letra (não número ou símbolo)
        3. Não foi tentada anteriormente
    
    Args:
        letra (str): A letra digitada pelo jogador.
        letras_tentadas (set): Conjunto de letras já tentadas.
        
    Returns:
        tuple: (bool, str) onde:
            - bool: True se a entrada é válida, False caso contrário
            - str: Mensagem explicando a validação (se inválida)
            
    Exemplo:
        >>> valido, msg = validar_entrada('A', set())
        >>> print(valido)  # True
    """
    # Verifica se é exatamente um caractere e se é uma letra
    if len(letra) != 1 or not letra.isalpha():
        return False, "Digite apenas uma letra!"
    
    # Verifica se a letra já foi tentada
    if letra in letras_tentadas:
        return False, "Você já tentou essa letra!"
    
    # Todas as validações passaram
    return True, ""


# ============================================================================
# FUNÇÃO: VERIFICAR CONDIÇÃO DE VITÓRIA
# ============================================================================

def verificar_vitoria(palavra_mascarada):
    """
    Verifica se o jogador adivinhou toda a palavra.
    
    Analisa se ainda existe algum underscore (letra oculta) na
    palavra_mascarada. Se não houver nenhum, significa que todas
    as letras foram reveladas.
    
    Args:
        palavra_mascarada (list): Lista com a palavra parcialmente revelada.
        
    Returns:
        bool: True se todas as letras foram descobertas, False caso contrário.
        
    Exemplo:
        >>> vencer = verificar_vitoria(['P','Y','T','H','O','N'])
        >>> print(vencer)  # True
    """
    # Se não houver underscore, significa que a palavra foi completamente revelada
    return "_" not in palavra_mascarada


# ============================================================================
# FUNÇÃO: FUNÇÃO PRINCIPAL (LOOP DO JOGO)
# ============================================================================

def main():
    """
    Função principal que controla o fluxo completo do jogo.
    
    Orquestra todas as operações do jogo: inicialização, loop principal
    com processamento de entradas, verificação de condições de vitória/derrota
    e exibição de mensagens finais.
    
    Fluxo:
        1. Inicializa uma nova partida
        2. Entra no loop principal enquanto o jogo estiver ativo
        3. Exibe o estado atual
        4. Coleta entrada do jogador
        5. Valida a entrada
        6. Processa a tentativa
        7. Verifica condições de término (vitória ou derrota)
        8. Exibe resultado final
        
    Returns:
        None (Jogo é interativo com o usuário)
    """
    # Exibe mensagem de boas-vindas
    print("\n" + "=" * 50)
    print("BEM-VINDO AO JOGO DA FORCA!")
    print("=" * 50)
    print("Você tem 6 tentativas para adivinhar a palavra secreta.")
    print("Cada letra errada reduz suas tentativas restantes.\n")
    
    # Inicializa o jogo com uma palavra aleatória
    palavra_secreta, palavra_mascarada, letras_tentadas = inicializar_jogo(PALAVRAS_SECRETAS)
    tentativas_restantes = 6
    jogo_ativo = True
    
    # Loop principal do jogo
    while jogo_ativo:
        # Exibe o estado atual da partida
        exibir_estado_jogo(palavra_mascarada, letras_tentadas, tentativas_restantes)
        
        # Coleta a entrada do jogador e converte para maiúscula
        letra = input("\nDigite uma letra: ").upper()
        
        # Valida a entrada do jogador
        entrada_valida, mensagem_erro = validar_entrada(letra, letras_tentadas)
        
        if not entrada_valida:
            # Se a entrada não é válida, exibe mensagem e continua
            print(mensagem_erro)
            continue
        
        # Processa a tentativa e verifica se acertou
        acertou = processar_tentativa(letra, palavra_secreta, palavra_mascarada, letras_tentadas)
        
        # Feedback sobre a tentativa
        if not acertou:
            tentativas_restantes -= 1
            print(f"Errou! A letra '{letra}' não está na palavra!")
        else:
            print(f"Acertou! A letra '{letra}' está na palavra!")
        
        # Verifica se o jogador venceu
        if verificar_vitoria(palavra_mascarada):
            print(f"\nPARABENS! Você adivinhou a palavra: {''.join(palavra_mascarada)}")
            print("VOCÊ VENCEU!\n")
            jogo_ativo = False
        
        # Verifica se o jogador perdeu (tentativas esgotadas)
        elif tentativas_restantes == 0:
            print(f"\nGAME OVER! A palavra era: {palavra_secreta}")
            print("VOCÊ PERDEU!\n")
            jogo_ativo = False


# ============================================================================
# PONTO DE ENTRADA DO PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Ponto de entrada do script. Garante que main() seja executada apenas
    quando o arquivo é rodado diretamente, não quando importado como módulo.
    """
    main()