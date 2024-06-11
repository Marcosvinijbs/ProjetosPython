arquivo = open('pessoas.txt', 'w')


arquivo.write('Orion\n')
arquivo.write('Maria\n')

arquivo.close()

with open('pessoas.txt', 'r+') as arquivoLeitura:
    for linha in arquivoLeitura:
        print(linha)

