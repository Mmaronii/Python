
from palavraforca import palavra #importei de outro codigo
letras_usuarios = [] #total de letras
chances = 7 #total de chances
ganhou = False # pra no final fazer o if

print("!DICA: É uma fruta!")

while True: #base # obs:".lower é pra deixar tudo no minusculo"
   #criar a nossa logica
   
   for letra in palavra:
       if letra.lower() in letras_usuarios:
           print(letra, end=" ") # se o usuario acertar a letra ira colocar a letra no seu deevido local
       else:
           print("_", end=" ") # se ele errar ira colocar apenas um _
           
   print(f"Você tem {chances} chances")
   tentativa = input("Escolha uma letra para adivinhar:") #informar a letra
   letras_usuarios.append(tentativa.lower())  # colocando a letra informada a cima dentro dos espaço vazio da forca
   if  tentativa.lower() not in palavra.lower(): # se  o usuario errar ira remover uma  das 7 chances
       chances -= 1
       
   ganhou = True
   for letra in palavra:
        if letra.lower() not in letras_usuarios:
             ganhou = False # isso tudo seria a logica pra verificar se ele ganhou
    
       
   if chances == 0 or ganhou:
       break # se ele perder ou ganha ira parar o  jogo
           
if ganhou:
        print(f"Parabéns, você ganhou. A palavra era : {palavra}")
else:
        print(f"Você perdeu. A palavra era : {palavra}")   #mensagem final