import random
print("====== Game de Pedra, Papel e Tesoura =====")
while True:
    player1 = input("Player 1, escolha entre pedra, papel e tesoura (ou digite 'sair' para encerrar): ")
    
    if player1 == 'sair':
        print("Jogo encerrado. Obrigado por jogar!")
        break
    elif player1 != "pedra" and player1 != "papel" and player1 != "tesoura":
        print("Opção inválida. Tente novamente.")

    cpu = None
    match player1:
        case "pedra":
            cpu = random.choice(["pedra", "papel", "tesoura"])
        case "papel":
            cpu = random.choice(["pedra", "papel", "tesoura"])
        case "tesoura":
            cpu = random.choice(["pedra","papel","tesoura"])
# f significa que é uma string formatada
    print(f"Player 1 escolheu {player1}")
    print(f"CPU escolheu {cpu}")

    print("====== Resultado =====")

    if player1 == cpu:
        print("Empate!")
    elif player1 == "pedra" and cpu == "tesoura":
        print("Player 1 venceu!")
    elif player1 == "papel" and cpu == "pedra":
        print("Player 1 venceu!")
    elif player1 == "tesoura" and cpu == "papel":
        print("Player 1 venceu!")
    else:
        print("CPU venceu!")
