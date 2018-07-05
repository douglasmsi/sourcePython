#!/usr/bin/python3

class Dog():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.energia = 10

    def latir(self):
        print('Au au!')


    def andar(self):
        self.energia -= 1
        print('andando.... energia: {}'.format(self.energia))


dog1 = Dog('bilu', 2)
print(dog1.idade)
dog1.andar()
dog1.latir()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
