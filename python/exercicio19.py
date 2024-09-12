num1 = float(input("Digite um numero: "))
num2 = float(input("Digite um numero: "))

while num2 == 0:
    print("----------------------------")
    print("Digite um numero maior que zero")
    num2 = float(input("Digite um numero: "))

while num1 == 0:
    print("----------------------------")
    print("Digite um numero maior que zero")
    num1 = float(input("Digite um numero: "))

    divisao = num1 / num2
    print("\n----------RESULTADO-----------")
    print(f"------{num1} ÷ {num2} = {divisao}-----")
    print("----------------------------")