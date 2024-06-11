import json


pessoas = [

    {'nome':'Marcos', 'telefone': '(61) 98602-2151', 'endereco': 'ABC'},
    {'nome':'Joao', 'telefone': '(61) 5555-2151', 'endereco': 'DEF'},
    {'nome':'Marcos', 'telefone': '(61) 8547-22151', 'endereco': 'GHI'}

]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4)