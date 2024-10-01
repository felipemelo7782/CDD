array = ['']*5
tam=len(array)
for i in range(tam):
    array[i] = input('Digite o nome do aluno: ')
for x in range(5):
    print(f" {x} {array[x]} ")
    