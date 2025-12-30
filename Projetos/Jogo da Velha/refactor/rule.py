player = 0
pc = 0
draw = 0

def bg_format(board):  # formato do tabuleiro
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def player_move(board):
    ok = False
    while not ok:
        move = input('Insira a posição que você deseja jogar: ')
        if len(move) == 1 and '1' <= move <= '9':
            move = int(move) - 1
            row = move // 3  # possíveis resultados (0, 0, 0, 1, 1, 1, 2, 2, 2)
            column = move % 3  # possíveis resultados (0, 1, 2, 0, 1, 2, 0, 1, 2)
            check = board[row][column]  # Verifica o que tem na matriz
            if check in ['X', 'O']:
                print('Essa posição já foi escolhida. . . ')
                continue
            else:
                board[row][column] = 'O'
                ok = True
                bg_format(board)
        elif move.lower() in ['sair', 'cancela', 'exit']:
            print('Jogo Encerrado. . . ')
            return 'fim'
        else:
            print('Jogada inválida. . . ')

def pc_move(board):
    from random import randint
    ok = False
    while not ok:
        move = randint(1,9) - 1
        row = move // 3  # possíveis resultados (0, 0, 0, 1, 1, 1, 3, 3, 3)
        column = move % 3  # possíveis resultados (0, 1, 2, 0, 1, 2, 0, 1, 2)
        check = board[row][column]  # Verifica o que tem na matriz
        if check in ['X', 'O']:
            continue
        else:
            board[row][column] = 'X'
            ok = True
            bg_format(board)

def check_win(sign):
    global draw
    if board[0] == [sign, sign, sign] or board[1] == [sign, sign, sign] or board[2] == [sign, sign, sign]:  # Linhas
        return True
    elif board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:  # Diagonal 1
        return True
    elif board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:  # Diagonal 2
        return True
    for i in range(3):  # Colunas
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return True
    full = all(isinstance(cell, str) for row in board for cell in row)
    if full:
        print("Empate! Deu velha!.")
        draw += 1
        reset()

def score(sign):
    global player, pc
    if sign == 'O':
        print('Você VENCEU!!! Parabéns. . . ')
        player += 1
    elif sign == 'X':
        print('HA HA HA, você PERDEU!!! Como pôde HA HA HA ')
        pc += 1

    print(f'''Partida finalizada!
    Placar atual:       Usuário {player}:{pc} Computador
    Empates: {draw}
    Partidas Jogadas: {player + pc + draw}''')
    reset()

def reset():
    global board
    for row in range(3):
        for col in range(3):
            board[row][col] = 3 * row + col + 1  #reescreve a matriz board
    bg_format(board)
#chatGPT me ajudou aqui, não adianta criar um novo objeto, ou deletar o antigo porque o python ainda guarda a variável antiga dentro da função 'mãe'
#Mesmo assim, eu implementei um sistema diferente para sair do problema (realizei mais chamados de função invés de funções sobre funções)

board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]  # cria a matriz [[1, 2, 3],[4, 5, 6],[7, 8, 9]]