import random
import timeit
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    lista = list(range(tam))
    random.shuffle(lista)
    return lista

def geraListaPiorCaso(tam):
    lista = []
    lista = list(range(tam))
    lista.reverse()
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        val = lista[i]
        j = i - 1
    while (j >= 0) and (lista[j] > val):
        lista[j+1] = lista[j]
        j = j - 1
        lista[j+1] = val
    return lista

def desenhaGrafico(x,y1,y2):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot( x, y1, label = 'Lista Aleatória')
    ax.plot( x, y2, label = 'Pior caso')
    plt.title('Algoritmo InsertionSort')
    plt.legend()
    plt.ylabel('Tempo')
    plt.xlabel('Tamanho das Series')
    plt.savefig('grafico.png', format='png')
    plt.show()

z = [1000,2000,3000,4000,5000,8000,11000,15000]
#z = [100,1000]
x = []
w = []
y = []
k = []

for i in z:
    x.append(geraLista(i))
for i in z:
    w.append(geraListaPiorCaso(i))

for i in range(len(x)):
    y.append(timeit.timeit("insertionSort({})".format(x[i]),setup="from __main__ import insertionSort",number=1))

for i in range(len(w)):
    k.append(timeit.timeit("insertionSort({})".format(w[i]),setup="from __main__ import insertionSort",number=1))

print("Tamanho das listas: "+str(z))
print("Tempo de listas aleatorias: "+str(y))
print("Tempo de listas pior caso: "+str(k))   
desenhaGrafico(z,y,k)
