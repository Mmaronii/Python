import random

def jogar_cara_ou_coroa():
    print("Bem-vindo ao jogo de Cara ou Coroa!")
    
    while True:
        escolha = input("Escolha 'cara' ou 'coroa': ").lower()
        
        if escolha not in ['cara', 'coroa']:
            print("Escolha inválida! Tente novamente.")
            continue
        
        resultado = random.choice(['cara', 'coroa'])
        print(f"O resultado foi: {resultado}")
        
        if escolha == resultado:
            print("Parabéns! Você ganhou!")
        else:
            print("Que pena! Você perdeu!")
        
        jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar! Até a próxima!")
            break

# Executa o jogo
jogar_cara_ou_coroa()
