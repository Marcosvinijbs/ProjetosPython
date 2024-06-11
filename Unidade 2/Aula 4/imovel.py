from abc import ABC, abstractclassmethod


class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self._nome = nome
        self._uf = uf
        self._valor = valor
        self._endereco = endereco
        self._area = area


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def uf(self, nome):
        self._nome = nome   


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome      


    '''
    def getNome(self):
        return self.nome    
    
    def setNome(self, nome):
        self.nome = nome
    '''


    def detalhar(self):
        print(self.__dict__)

    def calcularimposto(self):
        return self._valor * 0.02
    
    @abstractclassmethod
    def aluguelSugerido ():
        ... 

class ImovelResidencial(Imovel):
    def __init__(self, nome, valor, uf, endereco = '', area = ''):
        super().__init__(nome, valor, uf, endereco = '', area = '')
        self._quartos = 0
        self._piscina = False

    def aluguelSugerido (self):
        return self._valor * 0.02    
    
    
class ImovelComercial(Imovel):
    
      def aluguelSugerido (self):
        return self.valor * 0.015 
      
      def calcularimposto(self):
          match self._uf:
              case 'DF': taxa = 0.03
              case 'SP': taxa = 0.04
              case 'RJ': taxa = 0.025
              case other: taxa = 0.2
          
          return self._valor * taxa 


casa = ImovelResidencial('Minha Casa', 'DF', 300000)
casa.nome = ("Casa Muito Bonita")
#print(casa.nome)

casa.detalhar() 
#print(casa.aluguelSugerido())
print(casa.calcularimposto())


clinica = ImovelComercial('Clinica x', 'SP', 800000)
#clinica.detalhar()
#print(casa.aluguelSugerido())

print(clinica.calcularimposto())


class ImovelRural:
    def __init__(self, hectares = "", curral = '', produtiva = True):
        self._hectareshectares = hectares
        self._curralcurral = curral
        self._produtiva = produtiva

    def mesPlatacao(self, mes):
        match int(mes):
            case 1 : print('Feijão')            
            case 3 : print('Soja')            
            case other : print('Algodão')  

class Fazenda(Imovel, ImovelRural):
    
    def aluguelSugerido (self):
        return self.valor * 0.015 

'''
fazenda = Fazenda('Fazenda Modelo','GO', 1500000)
fazenda.detalhar()
print(fazenda.calcularimposto())
fazenda.mesPlatacao(3)
'''

'''
imovel = Imovel('Solar do Cerrado', 'DF', 500000)
imovel.detalhar()
imovel.endereco = 'ABC'
imovel.area = 2000
print(imovel.__dict__)         
imovel.detalhar()
'''