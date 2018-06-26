#!/usr/bin/python3
mensagem = 'Bem vindo'
aluno = input("Aluno: ")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
media = (n1+n2)/2.0

if media >= 7.0:
    result = 'Aprovado'
elif media < 7.0 and media > 4.0:
    result = "Recuperacao"
else:
    result = 'Reprovado'

print("""
        Aluno: {}
        Media: {}
        Resultado: {}
        """.format(aluno,media, result))

print ("{} a sua nota media e {} foi {}".format(aluno,media, result))
