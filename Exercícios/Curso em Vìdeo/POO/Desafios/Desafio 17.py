#Crie a classe produto onde é possível cadastrar nome e preço.
#Crie também um método que mostre uma etiqueta de preço do produto

class Produto():
    def __init__(self, nome:str, preço:float):
        self.nome = nome
        self.preco = float(preço)
    
    def etiqueta(self):
        return f'''
|__________Produto___________|
|        {self.nome}         |
|----------------------------|
|     R${self.preco}      |
|____________________________|
'''
    


p1 = Produto('Iphone PRO MAX', 25000)
p2 = Produto('PC Gamer', 5000)
print(p1.etiqueta())
print(p2.etiqueta())