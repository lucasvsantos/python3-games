print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = input("Digite um número: ")
print("Você digitou o numero:", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou! xD")
else:
    print("Você errou! =(")

print("Fim do jogo!")