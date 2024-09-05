numero1 = int(input("Insira um numero: "))
numero2 = int(input("Insira outro numero: "))

if (numero1 == numero2) :
    print(f"numeros iguais")
else :
    if (numero2 > numero1) :
        print(f"{numero1}, {numero2}")
    else :
        print(f"{numero2},{numero1}")