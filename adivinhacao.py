print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

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

print("Fim do jogo!")