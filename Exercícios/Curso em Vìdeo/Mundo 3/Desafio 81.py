#Crie um programa que vai ler vários números e colocar em uma lista
#Depois mostre: Quantos números foram digitados; A lista em ordem decrescente; se o número 5 está na lista.
lista = list()
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    cancela = input('Deseja inserir mais números? (S/N)').upper.strip()
    if cancela == 'S':
        print('Ótimo, vamos aumentar nossa lista! ')
    elif cancela == 'N':
        lista = lista.reverse()  
        print(f'Encerrando...\nEssa foi a lista que você criou: {lista}, ela possui {len(lista)} números. ',end='')
        if 5 in lista:
            print('O número 5 foi digitado!')
        break
    else:
        print('Não entendi o valor digitado, vamos continuar então. \n :)')
        continue
