#lista fluxo caixa
fluxo_caixa = []

# título, orientações de comando 1 receita,2 despesa e outro num pra encerrar
print("--------------")
print("@ Fluxo caixa")
print("--------------")
print("1 - Adicionar receita")
print("2 - Adicionar despesa")
print("3 - sair")
print("\n#Digite outro numero para encerrar #\n")

#criar uma função add transacao com input nome input valor float e append de 'nome' e 'valor' na lista fluxo caixa.
def adicionar_transacao():
    nome = input("Nome:")
    valor = float(input("Valor:"))
    fluxo_caixa.append({
        "nome": nome,
        "valor": valor
    })

#iniciar loop while True
while True:

    # input de opção
    opcao = int(input("Digite a opção: "))

    #condicionais if opcao um elif opção 2 else break
    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

# inicializar variavel total em 0
total = 0

# loop for em lista principal fluxo caixa para imprimir nome e valor acessando as chaves da lista
for fc in fluxo_caixa:
    print("nome:", fc['nome'], ", Valor: R$", fc['valor'])
    # calculo para somar total +=
    total += fc['valor']  #total = total + fc['valor]
#print do saldo atual total
print("Saldo atual: R$", total)
    