class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def aplicar_desconto(self, percentual):
        self.preco -= self.preco * (percentual / 100)