#!/usr/bin/python3

soma = 0
while True:
    num = int(input("Digite um numero ou 0 para sair : "))
    if num == 0:
        break

    soma += num
    print('Total: {}'.format(soma))
