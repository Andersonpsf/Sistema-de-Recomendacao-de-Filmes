import time 

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
    if escolha ==1:
        base = open("BaseDeDados.txt", "r")
        texto = base.read()
        print(texto)

    elif escolha==2:
        base = open("BaseDeDados.txt", "r")
        nome = input("\nDigite o nome do filme: ").lower()
        for line in base:
            filmes = line.split("|")
            if nome in filmes[0].lower():
                encontrado=True
                print(line)
        if encontrado == False:
            print("Filme não encontrado")
            

    elif escolha==3:
        base = open("BaseDeDados.txt", "r")
        genero = input("\nGenero: ").lower()
        for line in base:
            filmes = line.split("|")
            if genero in  filmes[1].lower():
                encontrado = True
                print(line)
        if encontrado==False:
            print("Genero não encontrado")

    elif escolha == 4:
        print("Você saiu do programa.")
        break
    else:
        print("Opção invalida!")
