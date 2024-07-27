import numpy as np
import random as rd
import matplotlib.pyplot as plt
import hashlib as hsh
import struct
from scipy.integrate import quad
from minCount import *

def m():
    return rd.randint(1,6)


def po(w, max_width):
    rho = max_width - w.bit_length() + 1
    
    if rho <= 0:
        raise ValueError('w overflow')

    return rho
    

def get_alpha(p):
    if not (4 <= p <= 16):
        raise ValueError("p=%d should be in range [4 : 16]" % p)

    if p == 4:
        return 0.673

    if p == 5:
        return 0.697

    if p == 6:
        return 0.709

    return 0.7213 / (1.0 + 1.079 / (1 << p))


def HyperLogLog(b,SET):

    alpha = get_alpha(b)  

    m = 2**b
    M = np.zeros(m)
    
    for s in SET:
        
        
        if isinstance(s, str):
            s = s.encode('utf-8')
        elif not isinstance(s, bytes):
            s = bytes(s)
        
        x = struct.unpack('!Q', hsh.sha256(s).digest()[:8])[0]
        j = x & (m - 1)        
        w = x >> b
    
        M[j] = max(M[j], po(w, 64 - b))
        
        
    somme = 0
    for i in range(m):
        somme += 2**(-M[i])
        
    estim = alpha * (m**2) * (somme**(-1))
    
    
    if(estim < (5/2) * m):
        
        V = 0
        for k in range(len(M)):
            if M[k] == 0:
                V += 1
        if(V != 0):
            return -m*np.log(V/m)

    elif(estim > (2**32)/30):
        H = 2**32
        return -H*np.log((H - estim)/H)
    
    else:
        return estim


def nchap_sur_n(Mlist,b):
    
    results = []
    index = []
    for it in range(len(Mlist)):
        index.append(it)
        results.append(HyperLogLog(b,Mlist[it])/(it+1))
        
    plt.scatter(index,results)
    
    return results
    

Mlist = []
last = 0

for i in range(1,1000+1):
    tempo = []
    for j in range(i):
        for k in range(m()):
            tempo.append(j+last)
    last = last + i
    rd.shuffle(tempo)
    Mlist.append(tempo)
    
    
print("k")

#b = 6
#resultats = nchap_sur_n(Mlist,b)

#k*32 = 2^b*5

print("jj")
#b=5, k=5
#b=6, k=10
#b=7, k=20
print("mincount:", mincount(Mlist,md5_mc, 5))
print("hyperloglog:", nchap_sur_n(Mlist, 5))

