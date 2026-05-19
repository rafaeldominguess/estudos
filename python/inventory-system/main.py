estoque = [
    {
        "nome": "Tomate",
        "quantidade": 4,
        "preco": 12.99
    },
    {
        "nome": "Banana",
        "quantidade": 8,
        "preco": 10.90
    },
    {
        "nome": "Laranja",
        "quantidade": 10,
        "preco": 14.75
    }
]

# Mensagens do menu (constantes)
opcao_visualizar = "1 - Visualizar Estoque Atual"
opcao_entrada = "2 - Registrar Entrada de Produto"
opcao_saida = "3 - Registrar Saída de Produto"
opcao_sair = "4 - Sair do Sistema"


while True:
    print("Escolha uma das opções:")
    print(opcao_visualizar)
    print(opcao_entrada)
    print(opcao_saida)
    print(opcao_sair)

    escolha_usuario = input("Digite sua escolha: ")
    
    # Opção 1: Visualizar todos os produtos em estoque
    if escolha_usuario == "1":
        for produto in estoque:
            print(f"Nome: {produto['nome']} | Qtd: {produto['quantidade']} | Preço: R$ {produto['preco']}")
    
    # Opção 2: Adicionar quantidade a um produto existente
    elif escolha_usuario == "2":
        nome_produto = input("Digite o nome do produto: ")
        
        for produto in estoque:
            if produto["nome"] == nome_produto:
                while True:
                    quantidade_solicitada = input("Digite a quantidade: ")
                    # Valida se a entrada contém apenas dígitos
                    if quantidade_solicitada.isdigit():
                        quantidade_solicitada = int(quantidade_solicitada)
                        produto["quantidade"] += quantidade_solicitada
                        print(f"Entrada registrada!")
                        break
                    else:
                        print("Erro! Digite apenas números!")
                break
        else:
            print("Produto não encontrado!")
    
    # Opção 3: Remover quantidade de um produto (com validações de estoque)
    elif escolha_usuario == "3":
        nome_produto = input("Digite o nome do produto: ")
        
        # Primeira validação: verifica se o produto existe
        for produto in estoque:
            if produto["nome"] == nome_produto:
                while True:
                    quantidade_solicitada = input("Digite a quantidade a remover: ")
                    # Valida se a entrada contém apenas dígitos
                    if quantidade_solicitada.isdigit():
                        quantidade_solicitada = int(quantidade_solicitada)
                        # Segunda validação: verifica se há quantidade suficiente no estoque
                        if quantidade_solicitada <= produto["quantidade"]:
                            produto["quantidade"] -= quantidade_solicitada
                            print(f"Saída registrada!")
                            break
                        else:
                            # Avisa quantidade insuficiente e não realiza a operação
                            print(f"Estoque insuficiente")
                    else:
                        print("Erro! Digite apenas números!")
                break
        else:
            print("Produto não encontrado!")

    # Opção 4: Encerrar o sistema com integridade
    elif escolha_usuario == "4":
        print("Encerrando o sistema...")
        break
    
    # Fallback: qualquer entrada não prevista é tratada
    else:
        print("Opção inválida! Digite uma das opções (1, 2, 3 ou 4).")
