#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas..
#- O nome com todas as letras minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome:str = input('Digite seu nome completo: ').strip() #Recebe o nome sem espaços antes e depois.
print(f'O seu NOME é: {nome.upper()}') #Mostra o nome maiúsculo
print(f'O seu nome é {nome.lower()}') #Mostra o nome 
nome_sem_espaço = nome.split() #Separa cada palavra do nome
print(f'O seu nome inteiro é {nome.capitalize()} e possui {(len(nome) - nome.count(' '))} letras')
print(f'O seu primeiro é {nome_sem_espaço[0]} e possui {len(nome_sem_espaço[0])} letras')
#Mostra a quantidade de letras do primeiro nome