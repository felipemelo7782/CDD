#faça um prgma para calcular a media de 2 notas
# e mostrar essa media e o nome do aluno
nome = input("coloque o nome do aluno")
#.replace(,) é para trocar um caracter por outro
nota1 = float(input("Insira uma nota").replace(',','.'))
nota2 = float(input("Insira uma nota").replace(',','.'))

media = (nota1+nota2)/2

print(f"Olá {nome} sua média é : {media}")
