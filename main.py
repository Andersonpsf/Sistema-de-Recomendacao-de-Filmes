import time 

while True:
    print("=" * 22)
    print("Recomendação de Filmes")
    print("=" * 22)
    print("1 - Mostrar Filmes ")
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
        nome = (input("Digite o nome do filme: ")).capitalize()
        print(nome)
        for line in base:
            filmes = line.split("|")
            if nome in filmes[0]:
                print(line)
                encontado = True
                break

            
    elif escolha == 4:
        print("Você saiu do programa.")
        break
    else:
        print("Opção invalida!")
