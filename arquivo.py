#!/usr/bin/python3

with open('frutas.txt', 'a') as arquivo:
    arquivo.write("limao\n")

with open('frutas.txt', 'r') as arquivo:
    print(arquivo.readline())
    print(arquivo.readline())
    arquivo.seek(0)
    print(arquivo.readline())
