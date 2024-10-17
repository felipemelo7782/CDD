
# fazer menu 1ler 2gravar 3pesquisar 4sair
with open("nome.txt","a") as arquivo:
    nome = input("Digite um nome: ")
    arquivo.write(f"{nome}\n")

with open("nome.txt", "r")as arq2:
    print(arq2.read())


def ler():
