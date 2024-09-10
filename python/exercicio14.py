num = int(input("Digite um numero : "))
#para CONTADOR no range até meu numero recebido
for contador in range(1,num+1):
# se o resto da divisão do contador por 2
# for diferente de 0 ele printa o numero
    if contador%2!=0 :
        print(f"{contador}")