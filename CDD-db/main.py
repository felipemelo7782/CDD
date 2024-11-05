import mysql.connector

banco = mysql.connector.connect (
    host="localhost",
    user="root",
    password="123456",
    database="turma_c"
)
#print(banco)

meucursor = banco.cursor()

pesquisa = 'select * from alunos;'

meucursor.execute(pesquisa)

# fetchall recebe tudo da pesquisa e retorna atraves de uma tupla

resultado = meucursor.fetchall()
for x in resultado:
    print(x)

nome="Felipe Melo"
telefone="993374199"

sql = "insert into alunos (nome, telefone) values (%s,%s)"
data = (nome,telefone)

meucursor.execute(sql,data)
banco.commit()
print(" ")
meucursor.execute(pesquisa)

# fetchall recebe tudo da pesquisa e retorna atraves de uma tupla

resultado = meucursor.fetchall()
for x in resultado:
    print(x)

meucursor.close()
banco.close()