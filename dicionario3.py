import os

mensagens = []  # temos uma lista vazia chamada mensagens

nome = input("Nome: ")  # recebemos um nome

while True:  # iniciamos um loop infinito, em cada execução ele limpa o terminal, verifica se tem mensagens
    # limpando terminal
    os.system('cls' if os.name == 'nt' else 'clear')

    if len(mensagens) > 0:  # se tiver mensagens ele exibe
        for m in mensagens:
            print(m['nome'], "-", m['texto'])

    print("________________")  # divisão para separar as informações

    # obtendo texto que o usuário vai colocar no chat
    texto = input("mensagem: ")
    if texto == "fim":  # verifica se é a palavra fim, se for encerra o loop, caso contrário segue adicionando a mensagem na lista
        break

    # adicionando mensagem na lista
    mensagens.append({
        "nome": nome,
        "texto": texto
    })
