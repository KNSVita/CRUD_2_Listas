NOME_ARQUIVO = "biblioteca_jogos.txt"

#MENU
def exibir_menu():
    print("\nBem-vindo à sua biblioteca de jogos!!!\n")
    print("Abaixo estão listadas algumas funções. Comece adicionando alguns jogos à sua biblioteca.")
    print("[1] Inserir jogo")
    print("[2] Consultar jogos")
    print("[3] Alterar jogo")
    print("[4] Excluir jogo")
    print("[5] Salvar biblioteca (utilize quando já tiver adicionado jogos à sua biblioteca)")
    print("[6] Importar biblioteca (utilize essa opção se já tiver salvo sua biblioteca)")
    print("[7] Sair\n")

def inserir_jogo(biblioteca):
    nome = input("\nInsira o nome do jogo: ")
    tipo = input("Insira o tipo do jogo: ")
    jogo = {"nome": nome, "tipo": tipo}
    biblioteca.append(jogo)
    print("Jogo inserido com sucesso!")
    exibir_jogos(biblioteca)

def consultar_jogos(biblioteca):
    consulta = input("\nQual jogo você deseja buscar? ")
    encontrados = []
    for jogo in biblioteca:
        if jogo["nome"] == consulta:
            encontrados.append(jogo)
    if encontrados:
        print("Jogo(s) encontrado(s):")
        for jogo in encontrados:
            print(f"Nome: {jogo['nome']}, Tipo: {jogo['tipo']}")
    else:
        print("Jogo não encontrado.")

def alterar_jogo(biblioteca):
    nome_antigo = input("\nDigite o nome do jogo que deseja alterar: ")
    jogo_encontrado = None
    for jogo in biblioteca:
        if jogo["nome"] == nome_antigo:
            jogo_encontrado = jogo
            break
    if jogo_encontrado:
        novo_nome = input("Digite o novo nome do jogo: ")
        novo_tipo = input("Digite o novo tipo do jogo: ")
        jogo_encontrado["nome"] = novo_nome
        jogo_encontrado["tipo"] = novo_tipo
        print("Jogo alterado com sucesso!")
        exibir_jogos(biblioteca)
    else:
        print("Jogo não encontrado.")

def excluir_jogo(biblioteca):
    nome = input("\nDigite o nome do jogo que deseja excluir: ")
    for jogo in biblioteca:
        if jogo["nome"] == nome:
            biblioteca.remove(jogo)
            print("Jogo removido com sucesso!")
            exibir_jogos(biblioteca)
            return
    print("Jogo não encontrado.")

def exibir_jogos(biblioteca):
    print("\nBiblioteca de Jogos:")
    for jogo in biblioteca:
        print(f"Nome: {jogo['nome']}, Tipo: {jogo['tipo']}")

def salvar_biblioteca(biblioteca):
    with open(NOME_ARQUIVO, "w") as arquivo:
        for jogo in biblioteca:
            arquivo.write(f"{jogo['nome']},{jogo['tipo']}\n")
    print("Biblioteca salva!")

def importar_biblioteca():
    biblioteca = []
    try:
        with open(NOME_ARQUIVO, "r") as arquivo:
            for linha in arquivo:
                nome, tipo = linha.strip().split(",")
                jogo = {"nome": nome, "tipo": tipo}
                biblioteca.append(jogo)
        print("Biblioteca importada!")
        exibir_jogos(biblioteca)
        return biblioteca
    except FileNotFoundError:
        print("Nenhum arquivo de biblioteca encontrado.")
        return []

def main():
    #biblioteca = importar_biblioteca()

    while True:
        exibir_menu()
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            inserir_jogo(biblioteca)
        elif opcao == "2":
            consultar_jogos(biblioteca)
        elif opcao == "3":
            alterar_jogo(biblioteca)
        elif opcao == "4":
            excluir_jogo(biblioteca)
        elif opcao == "5":
            salvar_biblioteca(biblioteca)
        elif opcao == "6":
            biblioteca = importar_biblioteca()
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")

    print("Saindo do programa...")

if __name__ == "__main__":
    main()
