from random import randint
print("JOGO DO PÊNALTI")
input("Pressione o enter para entrar: ")
print("__________________")
print("|                |")
print("|  1          2  |")
print("|                |\n")
chute =int(input("Escolha um número (de 1 a 2) para chutar:"))
numero = randint(1, 2)
if chute == numero:
  print("Você errou! O goleiro pegou")
else:
  print("Párabens,você acertou o pênalti")