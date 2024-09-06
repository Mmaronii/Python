nome = input("Informe seu nome:")
nasc = input("Informe seu nascimento:")
film = input("Informe seu filme favorito:")

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

mycursor = mydb.cursor()

sql ="INSERT INTO autores(Nome,DataDeNascimento,Filme) VALUES(%S,%S,%S)"
reslt =(nome,nasc,film)
mycursor.execute(sql,reslt)

mydb.commit()

print(mycursor.rowcount, "Está inserido")