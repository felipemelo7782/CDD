
class Pessoa:

    def __init__(self,nome,peso,idade,andando):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.andando=False
        self.dormindo=False
        self.comendo=False

    def dormir(self):
        if not self.andando and not self.comendo and not self.dormindo:
            self.dormindo = True
            print(f" {self.nome} Foi Dormir")
        elif (self.andando):
            print(f" {self.nome} Foi andar ñ pode Dormir")
        elif (self.comendo):
            print(f" {self.nome}  Está Comendo ñ pode dormir")
        elif (self.dormindo):
            print(f" {self.nome}  Já Está Dormindo")

    def andar(self):
        if not self.andando and not self.comendo and not self.dormindo:
            self.andando = True
            print(f" {self.nome} Foi andar de cavalo")
        elif (self.andando):
            print(f" {self.nome} Já Foi andar de cavalo")
        elif(self.comendo):
            print(f" {self.nome} Está Comendo ñ pode andar")
        elif(self.dormindo):
            print(f" {self.nome} Está Dormindo ñ pode andar")

    def comer(self):
        if not self.andando and not self.comendo and not self.dormindo:
            self.comendo = True
            print(f" {self.nome} Foi comer")
        elif (self.andando):
            print(f" {self.nome} Foi andar ñ pode comer")
        elif(self.comendo):
            print(f" {self.nome} Já Está Comendo ")
        elif(self.dormindo):
            print(f" {self.nome} Está Dormindo ñ pode andar")

    def pararDeComer(self):
        if (self.comendo):
            self.comendo=False
            print(f" {self.nome} Parou de comer")
        else:
            print(f" {self.nome} Não está comendo")

    def pararDeAndar(self):
        if (self.andando):
            self.andando=False
            print(f" {self.nome} Parou de andar")
        else:
            print(f" {self.nome} Não está Andando")

    def pararDeDormir(self):
        if (self.dormindo):
            self.dormindo=False
            print(f" {self.nome} Parou de Dormir")
        else:
            print(f" {self.nome} Não está Dormindo")

class Animal:
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O {self.nome} Foi comer...")

class Gato(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def miar (self):
        print(f"O {self.nome} Fez MIAAAAAAAAAU")

class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def comer(self,alimento):
        print(f"O cachorro de {self.nome} foi comer {alimento} ")

    def late(self):
        print(f"O {self.nome} Fez AU AU AU")

class Papagaio(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def Falar(self):
        print(f"O {self.nome} Fez arhh arhh")

class Galinha(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)

    def cacarejar(self):
        print(f"A {self.nome} Có Có Có Có ")

class Arquivo:
    def __init__(self,nomeArquivo):
        self.nome=nomeArquivo

    def pesquisar(texto):
        cont = 0
        with open(, "r") as pesq:
            for x in pesq:
                if texto in x:
                    cont += 1
            print(f"Achei {cont} ocorrencia de {texto} no arquivo")

    def gravar(t):
        with open("nome.txt", "a") as arquivo:
            arquivo.write(f"{t}\n")