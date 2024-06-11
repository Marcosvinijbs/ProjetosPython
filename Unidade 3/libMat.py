import matplotlib.pyplot as plt

'''
meses = [ 'Jan' , 'Fev', 'Mar', 'Abr', 'Mai', 'Jun']
qtdTi= [ 60, 52, 76, 89, 108, 95]
qtdRh = [ 40,72,17,28,87,56]

plt.plot(meses, qtdTi, label = "TI", color="blue", marker="o")
plt.plot(meses, qtdRh, label = "Rh", color="red", marker=".")
plt.title('Chamados abertos')
plt.xlabel('Meses')
plt.ylabel('Quantidade')
plt.legend()
plt.show()
'''

navegadores = ['Chrome', 'Firefox', 'Edge']
qtd = [1200, 600, 200]
cores = ['red', 'orange', 'blue']



plt.pie(qtd,labels=navegadores, colors=cores)
plt.show()
