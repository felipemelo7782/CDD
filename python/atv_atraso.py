opcao =1
while opcao==1:
    av1 = float(input("-----------------------------\n"
                      "Qual a nota da 1ª Avaliação? \n"))

    while av1>10 or av1<0 or av1=='' or av1==-0 :
        print("---- DIGITE UMA NOTA ENTEE ZERO E DEZ ----")
        av1 = float(input("Qual a nota da 1ª Avaliação \n"))

    av2 = float(input("-----------------------------\n"
                      "Qual a nota da 2ª Avaliação \n"))

    while av2>10 or av2<0 or av2=='' or av2==-0 :
        print("---- DIGITE UMA NOTA ENTEE ZERO E DEZ ----")
        av2 = float(input("-----------------------------\n"
                      "Qual a nota da 2ª Avaliação \n"))

    media =(av1+av2)/2

    print(f"Media do aluno é : {media:,.2f}\n--------------\n------------\n")
    opcao = int(input("Deseja Fazer outro calculo? \n"
                      "(1) PARA CONTINUAR E (2) PARA FINALIZAR\n"))
