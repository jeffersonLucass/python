from Carrinho import Carrinho
from tabulate import tabulate
class Loja:
    def __init__(self):
        self.produtos = []
        self.carrinho = Carrinho()

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def exibir_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado.")
        else:
            dados = [[produto.nome, produto.preco, produto.quantidade] for produto in self.produtos]
            
            cabecalhos = ["Nome", "Preço", "Estoque"]
            
            print(tabulate(dados, headers=cabecalhos, tablefmt="grid"))

    def processar_pagamento(self, valor_pago):
        total = self.carrinho.calcular_total()
        if valor_pago >= total:
            troco = valor_pago - total
            self.carrinho.esvaziar()
            print(f"Pagamento realizado com sucesso! Troco: {troco}")
        else:
            print("Pagamento insuficiente.")