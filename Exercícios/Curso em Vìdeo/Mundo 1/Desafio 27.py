#Faça um programa que leia o nome de uma pessoa e diga o seu primeiro nome e o seu último nome
nome:str = input('Digite seu nome completo: ').capitalize().strip()
nome_separado = nome.split()
print(f'Prazer em conhecer você senhor {nome_separado[0]} {nome_separado[-1]}')