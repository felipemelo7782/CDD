num = int(input("Digite um numero: "))

for i in range(1,num+1):
    print(f"{i}", end=" ")
    for j in range(i):
        print(f"{i}", end=" ")