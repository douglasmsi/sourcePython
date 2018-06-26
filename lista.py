#!/usr/bin/python3
nomes = ['daniel','maria','jose','joao']

nomes.append(['daniel','prata'])
nomes.insert(0, 'prata')

print(nomes)
print(type(nomes))
print(nomes[-1])
print(type(nomes[-1]))

print(nomes[-1][0])

print(len(nomes))
print(len(nomes[-1]))



numeros = list((range(40,100)))
print(numeros)
