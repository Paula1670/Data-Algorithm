
import math
from l2 import *
from matplotlib import pyplot as plt


def generateMultisets(n):
    M = []
    length = 1
    for i in range(0,n):
        m = List_function(length)
        toIncr = int(length*(length+1)/2)
        m = [x+toIncr for x in m]
        length =length +1
        M.append(m)
    return M

def List_function(n):
    list_array = []
    for i in range(n):
        list_array.append(i)
    return(list_array)



def zad5b():
    multisets = generateMultisets(1000)
    print("multisets generated")
    k = [2,3,10,100,400]


    for kV in k:
        x = []
        y = []
        for multiset in multisets:
            _n = minCount(multiset,md5,kV)
            n = len(multiset)
            x.append(n)
            y.append(_n/n)
        
        plt.scatter(x, y) 
        plt.show()

def zad5c(h =sha256, k =210):
    multisets = generateMultisets(1000)
    good =0
    bad =0
    for multiset in multisets:
        _n = minCount(multiset,h,k)
        n = len(multiset)

        if abs( _n/n - 1) < 0.1:
            good += 1
        else:
            bad +=1
    
    print(good/(good + bad))
#Lo hize mil  veces pa ver cuantas word satisfacen la sol e intentando conseguir el case, el case es 250
#
def zad6():
    zad5c(md5,100)
    zad5c(mod,100)
    zad5c(sha512,100)
#hash funcion es buena, no tiene muchas collisiones


def zad7():
    multisets = generateMultisets(1000)
    x = []
    y = []
    plusDelta = []
    minusDelta =[]
    k = 400
    alfa = 0.5/100
    for multiset in multisets:
        if len(multiset) < 400:
            continue
        _n = minCount(multiset,md5,k)
        n = len(multiset)
        x.append(n)
        y.append(_n/n)
        var = (n-k+1)*n/(k-2)
        
        delta = math.sqrt(var/alfa)
        plusDelta.append(1+delta)
        minusDelta.append(1-delta)
    plt.axhline(1+delta,color="red")
    plt.scatter(x, y,marker='.') 
    plt.plot(x, plusDelta,  label ="1+delta") 
    plt.plot(x, minusDelta, label  = "1-delta") 
    
    plt.legend()
    plt.show()

zad7()