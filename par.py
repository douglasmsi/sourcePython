#!/usr/bin/python3
#!/usr/bin/python3

#Ler numero e verificar se ele e par ou impar
# e adicionar ele em uma lista com o Resultado
#[2, 'par']
#[3,'impar']
#
entrada = int(input('Numero: '))
lista = []

if (entrada%2) == 0:
    lista.insert(0,[entrada,'Par'])
else:
    lista.insert(0,[entrada,'Impar'])

print(lista)
