lista = []
tipo_jogos = []

#MENU INICIO
while True:

    print("\nBem Vindo a sua bliblioteca de jogos!!!\n")
    print("Abaixo estão listadas algumas funções. Comece adicionando alguns jogos a sua bliblioteca basta digitar 1\n")

    print("[1] Inserir game")
    print("[2] Consultar games")
    print("[3] Alterar game")
    print("[4] Excluir game")
    print("[5] Salvar bliblioteca (Só utilizar quand já tiver adicionado jogos a sua bliblioteca.)")
    print("[6] Importar bliblioteca (Só utilize essa opção se já tiver salvo sua bliblioteca.)")
    print("[7] Sair\n")


    resposta = int(input("Digite a opção desejada : "))
#MENU FIM

#INSERT
    if resposta == 1:
        insira = str(input("\nO insira um game ?\n"))
        lista.append(insira)
        insira_2 = str(input("\nQual o tipo do game ?\n"))
        tipo_jogos.append(insira_2)
        print("\nGame inserido com sucesso!!!\n")
        print('\nJogo :',lista)
        print('Tipo :',tipo_jogos)

#Select
    elif resposta == 2:
        consultar = str(input("\nQual game quer buscar ?\n"))
        if consultar in lista:
            print("O jogo está na lista\n")
            j_pos = lista.index(consultar)
            print(lista[j_pos])
            print(tipo_jogos[j_pos],'\n')
        else:
            consultarn = consultar+'\n'
            if consultarn in lista:
                print("O jogo está na lista\n")
                j_pos = lista.index(consultarn)
                print(lista[j_pos])
                print(tipo_jogos[j_pos],'\n')
            else:
                print("\nO item não esta na lista. Gostaria de adicionar ?\n")
                print("[1] Sim")
                print("[2] Não\n")
                cond_consu = int(input("Selecione : "))
                if cond_consu == 1:
                    lista.append(consultar)
                    select_tipo= str(input("\nEscreva o tipo desse jogo : ")) 
                    tipo_jogos.append(select_tipo)
                    print("\nJogo adicionado\n")
                elif cond_consu == 2:
                    print("\nVoltando para o menu\n")


#Alterar
    elif resposta == 3:
        print(lista)
        antigo = str(input("\nEscreva um jogo da lista acima para fazer a substituição : \n"))
        if antigo in lista:
            g_pos = lista.index(antigo)
            novo = str(input("Digite o jogo que vai substituir o elemento que digitou anteriormente : "))
            lista[g_pos] = novo
            novo_tipo = str(input("Digite o novo tipo do seu jogo : "))
            tipo_jogos[g_pos] = novo_tipo
        else :
            antigon = antigo + '\n'
            g_pos = lista.index(antigon)
            novo = str(input("Digite o jogo que vai substituir o elemento que digitou anteriormente : "))
            lista[g_pos] = novo
            novo_tipo = str(input("Digite o novo tipo do seu jogo : "))
            tipo_jogos[g_pos] = novo_tipo
        print(lista)
        print(tipo_jogos)


#Delete
    elif resposta == 4:
        print(lista,'\n')
        remover = str(input("Digite o game para ser removido (NÃO ESCREVA : '\-n') : \n"))
        if remover in lista:
            r_pos = lista.index(remover)
            lista.remove(remover)
            t_rem = tipo_jogos[r_pos]
            tipo_jogos.remove(t_rem)
            print("Itens removidos")
        else:
            removern = remover+'\n'
            r_pos = lista.index(removern)
            lista.remove(removern)
            t_rem = tipo_jogos[r_pos]
            tipo_jogos.remove(t_rem)
            print("Itens removidos")
            print(lista)

#Gravar arquivo
    elif resposta == 5:
        arquivo = open("texto_nome.txt","a")
        arquivo_tipo = open("texto_tipo.txt","a")
        arquivo.writelines(line + "\n" for line in lista)
        arquivo_tipo.writelines(line_t + "\n" for line_t in tipo_jogos)
        print("Bliblioteca salva!! (Ao fechar o programa para importar basta digitar a opção 6)")

#Importar arquivo
    elif resposta == 6:
        arquivo = open("texto_nome.txt","r")
        arquivo_tipo = open("texto_tipo.txt","r")
        lista = arquivo.readlines()
        tipo_jogos = arquivo_tipo.readlines()
        print("\n",lista)
        print(tipo_jogos)
        print("Bliblioteca importada!!")


#Exit
    elif resposta == 7:
        exit()

    else:
        print("Não existe essa opção, te retornando para o menu.")
