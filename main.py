import time 
base = open("BaseDeDados.txt", "r")
while True:
    print("=" * 22)
    print("Recomendação de Filmes")
    print("=" * 22)
    print("1 - Mostrar Filmes ")
    print("2 - Buscar por Nome")
    print("3 - Buscar por Gênero")
    print("4 - Sair")


    escolha = int(input("Opção: "))
    if escolha ==1:
        texto = base.read()
        print(texto)
    elif escolha==2:
        
        nome = input("Digite o nome do filme: ").lower()
        for line in base:
            filmes = line.split("|")
            if nome in filmes[0].strip().lower():
                print(line)
            

    elif escolha==3:
        genero = input("Genero: ").lower()
        for line in base:
            filmes = line.split("|")
            if genero in  filmes[1].lower():
                print(line)
            
    elif escolha == 4:
        print("Você saiu do programa.")
        break
    else:
        print("Opção invalida!")
