##f = open('surf.txt')#arquivo deve estar no mesmo diretório
##for linha in f:
##    print(linha.strip())
##f.close()
##
##
##f = open('surf.txt')
##maior = 0 
##for linha in f:
##    nome, pontos = linha.split()=# atribuição multipla
##    if float(pontos) > maior:
##        maior = float(pontos)
##f.close
##print (maior)

##f = open('surf.txt')
##notas = []
##for linha in f:
##    nome, pontos = linha.split()
##    notas.append(float(pontos))       #dei as notas!
##f.close
##notas.sort()
##notas.reverse()
##print(notas[0])
##print(notas[1])
##print(notas[2])



f = open('surf.txt')
notas = {}
for linha in f:
    nome, pontos = linha.split()        #versão Dicionário!
    notas[float(pontos)] = nome         #agora quero notas junto com os nomes!
f.close()
for nota in sorted(notas, reverse = True):
    print(f'{notas[nota]} tem nota {nota}')
