opcao=1
while opcao==1:
    num = int(input("MOSTRAREI A TABUADA DO SEU NUMERO \nDigite um numero: "))
    n=1
    while n<=10:
        multi = n * num
        print(f"{num} X {n} ={multi}")
        n+=1
    opcao= int(input("\n\nDESEJA CONTINUAR?\n-------(1) PARA CONTINUAR----------\n-------(0) PARA FINALIZAR----------\n"))