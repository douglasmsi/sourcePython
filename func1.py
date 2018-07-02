#!/usr/bin/python3

nome = input('Digite o nome do arquivo: ')

def abre_arquivo(nome):
    try:
        with open(nome, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return "Erro {}".format(e)

arquivo = abre_arquivo(nome)
print(arquivo)
