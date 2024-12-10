import random 

poderes = ['pedra', 'papel', 'tesoura']

jogo_on = True 

while jogo_on:
    
    computador = random.choice(poderes)
    jogador = str(input('JOKENPO -> pedra, papel ou tesoura: '))
    if jogador not in poderes:
        raise Exception('PODER INCORRETO: escolha entre pedra, papel ou tesoura')
    if jogador == computador:
        print('Empate!')
    elif jogador == 'pedra':
        if computador != 'papel':
            print('JOGADOR GANHOU!')
        else:
            print('PC GANHOU!')
    elif jogador == 'papel':
        if computador != 'tesoura':
            print('JOGADOR GANHOU!')
        else:
            print('PC GANHOU!')
    elif jogador == 'tesoura':
        if computador != 'pedra':
            print('JOGADOR GANHOU!')
        else:
            print('PC GANHOU!') 
    continuar = input("Quer jogar novamente? (s/n): ")
    
    if continuar.lower() != 's':
            print("Fim do jogo! obrigado por jogar.")
    