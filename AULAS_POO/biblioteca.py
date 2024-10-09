
class Pessoa:

    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.andando=False
        self.dormindo=False
        self.comendo=False

    def dormir(self):
        if (not self.andando and not self.comendo and not self.dormindo):
            self.dormindo = True
            print(f" {self.nome} Foi Dormir")
        elif (self.andando):
            print(f" {self.nome} Foi andar ñ pode Dormir")
        elif (self.comendo):
            print(f" {self.nome}  Está Comendo ñ pode dormir")
        elif (self.dormindo):
            print(f" {self.nome}  Já Está Dormindo")

    def andar(self):
        if (not self.andando and not self.comendo and not self.dormindo):
            self.andando = True
            print(f" {self.nome} Foi andar de cavalo")
        elif (self.andando):
            print(f" {self.nome} Já Foi andar de cavalo")
        elif(self.comendo):
            print(f" {self.nome} Está Comendo ñ pode andar")
        elif(self.dormindo):
            print(f" {self.nome} Está Dormindo ñ pode andar")

    def comer(self):
        if (not self.andando and not self.comendo and not self.dormindo):
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
        if (self.andando):
            self.dormindo=False
            print(f" {self.nome} Parou de Dormir")
        else:
            print(f" {self.nome} Não está Dormindo")