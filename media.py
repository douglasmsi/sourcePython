#!/usr/bin/python3
mensagem = 'Bem vindo'
aluno = input("Aluno: ")
n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
media = (n1+n2)/2.0
aluno1 = aluno.strip()
print ("{} a sua nota media e {} {}".format(aluno,media, aluno1))
