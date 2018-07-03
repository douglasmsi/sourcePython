#!/usr/bin/python3

#nome = input('Digite o nome do arquivo: ')

def abre_arquivo(nome):
    try:
        with open(nome, 'r') as arq:
            return arq.readlines()
    except Exception as e:
        return "Erro {}".format(e)


def escr_arq(nome_arq, conteudo):
    try:
        with open(nome_arq,'w') as arq:
            arq.writelines(conteudo)
            return True
    except Exception as e:
        return "Erro: {}".format(e)

def alterar_lista(lista):
    lista1 = []
    for x in lista:
        lista1.append('{}\n'.format(x))
    return lista1

nomes = ['daniel','teste']
#arquivo = abre_arquivo(nome)
print(alterar_lista(nomes))
#print(arquivo)

#escr_arq('nomes.txt',abre_arquivo(nome))
