alunos = int(input("Digite o numero de alunos : "))

somaNotas = 0
x = 1

# ENQUANTO x for menor ou igual a o valor de ALUNOS
while x <= alunos:
    # nota recebe um input  CONVERTIDO PRA FLOAT da nota do aluno
    nota = float(input(f"Digite a nota do aluno {x}: "))

    # soma a nota recebida + o total de notas
    somaNotas = somaNotas + nota

    # adiciona +1 a variavel X
    x += 1

# calcula a media do total de alunos
media = somaNotas / alunos

# imprime a media
print(f"MEDIA ARITMETICA DA TURMA: {media}")