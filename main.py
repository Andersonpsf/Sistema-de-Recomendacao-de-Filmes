def MostrarFilmes():
    base = open("BaseDeDados.txt", "r")
    texto = base.read()
    print(texto)

def MostrarRecomendarFilmes(encontrado, nome):
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
        print("Filmes Recomendados: ")
        for line in linhas:
            filmes = line.split("|")
            if relacionados in filmes[1]:
                print(line)


def MostrarPorGenero(encontrado, genero):
    base = open("BaseDeDados.txt", "r")
    for line in base:
        filmes = line.split("|")
        if genero in filmes[1].lower():
            encontrado=True
            print(line)
    if encontrado==False:
        print("Nenhum resultado encontrado")


while True:
    print("=" * 22)
    print("Recomendação de Filmes")
    print("=" * 22)
    print("\n1 - Mostrar Filmes ")
    print("2 - Buscar por Nome")
    print("3 - Buscar por Gênero")
    print("4 - Sair")
    encontrado = False

    escolha = int(input("Opção: "))
    if escolha == 1:
        MostrarFilmes()

    elif escolha==2:
        nome = input("\nDigite o nome do filme: ").lower()
        MostrarRecomendarFilmes(encontrado, nome)
 
    elif escolha==3:
        genero = input("\nGenero: ").lower()
        MostrarPorGenero(encontrado,genero)


    elif escolha == 4:
        print("Você saiu do programa.")
        break
    else:
        print("Opção invalida!")
