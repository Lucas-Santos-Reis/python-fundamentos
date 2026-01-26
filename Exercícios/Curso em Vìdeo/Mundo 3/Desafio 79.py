#Crie um programa onde o usuário possa digitar vários valores numéricos e os cadastrar em uma lista:
#Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os números digitados em ordem crescente
from time import sleep
lista = list()
while True:
    num = input('Digite um número que você deseja adicionar à lista: ')
    if int(num) not in lista:
        lista.append(int(num))
        sleep(1)
        print(f'O valor {num} foi adicionado com sucesso!')
    else:
        print(f'O número {num} já está na lista... ')
    
    continuar = input('Deseja continuar adicionando mais números? (S/N) ')
    if continuar in ['S','s']:
        sleep(1)
        print('Ótimo, vamos aumentar nossa lista! ')
        continue
    elif continuar in ['N','n']:
        sleep(1)
        print('=-'*30)
        sleep(2)
        print(f'Encerrando...\nEssa foi a lista que você criou: {sorted(lista)}')
        break
    else:
        sleep(2)
        print('Não entendi o valor digitado, vamos continuar então. \n :)')
        continue