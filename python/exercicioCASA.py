escolha = 9999
while escolha != -0:
    num1 = float(input("Digite o primeiro número: \n"))
    num2 = float(input("Digite o segundo número: \n"))
    print("\nSelecione a operação:\n1. para soma\n2. para subtração\n3. multiplicação\n4. divisão\n"
          "5. para digitar novos números\n6. para sair")
    escolha = input("Escolha uma operação (1/2/3/4/5/6): ")
    match escolha:
        case "1":   print("Resultado da soma:", num1 + num2)
        case "2":   print("Resultado da subtração:", num1 - num2)
        case "3":   print("Resultado da multiplicação:", num1 * num2)
        case "4":
            if num2 != 0:   print("Resultado da divisão:", num1 / num2)
            else:   print("Não é possível dividir por zero.")
        case "5":   print("Digite novos números e rode o programa novamente.")
        case "6":
            print("Saindo...")
            escolha = -0
        case _: print("Opção inválida.")