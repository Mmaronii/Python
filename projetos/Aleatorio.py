import time

input("Olá, Seja Bem-vindo ao Detran. Para saber se foi multado, aperte 'Enter'")
print("Para saber se foi multado, insira algumas informações básicas a baixo:")
time.sleep(2)
print("Aguarde um tempo")
time.sleep(5.5)
lugar = input("Qual foi o local?:")
time.sleep(1.5)
hora = str(input("Qual foi o hórario?:"))
time.sleep(1.5)
dia = str(input("Qual foi o dia?:"))
time.sleep(1.5)
velocidade = int(input("Qual era a sua Velocidade?:"))
time.sleep(1.5)
placa = str(input("Qual é o carro e placa?:"))

vel_maxima = (80)

if velocidade <= vel_maxima:
    print(f"Você não foi multado. No dia {dia} as {hora} o carro identificado como {placa} estava a {velocidade} e a velocidade maxíma era 89km")
else:
    print(f"Infelizmente você foi multado, a velocida maxíma era de 89 e o carro {placa} estava a {velocidade}")

