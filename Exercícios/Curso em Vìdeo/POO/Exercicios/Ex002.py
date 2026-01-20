#Declaração de classes:
class Gafanhoto:
    '''
    Manual da Classe: Essa classe cria um gafanhoto, que é uma pessoa com nome e idade fã de aprender.

    Para criar um gafanhoto basta:
    variavel = Gafanhoto (nome, idade)
    '''
    def __init__(self, nome:str = 'Vazio', idade:int = 0): #self -> método construtor -> define atributos de instância

        self.nome = nome
        self.idade = idade
        #self.atributo = valor 
    
    #Método de identação:
    def aniversario (self):
        self.idade += 1

    #Método dunder string
    def __str__(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'
    #Método dunder getstate
    def __getstate__(self):
        return f'Nome: {self.nome} \n Idade: {self.idade}'

#Declaração de objetos:
gafanhoto_1 = Gafanhoto('Lucas', 25) #instânciação
gafanhoto_1.aniversario()
print(gafanhoto_1) #chama o método dunder string
gafanhoto_2 = Gafanhoto('João', 28)
print(gafanhoto_2.__getstate__())