#Declaração de classes:
class Gafanhoto:
    def __init__(self): #método construtor -> define atributos de instância
        self.nome = ''
        self.idade = 0
    #Métodos de identação:
    def aniversario (self):
        self.idade += 1
    def mensagem (self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

#Declaração de objetos:
gafanhoto_1 = Gafanhoto() #instânciação
print(gafanhoto_1.mensagem())