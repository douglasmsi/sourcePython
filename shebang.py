#!/usr/bin/python3

nome = input('Digite o nome do arquivo: ')

with open(nome, 'r+') as arquivo:
    conteudo = arquivo.readlines()
print(conteudo[0])


shebang = "\#!/usr/bin/python3\n"
if conteudo[0] != shebang:
    conteudo.insert(0, '#!/usr/bin/python3\n')
    with open(nome, 'w') as arquivo:
        for linha in conteudo:
            arquivo.write(linha)
