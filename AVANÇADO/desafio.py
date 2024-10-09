usuarios = [""] * 5
senhas = [""] * 5
tam = len(senhas)
nomeUsuario = ""
senhaUsuario = ""
posi = 0
resposta = 1

while resposta != 3:
    resposta = int(input("===Menu=== \n1. Cadastrar \n2. Login \n3. Sair \n\nResposta: "))

    match resposta:
        case 1 :
            for i in range(tam):
                usuarios[i] = input("⤜ Cadastre o usuário: ")
                senhas[i] = input("⤜ Cadastre a senha: ")
        case 2 :
            for k in range(3, -1, -1):
                nomeUsuario = input("\n⤜ Digite seu usuário: ")
                if nomeUsuario in usuarios:
                    for j in range(tam):
                        if nomeUsuario == usuarios[j]:
                            posi = j
                            for l in range(3, -1, -1):
                                senhaUsuario = input(f"\nOlá {nomeUsuario} ㋡! \n⤜ Digite sua senha: ")
                                if senhaUsuario == senhas[posi]:
                                    print("\n✰ Login efetuado com sucesso ✰")
                                    break
                                else:
                                    print(f"\n«Senha inválida!» \n⥼ Restam {l - 1} tentativas ⥽")
                                if l == 0:
                                    print("\n⊗ Tentativas esgotadas! ⊗")
                                    break
                    break
                else:
                    print(f"\n«Usuário não existe!» \nRestam {k - 1} tentativas!")
                if k == 1:
                    print("\n--- Tentativas esgotadas! --- \n---Voltando ao menu ↺---")
                    break
        case _:
            print("\nQUASE USEI O VSCODE\n")