array = [0]*5
tam = len(array)
for n in range(tam):
    array[n] = int(input("Digite um numero: "))
for i in range(tam,0,-1):
    print(array[i-1])