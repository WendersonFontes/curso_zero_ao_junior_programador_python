# parte 1
notas = []

for x in range(5):
    codigo_aluno = input('RM: ')
    nota = float(input('Nota: '))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print("quantidade de notas", len(notas))

# parte 2
#for n in notas: #percorrer na lista criada, n será uma variável temporária que armazena cada sub-lista (par [RM, nota]) durante cada iteração do loop.
#    codigo_aluno = n[0] #Aqui, estamos acessando o primeiro elemento da sub-lista n 
#    nota = n[1]
#    print("O RM", codigo_aluno,"tirou a nota: ", nota)


for n in notas:
    codigo_aluno = n[0]
    notas = n[1]
    print(f'O RM {codigo_aluno} tirou a nota: {notas}')