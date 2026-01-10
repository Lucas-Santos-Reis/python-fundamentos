#Crie um programa que leia uma frase e diga:
#Quantas vezes a letra 'a' aparece
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela última vez
frase:str = input('Digite uma frase: ').lower().strip()
print(f'A frase digitada possui {frase.count('a')} letras "a"')
print(f'A primeira vez que a letra "a" aparece é na posição {frase.find('a')} e aparece pela última vez na posição {frase.rfind('a')}')