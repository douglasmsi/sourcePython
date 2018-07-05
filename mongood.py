#!/usr/bin/python3
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO:{}".format(e))

dados = db.pessoas.find()
dados = [x for x in dados]
print(dados)
