import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import bernoulli




def simulator_n_unknown(n,u):
    
    i = 0
    nb = 1
    slot = "NULL"
    nb_round = 1
    
    p = [1/(2**i) for i in range(1,math.ceil(np.log2(u))+1)]
    
    while(slot != "SINGLE"):
        
        taille = len(p)
        while(i >= taille):
            p = p+p
            nb_round += 1
            taille = len(p)


        tempo = 0
        for j in range(n):

            if(bernoulli.rvs(p[i], 0, size = 1)[0] == 1):
                tempo = tempo + 1
            
        
            
        if(tempo==1):
            slot = "SINGLE"
            return i,nb,nb_round
        else:
            i = i+1
            nb = nb+1
    
    
    
def number_slots_n_unknown(n,u,nb_test):
    
    nb_slot = []
    
    for i in range(nb_test):
        nb_slot.append(simulator_n_unknown(n,u)[1])
        
    plt.hist(nb_slot,bins=max(nb_slot),align='left',rwidth=0.7)
    plt.xlabel("Number of slots required")
    plt.ylabel("Number of time the amount of slots is required")
    plt.title("Histogram for upper bound u = "+str(u)+", n = "+str(n)+", number of tests = " + str(nb_test))


    return nb_slot
#primer slot Es el mas alto pq solo hay 2 dispositivos. 
#no es mucha la prob of devices al mismo tiempo. 
#Podemos tenerlos en el primer slot.




#prob pal cuarto slot cd solo tengo 4 rondas, es la mas baja
    
#number_slots_n_unknown(16,16,3333)
#Uncomment the line to show the histogram for unknown n and upper bounf u



#------------------------------ Task 4 --------------------------------
# We use a Monte Carlo method to estimate the lambda constant


def monte_carlo(n,u,nb_simus):
    
    compteur = 0
    
    for i in range(nb_simus):
        
        if(simulator_n_unknown(n,u)[2]==1):
            compteur = compteur + 1
        
    print(compteur/nb_simus)
    


#monte_carlo(10, 10, 1333)

#la prob de selecionar a lider en la primera ronda 
#es mas alta q la costante, usamos este metodo
#hacemos muchos tests, y dividimos el resultado de los tests positivos 
#entre el numero d tests

#queremos los resultados solo de 1 ronda






