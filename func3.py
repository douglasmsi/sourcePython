#!/usr/bin/python3

def boas_vindas(*nomes):
    for item in nomes:
        print("Ola {} Seja bem vindo!".format(item))


boas_vindas('Douglas','Rafael','Lucia')
