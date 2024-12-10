import random

poderes = ['pedra','papel','tesoura']
computador = random.choice(poderes)
jogo_on = True
print(computador)
while jogo_on:
    jogador = str(input('JOKEPO -> pedra,papel ou tesoura:'))
    if jogador not in poderes:
        raise Exception('PODER INCORRETO: pedra,papel ou tesoura')
    if jogador == computador:
        print('empate')
    elif jogador == 'pedra':
        if computador != 'papel':
            print('JOGADOR GANHOU')
        else:
            print('PC GANHOU')
        jogo_on=False
    elif jogador == 'papel':
        if computador!='tesoura':
            print('JOGADOR GANHOU')
        else:
            print('PC GANHOU')
        jogo_on=False
    elif jogador == 'tesoura':
        if computador!= 'pedra':
            print('JOGADOR GANHOU')
        else:
            print('PC GANHOU')
        jogo_on=False
