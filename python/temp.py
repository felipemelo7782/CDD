# a = int(input("insira um numero "))
# b = int(input("insira um numero "))
# c = int(input("insira um numero "))
# print(f"A soma : {a+b}")
# if (a+b)<c :    print(f"o valor de C: {c} é maior que a soma dos numeros {a} e {b}")
# elif (a+b)==c:   print(f"o numero {c} é igual a soma ")
# else:   print(f"o numero {c} é menor que a soma dos numeros {a} e {b}")
#---------------------------------
# a = int(input("digite um numero "))
# texto=""
# if a>0 : texto = "é positivo,"
# else:texto = "é negativo,"
# if a % 2 == 0:  texto = f"{texto} é par"
# else:   texto = f"{texto} é impar"
# print(texto)
#----------------------------------
# opcao=1
# while opcao==1:
#     a = int(input("digite um numero "))
#     texto=""
#     if a>0 : texto = "é positivo,"
#     else:texto = "é negativo,"
#     if a % 2 == 0:  texto = f"{texto} é par"
#     else:   texto = f"{texto} é par"
#     print(texto)
#     opcao = int(input("\nDESEJA CONTINUAR?\n1 para Continuar\n2 para parar"))
#------------------------------------
# a = int(input("Digite um numero inteiro "))
# b = int(input("Digite um numero inteiro "))
# if a==b:    c=a+b
# else:   c=a*b
# print(f"O RESULTADO É: {c}")
#-------------------------------------
# a = int(input("Digite um numero: "))
# print(f"----- Antecessor : {a-1} Sucessor : {a+1} -----")
#-------------------------------------
# salario = float(input("Digite o valor do salário minimo: \n"))
# salarioDoUsuario = float(input("Digite o valor do salário do usuario: \n"))
#
# calc = salarioDoUsuario/salario
#
# print(f"o usuario ganha: {calc:.2f}X salarios minimos")
#--------------------------------------
# peso = float(input("Digite o seu peso: "))
# altura = float(input("Digite sua altura"))
# imc = peso/altura**2
#
# if imc<18.6:
#     print("Abaixo do peso🟢")
# elif imc>=18.6 and imc<=24.9:
#     print("Peso Ideal (PARABENS👌)")
# elif imc>=25.0 and imc<=29.9:
#     print(f"Levemente acima do peso")
# elif imc>=30.0 and imc<=34.9:
#     print("Obesidade grau I 🟡")
# elif imc>=35.0 and imc<=39.9:
#     print("Obesidade grau II (Severa🟠)")
# elif imc>=40:
#     print("Obesidade grau III (Mórbida🔴)")
# else:
#     print("ERRO NO PROGAMA")
# print(f"SEU INDICE DE MASSA CORPORAL É: {imc:.1f}")
#-----------------------------------------
# print("\nINPARES 1 ATÉ 500")
# for i in range(0,501):
#     if i%2!=0: print(i,end=" ")
#------------------------------------------
# print("\nPARES 100 ATÉ 1")
# for i in range(101,0,-1):
#     if i%2==0: print(i,end=" ")
#-------------------------------------------
# print("\nINPARES 1 ATÉ 500")
# i = 1
# while i<=500:
#     if i % 2 != 0: print(i, end=" ")
#     i+=1
#--------------------------------------------
# print("\nPARES 100 ATÉ 1")
# i = 100
# while i >=1:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i-=1
#---------------------------------------------
