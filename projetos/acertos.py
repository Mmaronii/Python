from random import randint

seu_nome = input('\033[94m' "Olá, você topa um desafio? Qual é o seu nome?" + '\033[0m')

print('\033[94m' + f"Ok {seu_nome}, estou escolhendo um número de 1 até 20. Você consegue adivinhar com 5 tentativas?" + '\033[0m')

numero_adivinhado = randint(1, 20)

numero_tentativa = 5

for tentativa in range(1, numero_tentativa + 1):
    numero_escolhido = int(input('\033[94m' + "Escolha um número: " + '\033[0m'))
    if numero_escolhido == numero_adivinhado:
        print('\033[94m' + f"Parabéns, você acertou em {tentativa} tentativas!" + '\033[0m')
        break
    elif numero_escolhido > numero_adivinhado:
        print('\033[94m' + "Escolha um número menor!" + '\033[0m')
    else:
        print('\033[94m' + "Escolha um número maior!" + '\033[0m')

print('\033[94m' + f"O número era {numero_adivinhado}. Obrigado por jogar!" + '\033[0m')