from time import sleep
import rule
print('''Vamos jogar um jogo?
Caso queira sair, basta digitar "sair" ou "exit" ''')
sleep(2)
rule.board[1][1] = 'X'
rule.bg_format(rule.board)
while True: #jogo
    if rule.player_move(rule.board) == 'fim': #vez do jogador e condição de saída
        break
    if rule.check_win('O'): #verifica se o jogador ganhou
        rule.score('O') #marca a pontuação
    rule.pc_move(rule.board)
    if rule.check_win('X'): #verifica se a máquina ganhou
        rule.score('X') #marca a pontuação