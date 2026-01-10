#crie o nome de um programa que diga se uma pessoa tem o 'SILVA' no nome
nome:str = input('Digite seu nome completo: ').strip().upper()
print('SILVA' in nome.split())