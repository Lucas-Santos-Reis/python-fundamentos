# Sabe-se que o CPF é formado por 9 dígitos + 2 dígitos verificadores, então para calcular os dígitos verificadores devemos seguir os seguintes passos:

# Multiplicar os 9 primeiros dígitos pelo índice de sua posição.
# Somar os resultados e dividir por 11 e guardar o resto.
# Exemplo: 123.456.789-09
# 1*1+2*2+3*3+4*4+5*5+6*6+7*7+8*8+9*9 = 285/11 = 25 Resto = 10

# A unidade do resto deverá ser igual ao primeiro digito verificador.
# Repetir passo 1 com os 10 primeiros dígitos, só que agora começando a sequência de multiplicador em zero.
# Exemplo: 1*0+2*1+3*2+4*3+5*4+6*5+7*6+8*7+9*8+0*9= 240/11 = 21
# Resto = 9

# Se o resto for igual ao segundo dígito verificador, e o resto da operação do passo 2 for igual ao primeiro digito verificador, o CPF é correto.
while True:
    cpf = input('Digite o seu CPF: ')
    lista = list()
    soma = 0
#Verifica o primeiro dígito verificador
    for number in cpf: 
        lista.append(int(number))

    for i in range (0,9):
        soma += lista[i] * (i + 1)

    if (soma % 11)%10 != lista[-2]:
        print('O CPF digitado não é válido, por favor, insira novamente')
        continue
#Verifica o segundo dígito verificador
    soma = 0
    for i in range (0,10):
        soma += lista[i] * i
    if (soma % 11)%10 == lista[-1]:
        print('CPF verificado com sucesso!!')
        break
    else:
        print('O CPF digitado não é válido, por favor, insira novamente')
        continue
