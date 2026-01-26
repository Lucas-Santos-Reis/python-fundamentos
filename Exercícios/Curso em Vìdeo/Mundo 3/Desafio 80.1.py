#Crie um programa que leia 5 valores númericos e cadastre-os em uma lista, já na posição correta de inserção. (sem usar o sort()), no final, mostre a lista ordenada.
lista = list()
for i in range(0,5):
    num = int(input('Digite um número para adicionar à lista: '))
    if i == 0 or num > lista[-1]: #Coloca o primeiro número ou se maior que o último
        lista.append(num)
    else:
        pos = 0
        while pos < len(lista):
            if i <= lista[pos]:
                lista.insert(pos, num)
                break
            pos += 1

print('=-'*30)
print(f'Prontinho! Arrumei os números que você me entregou:\n{lista}')