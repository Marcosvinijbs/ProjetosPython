class Produto:

    def __init__(self, nome , valor , quantidade = 0 ,  marca = '' , modelo = ''):
        self.nome = nome
        self.valor = valor
        self.quantidade= quantidade
        self.marca = marca
        self.modelo = modelo

    def vender(self, quantidade):
        if (quantidade > self.quantidade):
            print("************************")
            print("Não há estoque suficiente")
            print("Quantidade Máxima: ", self.quantidade)
            print("************************")

        else:     
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade  
    


produto0 = Produto("Celular", '2000', 100,'Samsung', 'J8')
produto0.comprar(10)
produto0.vender(110)


produto1 = Produto("Geladeira", '3000', 50 , 'Brastemp','BSP1000' )


produto2 = Produto("Notebook", 4000)
produto2.comprar(1)
produto2.vender(1)

         


print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)