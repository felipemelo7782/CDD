nome = input("Insira seu nome: ")

idade = int(input("Insira sua idade: "))

salario = float(input("Insira seu salário: "))

salario_novo = salario*1.1
idade_meses = idade*12
print("------------------------------")
print(f"Nome: {nome}\nIdade : {idade}\nIdade em Meses : {idade_meses}\nSalário : {salario:,.2f}\nSalário+10%: {salario_novo:,.2f}")
print("------------------------------")