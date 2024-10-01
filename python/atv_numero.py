num = int(input("Digite um numero: "))

for i in range(1,num+1):
    for j in range(i):
        print(f" {j}", end="")
    print("")