def imprimir_funcao():
    calculo = 0
    while calculo !=6:
        f1=int(input("Escolha um número: "))
        f2=int(input("Escolha um número novamente: "))
        calculo = int(input("escreva o número da função:\n 1-soma\n 2-subtração\n 3-mult\n 4-divisão\n 5-Exponenciação\n 6-sair\n"))
        if calculo == 1:
          res= (f1 + f2)
          print(f"Soma:{res}")
        if calculo == 2:
          res = (f1 - f2)
          print(f"subtração:{res}")
        if calculo == 3:
            res = (f1 * f2)
            print(f"multiplicação:{res}")
        if calculo == 4:
            res = (f1 / f2)
            print(f"divisão:{res}")
        if calculo == 5:
            res = (f1 ** f2)
            print(f"Exponenciação:{res}" )
        elif calculo == 6:
            print("sair")

imprimir_funcao()