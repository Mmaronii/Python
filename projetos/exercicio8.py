import time
print("Responda as perguntas com a,b,c,d.")
 
time.sleep(2)
 
print("\033[93mDe onde é a invenção do chuveiro elétrico?\033[0m")

time.sleep(2)

print(" a) França\n b) Inglaterra\n c) Brasil\n d) Austrália")
res_1 = input(" Resposta:")

time.sleep(2)

print("\033[93mQuais o menor e o maior país do mundo?\033[0m")

time.sleep(2)

print(" a) Vaticano e Rússia\n b) Nauru e China\n c) Mônaco e Canadá\n d) Malta e Estados Unidos")
res_2 = input(" Resposta:")

time.sleep(2)

print("\033[93mO que a palavra \033[38;2;218;165;32mLEGEND\033[0m \033[93msignifica em português?\033[0m")

time.sleep(2)

print(" a) Legenda\n b) Conto\n c) História\n d) Lenda")
res_3 = input(" Resposta:")

time.sleep(2)

print("\033[93mQual o número mínimo de jogadores em cada time numa partida de futebol?\033[0m")
print(" a) 7\n b) 10\n c) 9\n d) 8")
res_4 = input(" Resposta:")

time.sleep(2)

print("\033[93mQual a altura da rede de vôlei nos jogos masculino e feminino?\033[0m")
print(" a) 2,5 m e 2,0 m\n b) 1,8 m e 1,5 m\n c) 2,45 m e 2,15 m\n d) 2,43 m e 2,24 m")
res_5 = input(" Resposta:")

print("RESULTADO:\n")

time.sleep(3)
if res_1 == "c":
  print("\033[92mCorreto\033[0m")
else:
  print("\033[91mErrado\033[0m")
  
if res_2 == "a":
  print("\033[92mCorreto\033[0m")
else:
  print("\033[91mErrado\033[0m")

if res_3 == "d":
  print("\033[92mCorreto\033[0m")
else:
   print("\033[91mErrado\033[0m")
   
if res_4 == "a":
  print("\033[92mCorreto\033[0m")
else:
   print("\033[91mErrado\033[0m")
   
if res_5 == "c":
  print("\033[92mCorreto\033[0m")
else:
   print("\033[91mErrado\033[0m")