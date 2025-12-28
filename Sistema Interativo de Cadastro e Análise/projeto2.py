global cadastros
cadastros = []
def cadastrar_pessoa():
    while True: # Loop infinito para cadastro de pessoas
        nome = input('Digite o nome da pessoa (ou "sair" para encerrar): ')

        if nome.lower() == 'sair':
            break

        idade = int(input(f'Digite a idade do(a) {nome}: '))

        profissao = input(f'Digite a profissão do(a) {nome}: ')

        cadastros.append({'nome': nome.capitalize(), 'idade': idade, 'profissao': profissao.capitalize()})
        print(f'Pessoa {nome} cadastrada com sucesso!')
        print('--------- Próximo Cadastro ----------\n')
def mostrar_cadastros():
    if not cadastros:
        print('Nenhuma pessoa cadastrada.')
        return
    else:
        print('\nPessoas cadastradas:')
        for pessoa in cadastros:
            print(f"Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Profissão: {pessoa['profissao']}")
def analisar_cadastros():
    if not cadastros:
        print('Nenhuma pessoa cadastrada para análise...')
        return
    else:
        while True:
            analise = input('''
        Qual análise deseja realizar?
        1: Obter lista de cadastros;
        2: Idade média; 
        3: Profissão mais comum; 
        4: Pessoas na maioridade;
        5: Voltar ao menu principal (cadastro de pessoas).
        Escolha uma opção (1-5): 
                            
                            ''')
            if analise == '1':
                mostrar_cadastros()
            elif analise == '2':
                soma_idade = 0
                for pessoa in cadastros:
                    soma_idade += pessoa['idade']
                idade_media = soma_idade / len(cadastros)
                print(f'Idade média das pessoas cadastradas: {idade_media:.0f} anos')
            elif analise == '3':
                mais_comum = ''
                maior_quantidade = 0
                profissoes = {} # Dicionário para contar profissões 
                #key = profissao, value = quantidade de pessoas
                for pessoa in cadastros:
                    profissao = pessoa['profissao']
                    if profissao in profissoes:
                        profissoes[profissao] += 1
                    else:
                        profissoes[profissao] = 1
                for profissao, quantidade in profissoes.items():
                    #for key, value in dict.items()
                    #verifica qual profissão tem maior quantidade
                    if quantidade > maior_quantidade:
                        maior_quantidade = quantidade
                        mais_comum = profissao
                print(f'Profissão mais comum: {mais_comum} com {maior_quantidade} pessoas cadastradas.')
            elif analise == '4':
                maiores = 0
                for pessoa in cadastros:
                    if pessoa['idade'] >= 18:
                        maiores += 1
                print(f'Número de pessoas na maioridade cadastradas: {maiores}')
            elif analise == '5':
                break
            else:
                print('Opção inválida. Tente novamente.')
#Sistema Interativo de Cadastro e Análise

print('Bem-vindo ao Sistema Interativo de Cadastro e Análise!')
while True:
    cadastrar_pessoa()
    analisar_cadastros()
    sair = input('Deseja encerrar o programa? (s/n): ')
    if sair.lower() == 's':
        print('Encerrando o programa. Até mais!')
        break