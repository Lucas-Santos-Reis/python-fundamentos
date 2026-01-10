#Crie um programa que leia o nome de uma cidade/estado e verifica se ela começa com 'SANTO'
cidade:str = input('Digite o nome de uma cidade').strip().upper()
print(cidade[0:5] == 'SANTO')

