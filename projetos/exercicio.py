peso = float(input("Quanto você pesa?"))
altura = float(input("Quanto você tem de altura?"))
imc = peso/(altura * altura)

if (imc >= 18.5 and imc <= 24.9):
    print(f"Seu IMC está normal: {imc:.2f}")
elif(imc >= 25.0 and imc <= 29.9):
    print(f"Seu IMC está com sobrepeso: {imc:.2f}")
elif(imc >= 30.0):
    print(f"Seu IMC esta dando obesidade!!!!: {imc:.2f}")