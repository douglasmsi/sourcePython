#!/usr/bin/python3

from random import choice, randint

def boas_vindas(**kargs):
    print("Ola {} {} seja bem vindo! ".format(kargs['nome'],kargs['sobrenome']))


boas_vindas(nome='daniel',teste='teste',sobrenome='teste')


nomes = ['daniel','douglas','maria',  'teste']
a = randint(0,100)
print(choice(nomes), a)

var = lambda x: x*2
print(var(4))
