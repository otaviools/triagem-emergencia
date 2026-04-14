from collections import deque

fila_preferencial = deque()
fila_normal = deque()

def inserir(nome): #Função inserir nome na fila
    escolha = input(f"{nome} é (1) Normal ou (2) Preferencial? ")
    if escolha == "2":
        fila_preferencial.append({"nome": nome, "espera": 0})
        print(f"--{nome} entrou como Preferencial")
    else:
        fila_normal.append({"nome": nome, "espera": 0})
        print(f"--{nome} entrou como Normal")

def chamar(): #Função chamar proximo fila
    if fila_preferencial:
        paciente = fila_preferencial.popleft()
        print(f"Chamando: {paciente['nome']} (Preferencial)")
    elif fila_normal:
        paciente = fila_normal.popleft()
        print(f"Chamando: {paciente['nome']} (Normal)")
    else:
        print("Fila vazia!")
        return

    for p in fila_normal: #Estrutura para promoção de espera
        p["espera"] += 1
        if p["espera"] > 5:
            print(f"AVISO | Promoção por espera: {p['nome']} subiu para Preferencial!")
            fila_preferencial.append(p)

    while fila_normal and fila_normal[0]["espera"] > 5:
        fila_normal.popleft()

def mostrar(): #Função mostrar fila atual
    print("\n--- FILA ATUAL ---")
    for p in fila_preferencial:
        print(f"[{p['nome']} | Pref]")
    for p in fila_normal:
        print(f"[{p['nome']} | Norm | Espera: {p['espera']}]")

# Menu principal
while True:
    print("\n1 - Inserir paciente")
    print("2 - Chamar próximo")
    print("3 - Mostrar fila")
    print("4 - Sair")
    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do paciente: ")
        inserir(nome)
    elif opcao == "2":
        chamar()
    elif opcao == "3":
        mostrar()
    elif opcao == "4":
        break