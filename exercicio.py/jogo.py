# lista de enigmas e respostas
enigmas = [
{"pergunta": 'O que é, o que é? Anda com os pés na cabeça.', "resposta": "Piolho"}
{"pergunta": 'O que é, o que é? Fica no início da rua, no fim do mar e no meio da cara.', "resposta": "A letra r"}
{"pergunta": 'o que é, o que é? Você me tem hoje e amanhã me terá ainda mais. Conforme o tempo passa, eu não sou nada fácil de guardar. Não ocupo nenhum espaço, mas estou sempre em um único lugar. Eu sou o que você viu, não o que  você vê.', "resposta": "memória"}
]

print("Bem-vindo ao jogo 'O que é, o que é?' ! ")
print("Responda os enigmas corretamente para vencer o jogo.\n")

# inicializa o contador de pontos
pontos = 0

# loop pelos enigmas
for enigma in enigmas:
    print(enigma["pergunta"]) # mostra o enigma
    resposta = input("sua resposta:").strip().lower() # recebe a respostado jogador
    
    if resposta == enigma["resposta"]: # verifica se a resposta está correta
        print("correto!\n")
        pontos += 1
    else:
        print(f"errado! A resposta certa é:{enigma['resposta']}\n")

        # Exibe o resultado final
        print(f"você acertou {pontos} de {len(enigmas)}enigmas!")
        if pontos == len(enigmas):
            print("parabéns! você acertou todos os enigmas!")
        else:
            print("tente novamente para melhorar sua pontuação!")