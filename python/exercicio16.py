#RECEBE QUANTIDADE DE ALUNOS NA VARIAVEL alunos
alunos = int(input("Digite o numero de alunos : "))
#INICIA A VARIAVEL GLOBALMENTE
somaNotas=0
#INICIA O FOR COM A QUANTIDADE DE ALUNOS+1 (POIS ELE SO VAI ATE A QUANTIDADE)E INICIA COM 1
for aluno in range(1, alunos + 1):
    #RECEBE A NOTA DO ALUNO ATUAL EM FLOAT
    nota = float(input(f"Digite a nota do aluno {aluno}: "))
    #SOMA O TOTAL DAS NOTAS
    somaNotas= somaNotas+nota

media= somaNotas / alunos
print(f"MEDIA ARITMETICA DA TURMA: {media}")