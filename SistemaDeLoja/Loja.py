from Carrinho import Carrinho

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
            for produto in self.produtos:
                print(f"Nome: {produto.nome}, Preço: {produto.preco}, Estoque: {produto.quantidade}")

    def processar_pagamento(self, valor_pago):
        total = self.carrinho.calcular_total()
        if valor_pago >= total:
            troco = valor_pago - total
            self.carrinho.esvaziar()
            print(f"Pagamento realizado com sucesso! Troco: {troco}")
        else:
            print("Pagamento insuficiente.")