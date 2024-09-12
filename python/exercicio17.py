
x=1
somaNotas=0

while x <= 10:
    nota = float(input(f"Digite a nota do aluno {x}: "))
    somaNotas= somaNotas+nota
    x+=1
media= somaNotas / 10
print(f"MEDIA ARITMETICA DA TURMA: {media}")