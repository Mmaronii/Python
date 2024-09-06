print("\033[94mOlá, Seja bem-vindo ao nosso site\033[0m")

input("Pressione o enter para entrar: ")
print(" FILMES:")
print(" 1-Os Três Mosqueteiros: Milady\n\n 2-A Maldição do Queen Mary\n\n 3-Wonka\n\n 4-Aquaman 2: O Reino Perdido\n\n 5-Minha Irmã E Eu\n\n")
filmes = {1: "Os Três Mosqueteiros: Milady",
          2: "A Maldição do Queen Mary", 
          3: "Wonka", 4:"Aquaman 2: O Reino Perdido",
          5:"Minha Irmã E Eu"
          }

ing_escolhido = input("Informe o número do filme escolhido (1 a 5): ")

# Convertendo para inteiro
ing_escolhido = int(ing_escolhido)

print("\nCerto, agora informe a quantidade de ingressos:")
print("\n1- Inteira R$ 44,27\n")
print("2- Promoção Todos Pagam Meia R$ 22,13\n")

qntd = int(input("Digite a quantidade de ingressos desejada: "))
tipo_ingresso = input("Escolha o tipo de ingresso (inteira ou meia): ").lower()

preco_inteira = 44.27
preco_meia = 22.13

if ing_escolhido in filmes:
    nome_do_filme = filmes[ing_escolhido]

    if tipo_ingresso == "inteira":
        soma = qntd * preco_inteira
    elif tipo_ingresso == "meia":
        soma = qntd * preco_meia
    else:
        print("Tipo de ingresso inválido. Escolha 'inteira' ou 'meia'.")
        soma = 0

    print(f"O valor dos ingressos para {nome_do_filme} ({tipo_ingresso}) é: R$ {soma:.2f} reais")
else:
    print("Opção de ingresso inválida.")