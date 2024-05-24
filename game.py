#importar os
import os

# Se o jogo tivesse múltiplos jogadores, cada jogador poderia ter um nome único. Isso seria útil para identificar quem é quem no jogo.
# Definindo o jogador - armazenar um dicionário em uma variável contendo nome, x de valor 0 e y de valor 0
player = {"nome": "Python", "x": 0, "y": 0}

# criar Função para movimentar o jogador com if direção d,a,w,s no eixo x e y com um if e 3 elifs
def andar(direcao):
    if direcao == "d":
        player['x'] += 1
    elif direcao == "a":
        player['x'] -= 1
    elif direcao == "w":
        player['y'] -= 1
    elif direcao == "s":
        player['y'] += 1

# criar Loop principal do jogo
while True:
    # os para limpar o terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    # Desenhando limites do mapa inicio - traços
    print("-----------------------------")
    # loop for para y com range 5
    for y in range(5):
        # loop for para x com range 10
        for x in range(10):
            # condiciona if se player x for igual a x e player y for igual a y
            if player["x"] == x and player['y'] == y:
                #print  emoji com end igual a aspas vazias
                print("🙂", end="")
            #else com print de emoji com end igual a aspas vazias
            else:
                print("🟩", end="")
        #print separador de espaços
        print("\n")
    # Desenhando limites do mapa inicio - traços
    print("-----------------------------")

    # input para receber a próxima direção ou fim para sair
    direcao = input("Próxima direção (w,s,d,a) ou 'fim' para sair: ")
    
    # condicional se direcao for igual a fim break loop while
    if direcao == 'fim':
        break
    # chamar função andar para a direção
    andar(direcao)

    # print da posição do jogador
    print(f"{player['nome']} está agora na posição ({player['x']}, {player['y']})")