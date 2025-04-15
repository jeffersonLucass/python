from Produto import Produto
from Loja import Loja

def menu():
    loja = Loja()

    loja.adicionar_produto(Produto("Camiseta", 50, 10))
    loja.adicionar_produto(Produto("Calça", 100, 5))
    loja.adicionar_produto(Produto("Boné", 30, 20))
    loja.adicionar_produto(Produto("Tênis", 150, 8))
    loja.adicionar_produto(Produto("Jaqueta", 200, 3))
    loja.adicionar_produto(Produto("Meias", 10, 50))
    loja.adicionar_produto(Produto("Relógio", 250, 2))
    loja.adicionar_produto(Produto("Óculos de Sol", 120, 7))
    loja.adicionar_produto(Produto("Mochila", 80, 6))
    loja.adicionar_produto(Produto("Carteira", 40, 15))

    while True: 
        print("\n1. Exibir produtos")
        print("2. Adicionar produto ao carrinho")
        print("3. Aplicar desconto manual")
        print("4. Visualizar carrinho")
        print("5. Finalizar compra")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            loja.exibir_produtos()
        
        elif opcao == '2':
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade: "))
            produto = next((produto for produto in loja.produtos if produto.nome == nome), None)
            if produto:
                loja.carrinho.adicionar_produto(produto, quantidade)
            else:
                print("Produto não encontrado.")
        
        elif opcao == '3':
            nome = input("Digite o nome do produto: ")
            percentual = float(input("Digite o percentual de desconto: "))
            produto = next((produto for produto in loja.produtos if produto.nome == nome), None)
            if produto:
                produto.aplicar_desconto(percentual)
            else:
                print("Produto não encontrado.")
        
        elif opcao == '4':
            total = loja.carrinho.calcular_total()
            print(f"Total do carrinho: R$ {total:.2f}")
        
        elif opcao == '5':
            print("Formas de pagamento:")
            print("1 - Dinheiro (10% de desconto)")
            print("2 - Pix (10% de desconto)")
            print("3 - Cartão (5% de acréscimo se parcelado)")

            forma = input("Escolha a forma de pagamento: ")
            total = loja.carrinho.calcular_total()

            if forma in ['1', '2']:
                total *= 0.9
                print(f"Total com desconto: R$ {total:.2f}")
            elif forma == '3':
                parcelas = int(input("Digite o número de parcelas: "))
                if parcelas > 1:
                    total *= 1.05
                    print(f"Total com acréscimo: R$ {total:.2f} em {parcelas}x")
                else:
                    print(f"Total a pagar: R$ {total:.2f}")
            else:
                print("Forma de pagamento inválida.")
                continue

            valor_pago = float(input("Digite o valor pago: "))
            loja.processar_pagamento(valor_pago, total)
        
        elif opcao == '6':
            break
        else:
            print("Opção inválida.")

menu()
