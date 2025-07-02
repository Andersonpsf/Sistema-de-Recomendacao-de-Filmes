"""
Programa Sistema de recomendação de filmes

Autores: 
    Anderson de Paula Siqueira Filho
    Paulo Henrique de Assis Lima 
    Rafael Pereira

Descrição do programa:
    O programa irá ler uma base de dados com filmes de um arquivo de texto(.txt)
    e irá dar escolhas do que o usuário deseja fazer:
        - Visualizar os filmes do catálogo
        - Pesquisar filmes por nome e receber recomendações relacionadas
        - Pesquisar filmes por gênero
        - Sair do Programa
"""

def MostrarFilmes():
    """
    Essa função serve para apresentar os filmes presentes no arquivo de texto

    Abre o arquivo "BaseDeDados.txt", lê todo o seu conteúdo
    e mostra o catálogo de filmes para o usuário
    """
    base = open("BaseDeDados.txt", "r")
    texto = base.read()
    print("Lista de Filmes \n")
    print(texto)

def MostrarRecomendarFilmes(encontrado, nome):
    """
    Mostra recomendações de filmes baseados no filme pesquisado pelo usuário

    Parâmetros:
    encontrado(Tipo booleana): Serve para indicar certificar que tenha um filme correspondente ao pesquisado
    nome(Tipo String): Variavél do nome digitado pelo usuário e convertida em minúscula para evitar um erro de digitação

    Funcionamento:
    Lê todas as linhas presentes no arquivo de texto e procura por linhas cujo o título seja igual ao nome pesquisado
    Caso encontrado, mostra o filme e recomendações do mesmo gênero, caso não, avisa que nenhum resultado foi encontrado 
    """

    with open("BaseDeDados.txt", "r") as base:
        linhas = base.readlines()

    for line in linhas:
        filmes = line.split("|")
        if nome in filmes[0].lower():
            relacionados = filmes[1]
            encontrado=True
            print(line)
    
    if encontrado==False:
        print("Nenhum resultado encontrado")
    
    else:
        print("Filmes Recomendados com base na pesquisa: ")
        for line in linhas:
            filmes = line.split("|")
            if relacionados in filmes[1] and nome not in filmes[0].lower():
                print(line)


def MostrarPorGenero(encontrado, genero):
    """
    Mostra todos os filmes do gênero pesquisado pelo usuário

    Pârametros:
    encontrado(Tipo Booleana): Serve para indicar certificar que tenha um gênero correspondente ao pesquisado
    genero(Tipo string): Variavél do genero digitado pelo usuário e convertida em minúscula para evitar um erro de digitação
    
    Funcionamento:
    Lê o arquivo de texto linha por linha, certifica-se que tenha o gênero pesquisado e mostra os filmes do mesmo gênero
    Caso não digitado de forma correta, irá informar que nenhum resultado foi encotrado
    """
    
    base = open("BaseDeDados.txt", "r")
    for line in base:
        filmes = line.split("|")
        if genero in filmes[1].lower():
            encontrado=True
            print(line)
    if encontrado==False:
        print("Nenhum resultado encontrado")


while True:
    """
    Interface do Programa

    Vai executar uma ação baseada na opção escolhida
    """
    print("=" * 22)
    print("Recomendação de Filmes")
    print("=" * 22)
    print("\n1 - Mostrar Filmes ")
    print("2 - Buscar por Nome")
    print("3 - Buscar por Gênero")
    print("4 - Sair")
    encontrado = False

    escolha = int(input("Opção: "))
    print("\n")
    if escolha == 1:
         #Mostra todos os filmes do catálogo

        MostrarFilmes()

    elif escolha==2:
        #Mostra recomendações de filmes semelhantes ao que foi escrito

        nome = input("\nDigite o nome do filme: ").lower()
        MostrarRecomendarFilmes(encontrado, nome)
 
    elif escolha==3:
        #Mostra todos os filmes do gênero pesquisado
        
        genero = input("\nGenero: ").lower()
        MostrarPorGenero(encontrado,genero)


    elif escolha == 4:
        #Sai do programa
        
        print("Você saiu do programa.")
        break
    else:
        #Caso o usuário, por acidente, digite uma opção fora das oferecidas
        print("Opção invalida!")
