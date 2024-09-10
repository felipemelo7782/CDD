soma = 0
for cont in range(10):
    num = int(input("Digite um numero : "))
    if num%2 !=0:
        soma= soma+num
print(f"SOMA TOTAL : {soma}")