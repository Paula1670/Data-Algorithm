import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import bernoulli



def simulator_n_known(n):
    
    i = 0
    nb = 1
    slot = "NULL"
    
    p = [1/n for k in range(n)]
    
    
    while(slot != "SINGLE"):
        
        i = i+1
        tempo = 0
        for j in range(n):
            if(bernoulli.rvs(p[j], 0, size = 1)[0] == 1):
                tempo = tempo + 1
            
        if(tempo==1):
            slot = "SINGLE"
            return i,nb
        else:
            i = i+1
            nb = nb+1
    
    
    
def number_of_slots_n_known(n,nb_test):
    
    nb_slot = []                            #list with the number of the slot used for each test
    
    for i in range(nb_test):
        nb_slot.append(simulator_n_known(n)[1])
        
    plt.hist(nb_slot,bins=max(nb_slot),align='left',rwidth=0.7)
    plt.xlabel("Number of slots required")
    plt.ylabel("Number of time the amount of slots is required")
    plt.title("Histogram for known n = "+str(n)+", number of tests = " + str(nb_test))
    
    return nb_slot
    
    
def mean_variance_n_known(n,nb_test):
    
    nb_slot = np.array(number_of_slots_n_known(n,nb_test))
    
    return nb_slot.mean(), nb_slot.var()
    


esp,var = mean_variance_n_known(10,1000) #1000 experiments, 10 devices
    
print("Mean value = " + str(esp) + ", Variance = " + str(var))
    