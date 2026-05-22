jogada1 = int(input("Jogador 1, escolha entre pedra(0) papel(1) e tesoura(2): "))
jogada2 = int(input("Jogador 2, escolha entre pedra(0) papel(1) e tesoura(2): "))

if jogada1 == 0:
    if jogada2 == 0:
        print("Empate")
    if jogada2 == 1:
        print("Jogador 2 ganhou")
    if jogada2 == 2:
        print("Jogador 1 ganhou")
if jogada1 == 1:
    if jogada2 == 1:
        print("Empate")
    if jogada2 == 2:
        print("Jogador 2 ganhou")
    if jogada2 == 0:
        print("Jogador 1 ganhou")
if jogada1 == 2:
    if jogada2 == 2:
        print("Empate")
    if jogada2 == 0:
        print("Jogador 2 ganhou")
    if jogada2 == 1:
        print("Jogador 1 ganhou")