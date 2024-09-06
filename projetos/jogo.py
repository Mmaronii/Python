def show_intro():
    print("Bem-vindo à Vila das Variáveis!")
    print("Aqui você aprenderá sobre variáveis e tipos de dados.")
    print("Vamos começar com um tutorial simples.")
    print()

def tutorial():
    print("Tutorial:")
    print("Em Python, você pode armazenar valores em variáveis. Por exemplo:")
    print("x = 5")
    print("nome = 'João'")
    print("Para ver o valor armazenado em uma variável, basta digitá-la:")
    print("print(x)")
    print("print(nome)")
    print()

def challenge():
    print("Desafio: Ajudar os habitantes da vila a organizar seus pertences.")
    print("Você precisa criar variáveis para armazenar os itens.")
    print("Depois, mostre o que você armazenou.")
    print()
    
    # Solicitar ao jogador que crie variáveis
    mochila = input("Digite o nome de um item para colocar na mochila: ")
    quantidade = int(input("Digite a quantidade desse item: "))
    
    # Mostrar os itens armazenados
    print()
    print("Você colocou na mochila:")
    print(f"Item: {mochila}")
    print(f"Quantidade: {quantidade}")
    print()

def main():
    show_intro()
    tutorial()
    
    continuar = input("Você está pronto para o desafio? (sim/não): ")
    if continuar.lower() == 'sim':
        challenge()
    else:
        print("Tudo bem! Volte quando estiver pronto.")
        print()

if __name__ == "__main__":
    main()
