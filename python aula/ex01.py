def readnotes1(): #esta chamando a primeira variavel
    n1 = float(input("What is the first note of the student?:")) #variavel
    return n1 #pedindo pra retornar a variavel

def readnotes2(): #mesma coisa que o de cima 
    n2 = float(input('What is the second note of the student?:'))
    return n2

def result(n1,n2): #aq esta pegando as duas variaveis e meio que juntando pra ficar mais facil de buscar
    average=(n1+n2)/2 #fazendo  a conta do dois numeros 
    print('Note 1:', n1)#exibindo aprimeira nota
    print('Note 2:', n2)#exibindo a segunda nota
    print('Average: ', average, "Result: " , end='')#resultados finais 
    if average >= 7: # si a 'media' for maior que 7vai  printar que ele passou else(si nao) que ele eprovou
        print('congratulation, You passed')  
    else:
        print("I'm sorry, You no passed:(") 
        
a = readnotes1()
b = readnotes2()
result(a,b) 
