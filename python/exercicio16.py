num = int(input("Digite o numero de alunos : "))

somaNotas=0
for aluno in range(1,num+1):
    nota = float(input(f"Digite a nota do aluno {aluno}: "))
    somaNotas= somaNotas+nota
media=somaNotas/num
print(f"MEDIA ARITMETICA DA TURMA: {media}")