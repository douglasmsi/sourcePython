#!/usr/bin/python3

def somar(x,y):
    return x + y

#b = somar(3,2)
#print(b)
#exit()

def par_impar(numero):
    if (numero%2) == 0:
        print('Par')
    else:
        print('Impar')


def boas_vindas(nome, idade):
    print('Ola sou o {} tenho {} anos '.format(nome, idade))


boas_vindas('douglas',29)
entrada = int(input('Numero: '))
par_impar(entrada)
