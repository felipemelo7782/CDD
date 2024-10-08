
def imprimeNome(nome):
    print(f"Olá, {nome}")

def piramide1(a):
    for i in range(1,a+1):
        for j in range(i):
            print(i,end=" ")
        print()

def piramide2(a):
    for i in range(1, a + 1):
        for j in range(1,i):
            print(f" {j}", end="")
        print("")

def conta_vogais(texto):
    tam = len(texto)
    vogais = 0
    for x in range(tam):
        if texto[x] in "aeiouAEIOU":
            vogais+=1
    #print(f"Foi encontradas {vogais} vogais")
    #para ser uma função tem que ter um RETURN
    return vogais

def soma(n1, n2, n3, n4, n5):
    soma = n1+n2+n3+n4+n5
    return soma

def soma1(n1, n2, n3, n4, n5):
    soma = n1+n2+n3+n4+n5
    print(f"valor total : {soma}")

def somaOsNumerosEImprima(*numeros):
    tam = len(numeros)
    soma =0
    for i in range(tam):
        soma += numeros[i]
    print(f"valor total : {soma}")

def someOsNumeros1(*numeros):
    tam = len(numeros)
    soma =0
    for i in range(tam):
        soma += numeros[i]
    return soma

def someOsNumeros2(*numeros):
    soma =0
    for i in numeros:
        soma += numeros[i]
    return soma

def someOsNumeros3(*numeros):
    soma =sum(numeros)
    return soma

def recebeTexto(texto):
    t = len(texto)
    letras = 0
    for i in range(t,0,-1):
        print(texto[i-1],end=" ")
        if texto[i-1]!=" ":
            letras+=1
    print(f"\nletras: {letras}")

def novaLista(lista):
    new_list=[]
    for i in l:
        if i in new_list:
            new_list.append(i)
    print(new_list)