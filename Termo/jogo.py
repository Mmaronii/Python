from palavratermo import palavras #impoprtando apalavra do outro codigo
import random

palavra_secreta = random.choice(palavras)

def avaliar_adivinhacao(palavra, tentativa): #aq vai ser aonde vai ver se as letra e a ordem esta correta
    resultado = ""
    for i in range (len(palavra)):
     if tentativa[i] == palavra[i]:
         resultado += "🟩" #letra correta na posicao correta
    
     elif tentativa[i] in palavra:
         resultado += "🟨"  #letra correta no lugar errado
         
     else:
         resultado += "⬜"  # Letra incorreta
    return resultado

#logica do jogo
def jogo_termo():
    tentativas_restantes  = 6
    input("Aperte ENTER para começar.")
    print("Bem vindo ao Termo!")
    print("Tente adivinhar a palavra de 5 letras.")
    
    while tentativas_restantes > 0:
        tentativa = input("Digite sua tentativa: ").lower()
        
        if len(tentativa) !=len(palavra_secreta):
            print(f"A palavra deve ter {len(palavra_secreta)} letras. Tente novamente")
            continue
        resultado = avaliar_adivinhacao(palavra_secreta, tentativa)
        print(resultado)
        
        if tentativa == palavra_secreta:
            print("Parabéns! Você acertou a palavra!")
            break #para parar de  jogar
        
        tentativas_restantes -=  1
        print(f"Tentativas restantes: {tentativas_restantes}")
    if tentativas_restantes  == 0:
     print(f"Você perdeu... A palavra era: { palavra_secreta}")
    
 #para comçar o jogo   
jogo_termo()
