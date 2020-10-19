from random import randint
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

def selectionSort(lista):
    for i in range(len(lista) - 1):
        minIndx = i
        minVal= lista[i]
        j = i + 1
        while j < len(lista):
            if minVal > lista[j]:
                minIndx = j
                minVal= lista[j]
            j += 1
        temp = lista[i]
        lista[i] = lista[minIndx]
        lista[minIndx] = temp       
    return lista

def desenhaGrafico(x,y1,y2):
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111)
    ax.plot( x, y1, label = 'Lista Aleatória')
    ax.plot( x, y2, label = 'Pior caso')
    plt.title('Algoritmo Selectionsort')
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
    y.append(timeit.timeit("selectionSort({})".format(x[i]),setup="from __main__ import selectionSort",number=1))

for i in range(len(w)):
    k.append(timeit.timeit("selectionSort({})".format(w[i]),setup="from __main__ import selectionSort",number=1))

print("Tamanho das listas: "+str(z))
print("Tempo de listas aleatorias: "+str(y))
print("Tempo de listas pior caso: "+str(k))   
desenhaGrafico(z,y,k)
