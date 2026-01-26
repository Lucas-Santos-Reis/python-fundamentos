#Crie um programa que leia 5 valores númericos e cadastre-os em uma lista, já na posição correta de inserção. (sem usar o sort()), no final, mostre a lista ordenada.
lista = list()
for i in range(0,5):
    num = input('Digite um número para adicionar à lista: ')
    lista.append(int(num))

for i in range(len(lista)-1): #Ordena os números
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            lista[i], lista[i+1] = lista[i+1], lista[i]

print('=-'*30)
print(f'Prontinho! Arrumei os números que você me entregou:\n{lista}')