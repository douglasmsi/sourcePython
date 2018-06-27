#!/usr/bin/python3

#Lista de nome vazia
# Ler nomes, adicionar na lista até digitar sair
#mostrar a lista no final
lista = []
while True:
    valor = input("Digite um nome ou Sair : ")
    if valor.strip().lower() == 'sair':
        break

    lista.append(valor)
    print('Lista: {}'.format(lista))
