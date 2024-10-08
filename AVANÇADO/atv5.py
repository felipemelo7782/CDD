usuarios = [""] * 5
senhas = [""] * 5
tam = len(usuarios)
for i in range(tam):
    usuarios[i] = input("Digite o seu usuario: ")
    senhas[i] = input("Digite sua senha: ")

for j in range(tam):
    print(f"O usuário {usuarios[j]} tem a senha {senhas[j]} na posição {j + 1}°")