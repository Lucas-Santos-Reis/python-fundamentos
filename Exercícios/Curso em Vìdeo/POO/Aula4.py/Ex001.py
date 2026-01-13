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
gafanhoto_1.nome = 'Lucas'
gafanhoto_1.idade = 25
gafanhoto_1.aniversario()
print(gafanhoto_1.mensagem())
gafanhoto_2 = Gafanhoto()
gafanhoto_2.nome = 'João'
gafanhoto_2.idade = 28