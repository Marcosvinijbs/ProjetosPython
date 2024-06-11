import pandas as pd

cidades = [
           { 'nome': 'Distrito Federal', 'uf': 'DF', 'população': 3121121},
           { 'nome': 'São Paulo', 'uf': 'SP', 'população': 11821212},
           { 'nome': 'Rio de Janeiro', 'uf': 'RJ', 'população': 5021212},
           { 'nome': 'Recife', 'uf': 'PE', 'população': 1090212},
]

dataFrame = pd.DataFrame(cidades)

#print(dataFrame)

ordenadas = dataFrame.sort_values(by='população', ascending= False)

print(ordenadas)