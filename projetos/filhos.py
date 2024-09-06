import time
print("Responda as perguntas com a,b,c,d.")
 
time.sleep(2)
 
print("\033[93mQuem é seu filho fav?\033[0m")

time.sleep(2)

print(" a) Enzo\n b) Miguel\n c) luisa\n d) Antonia")
res_1 = input(" Resposta:")

print("RESULTADO:\n")

time.sleep(3)
if res_1 == "b":
  print("\033[92mCorreto\033[0m")
else:
  print("\033[91mErrado\033[0m é o miguellll")