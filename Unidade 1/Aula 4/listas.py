numeros = [10, 20, 17, 58, 60]
print(numeros[0])

carros = ["Palio", "Ka", "Virtus", "GranSiena","Palio", "Ka", "Virtus", "GranSiena","Palio", "Ka", "Virtus", "GranSiena"]
print("1 ->", carros)

carros.append("Kombi")
print("2 ->",carros)

carros.remove("Ka")
print("3 ->", carros)

del carros[2]
print("4 -> ", carros)

#carros = sorted(carros) 
#print("5 ->", carros)

for i in carros:
    print(i)