#!/usr/bin/python3

#Lista de nome vazia
# Ler nomes, adicionar na lista até digitar sair
#mostrar a lista no final

with open('nomes.txt','a') as arquivo:
    while True:
        valor = input("Digite um nome ou Sair : ")
        if valor.strip().lower() == 'sair':
            break

        arquivo.write(valor+"\n")

with open('nomes.txt', 'r') as arquivo2:
    var = arquivo2.readlines()

print(var)
