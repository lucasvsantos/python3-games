print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número: ")
    print("Você digitou o numero:", chute_str)

    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou! xD")
    else:
        if(maior):
            print("Você errou! O seu número é maior do que o número secreto. =(")
        elif(menor):
            print("Você errou! O seu número é menor do que o número secreto. =(")

    rodada = rodada + 1

print("Fim do jogo!")