#Crie uma classe funcionário, onde podemos cadastrar nome, setor e cargo.
#Crie também um método para ele se apresentar
class Funcionario:
    #Atributos de classe
    empresa = 'Curso em Vídeo'
    #Atributos de instância
    def __init__(self, nome:str, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentação (self) -> str: 
        return f'Olá, me chamo {self.nome}, e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}'
    

#objetos
c1 = Funcionario('Maria', 'Adminstração', 'Diretora')
print(c1.apresentação())
c2 = Funcionario('Pedro', 'TI', 'Programador')
print(c2.apresentação())