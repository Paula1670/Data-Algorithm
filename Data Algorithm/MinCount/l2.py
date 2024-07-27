import hashlib
import random

def minCount(m, h, k):
    
    M = [1] * k
    
    for x in m:
       
        hV = h(x)
        
        if hV < M[k-1] and hV not in M:
            M[k-1] = hV
            M.sort()
    if M[k-1] == 1:
        return  k - M.count(1)
    else:
        return (k-1)/M[k-1]

def md5(x):
    return int(hashlib.md5(str(x).encode()).hexdigest(),16)/2**128

def sha256(x):
    return int(hashlib.sha256(str(x).encode()).hexdigest(),16)/2**256

def sha512(x):
    return int(hashlib.sha512(str(x).encode()).hexdigest(),16)/2**512

def mod(x):
    return (x % 100)/99


def test():
    n = range(1,10001)
    k = [2,3,10,100,4000]

    for k in k:
        for n in n:
            minCount(n)
            
    
#longitud lita < nmeros elementos(k) --> no aleatorios
#llongitud lita  > nmeros elementos(k) -->aleatorios numeros
