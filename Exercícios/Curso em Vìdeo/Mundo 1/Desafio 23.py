num:int= int(input('Digite um número entre 0 e 9999: '))
unidades = num // 1 % 10 
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhares = num // 1000 % 10

print(f'O número digitado possui \n {unidades} Unidade(s) \n {dezenas} Dezena(s) \n {centenas} Centena(s) \n e {milhares} Milhar(es).')