#Faça um programa que leia 5 números e guarde-os em uma lista.
#Mostre qual é o maior, o menor e a posição desses números na lista.
lista = list()
maior = 0
menor = 0
for i in range (0,5): #Cria a lista com os 5 números e acha o maior/menor
    número = int(input(f'Digite um número inteiro para a posição {i}: '))
    lista.append(número)
    if i == 0:
        maior = menor = lista[i]
    elif lista[i] > maior:
        maior = lista[i]
    elif lista[i] < menor:
        menor = lista[i]

pos_maior = list()
pos_menor = list()
for pos, num in enumerate(lista): #Acha a posição dos números
    if num == maior:
        pos_maior.append(pos)
    elif num == menor:
        pos_menor.append(pos)
    
print('+='*30)
print(f'Você digitou os valores {lista}')

#Exibe o resultado
print(f'A lista que você criou possui {len(lista)} números\nO maior número é o {maior} que aparece na(s) posição(s) {pos_maior}, o menor número é o {menor} que aparece na(s) posição(s) {pos_menor}.')