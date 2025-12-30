#Variáveis:
movim = []
board = []
empyt = ' '
maq_point = 0
usuario = 0
draw = 0
#Funções:
def bg_format():
  print("+-------" * 3,"+", sep="")
  for row in range(3):
    print("|       " * 3,"|", sep="")
    for col in range(3):
      print("|   " + str(board[row][col]) + "   ", end="")
    print("|")
    print("|       " * 3,"|",sep="")
    print("+-------" * 3,"+",sep="")

def posicao (): #escolha do usuário
  ok = False #força a entrada do loop
  while not ok:
    posicao = input('Escolha a posição que você deseja jogar... ')
    ok = len(posicao) == 1 and posicao >= '1' and posicao <= '9'
    if not ok:
      print('Você digitou um valor inválido... ')
      continue
    elif int(posicao) in movim:
      print('Essa posição já foi escolhida, tente outra...')
      continue
    else:
      movim.append(int(posicao))
      updt_board(int(posicao), 'O')

def maquina(): #escolha do computador (aleatório)
  import random
  posicao = random.randint(1,9)
  if posicao in movim:
    maquina()
  else:
    movim.append(posicao)
    updt_board(posicao, 'X')

def updt_board(posicao, marc): #Marcação no tabuleiro
  if posicao == 1:
    board[0][0] = marc
  elif posicao == 2:
    board[0][1] = marc
  elif posicao == 3:
    board[0][2] = marc
  elif posicao == 4:
    board[1][0] = marc
  elif posicao == 5:
    board[1][1] = marc
  elif posicao == 6:
    board[1][2] = marc
  elif posicao == 7:
    board[2][0] = marc
  elif posicao == 8:
    board[2][1] = marc
  elif posicao == 9:
    board[2][2] = marc

def who_won(marc): #Verifica quem ganhou
  global maq_point, usuario
  if marc == 'X':
    print('Você perdeu! ha ha ha')
    maq_point += 1
    print(f'O placar atual é: Usuário {usuario} : {maq_point} Computador. Atualmente teve {draw} empates ')
    reset()
  elif marc == 'O':
    print('Você ganhou! Parabéns!')
    usuario += 1
    print(f'O placar atual é: Usuário {usuario} : {maq_point} Computador. Atualmente teve {draw} empates ')
    reset()

def reset (): #Reset do tabuleiro
  global movim
  del movim
  movim = []
  global board
  del board
  board = []
  for i in range(3): #Geração de um novo tabuleiro
    linha = [empyt for i in range(3)]
    board.append(linha)

def check_win(marc): #Verificação de vitória
  global draw
  if board[0] == [marc, marc, marc] or board[1] == [marc, marc, marc] or board[2] == [marc, marc, marc]: #Linhas
    print('Jogo finalizado!')
    who_won(marc)
  elif board[0][0] == marc and board[1][1] == marc and board[2][2] == marc: #Diagonal 1
    print('Jogo finalizado!')
    who_won(marc)
  elif board[0][2] == marc and board[1][1] == marc and board[2][0] == marc: #Diagonal 2
    print('Jogo finalizado!')
    who_won(marc)
  for i in range(3): #Colunas
    if board[0][i] == marc and board[1][i] == marc and board[2][i] == marc:
      print('Jogo finalizado!')
      who_won(marc)
  if len(movim) == 9: #Condição de empate
    print('Deu velha!!!')
    draw += 1
    print(f'''O placar atual é: Usuário {usuario}:{maq_point} Computador. Atualmente teve {draw} empates''')
    reset()
#Programa principal:
print('''Vamos jogar um jogo?''')
reset()
board[1][1] = 'X'
movim.append(5)
bg_format()
while True: #Jogo
  posicao() #Jogada do usuário
  check_win('O') #Verifica se o usuário ganhou
  bg_format() #Mostra o tabuleiro
  maquina() #Jogada do computador
  bg_format()
  print(movim)
  check_win('X') #Verifica se o computador ganhou