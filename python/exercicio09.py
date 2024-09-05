tipo = input("Qual o combustivel?\n----(G) GASOLINA ----OU---- (E) ETANOL----\n")

if tipo=="G" or tipo=="GASOLINA" or tipo=="g":
    tipo = "GASOLINA"
    valor_combustivel= 5.80
    litros = float(input(f"Quantos litros de {tipo} ?\n"))

    valor_total = litros*valor_combustivel
    print("-----------------------------------------------")
    print(f"CLIENTE PAGA UM TOTAL DE : R${valor_total:,.2f}")
    print("-----------------------------------------------")
elif tipo=="E" or tipo=="ETANOL" or tipo=="e":
    tipo = "ETANOL"
    valor_combustivel = 4.90
    litros = float(input(f"Quantos litros de {tipo} ?\n"))

    valor_total = litros * valor_combustivel
    print("-----------------------------------------------")
    print(f"CLIENTE PAGA UM TOTAL DE : R${valor_total:,.2f}")
    print("-----------------------------------------------")
else :
    print("CODIGO DO COMBUSTIVEL INVALIDO")
