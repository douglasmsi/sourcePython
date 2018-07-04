#!/usr/bin/python3

def manipular_arquivo(nome, modo, conteudo=None):
    if modo == 'r':
        with open(nome, modo) as arquivo:
            return arquivo.readlines()
    elif modo == 'a':
        with open(nome, modo) as arquivo:
            arquivo.write(conteudo+'\n')
            return True


a = manipular_arquivo('nomes.txt', 'r')
manipular_arquivo('nomes.txt', 'a','josevaldo')

print(a)
