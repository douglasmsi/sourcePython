#!/usr/bin/python3
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux']
except Exception as e:
    print("ERRO:{}".format(e))


db.pessoas.remove()
db.pessoas.insert({'_id':5, 'nome':'joaozinho'})
db.pessoas.update({'_id':5}, {'$set':{'sobrenome':'silva'}})


dados = db.pessoas.find()
dados = [x for x in dados]
print(dados)
