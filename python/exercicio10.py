num = int(input(f"Insira o Mês \n -----VALOR EM NUMEROS-----\n------ DE 1 A 12------\n"))

if num >12 or num<1:
    print(f"Mês Inválido")
elif num == 1:
    print("Janeiro")
elif num == 2:
    print("Fevereiro")
elif num == 3:
    print("Março")
elif num == 4:
    print("Abril")
elif num == 5:
    print("Maio")
elif num == 6:
    print("Junho")
elif num == 7:
    print("Julho")
elif num == 8:
    print("Agosto")
elif num == 9:
    print("Setembro")
elif num == 10:
    print("Outubro")
elif num == 11:
    print("Novembro")
elif num == 12:
    print("Dezembro")

# OUTRO METODO
# match num:
#
#     case 1:
#         print("Janeiro")
#     case 2:
#         print("Fevereiro")
#     case 3:
#         print("Março")
#     case 4:
#         print("Abril")
#     case 5:
#         print("Maio")
#     case 6:
#         print("Junho")
#     case 7:
#         print("Julho")
#     case 8:
#         print("Agosto")
#     case 9:
#         print("Setembro")
#     case 10:
#         print("Outubro")
#     case 11:
#         print("Novembro")
#     case 12:
#         print("Dezembro")
#     case _:
#         print(f"Mês Inválido")