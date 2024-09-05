nota1 = float(input("Insira a 1ª nota : "))
nota2 = float(input("Insira a 2ª nota : "))
nota3 = float(input("Insira a 3ª nota : "))

media = (nota1+nota2+nota3)/3

if media>=7.0:
    print("---------APROVADO-----------------")
    print(f"--------com media : {media:,.2f}---------")
    print("----------------------------------")
elif media>=4.0:
    print("----------RECUPERAÇÃO--------------")
    print(f"-------com media : {media:,.2f}----------")
    print("-----------------------------------")
else:
    print("---------REPROVADO----------------")
    print(f"-------com media : {media:,.2f}---------")
    print("----------------------------------")
