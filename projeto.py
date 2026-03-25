print("Bem vindo a sua agenda de tarefas")

acao = input("Deseja adicionar atividades de hoje? digite adicionar \n"
             "Deseja ver o total de atividades? presione enter \n")

if acao == "adicionar":
    atividades = input("Quais são suas atividade?\n")
    listaatv = atividades.split(",")
    quantidade = len(listaatv)
    visualizar = input("Deseja visualizar suas atividades? digite sim \n")
    if visualizar == "sim":
        print(f"Voce tem", quantidade,"atividades, sendo elas:", listaatv)
    else:
        print("Suas atividades foram cadastradas com sucesso!")
else:
    print("Voce nao tem atividades cadastradas.")
