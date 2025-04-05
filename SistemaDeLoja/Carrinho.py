class Carrinho:
    def __init__(self):
        self.itens = []  


    def adicionar_produto(self, produto, quantidade):
        if produto.quantidade >= quantidade:
            self.itens.append((produto, quantidade)) 
            produto.quantidade -= quantidade
        else:
            print(f"Estoque insuficiente para {produto.nome}")
    

    def calcular_total(self):
        total =  sum(produto.preco * quantidade for produto, quantidade in self.itens)   
        return total 
    
    def esvaziar(self):
        self.itens = [] 