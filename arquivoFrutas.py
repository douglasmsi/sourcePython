#!/usr/bin/python3

#Lista de nome vazia
# Ler nomes, adicionar na lista até digitar sair
#mostrar a lista no final

with open('frutas.txt', 'r') as arquivo:
    var = arquivo.readlines()
    alterado = []
    cont = 1
    for linha in var:
        linha = linha.replace('\n', '-{}\n'.format(cont))
        alterado.append('{}-{}'.format(linha,cont))
        cont += 1

with open('novo.txt','a') as arquivo:
    for linha in alterado:
        arquivo.write(linha)


print(alterado)
