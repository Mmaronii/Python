from random import randint
print("JOGO DO PÊNALTI")
input("Pressione o enter para entrar: ")
print("__________________")
print("|1              4|")
print("|        3       |")
print("|2              5|\n")
chute =int(input("Escolha um número (de 1 a 5) para chutar:"))
numero = randint(1, 5)
if chute == numero:
  print("Você errou! O goleiro pegou")
else:
  print("Párabens,você acertou o pênalti")
