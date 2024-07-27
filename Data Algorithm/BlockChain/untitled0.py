# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:53:24 2023

@author: Paula
"""
#a)
import matplotlib.pyplot as plt
import numpy as np
import math as ma
from scipy.stats import bernoulli
from scipy.stats import poisson
import scipy


def qm(q,m):
    return (q/(1-q))**m

def P_nakamoto(q,n):
    
    a = n*(q/(1-q))
    somme = 0
    
    for k in range(n):
        somme += (a**k)*np.exp(-a)*(1 - qm(q,n-k))/(ma.factorial(k))
    
    return 1 - somme

def P_grunspan(q,n):
    
    somme = 0
    p = 1-q
    
    for k in range(n+1):
        somme += ((p**n)*(q**k) - (q**n)*(p**k))*scipy.special.binom(k+n-1,k)
    
    return 1 - somme
    
    
    

def graph(n):
    
    q_inter = np.linspace(0.001, 1/2.001, 100)
    naka = []
    grun = []
    
    for i in range(len(q_inter)):
        naka.append(P_nakamoto(q_inter[i],n))
        grun.append(P_grunspan(q_inter[i],n))
        
        
    plt.scatter(q_inter,naka,marker="x")
    plt.scatter(q_inter,grun,marker="x")



def chooser(prob): #0.1%=0.1/100
    
    n_inter = np.linspace(1, 100000, 100000, dtype=int)
    q_inter = np.linspace(0.001, 1/2.001, 100)
    
    list_q = []
    list_n = []
    
    for q in q_inter:
        i = 0
        proba = P_grunspan(q,n_inter[i])
        while proba > prob:
            i = i + 1
            proba = P_grunspan(q,n_inter[i])
         
        '''  
        print(q)
        print("-----------------")
        print(P_grunspan(q,n_inter[i]))
        print("======================")
        print(i)
        print("~~~~~~~~~~") 
        '''
        list_q.append(q)
        list_n.append(n_inter[i])
        
        
    plt.scatter(list_q,list_n)
                

def attack(n,q):
    
    limite = n + 35
    
    honest = 0
    attack = 0
    
    bernoulli.rvs(q)
    
    while True:
        
        test = bernoulli.rvs(q)
        
        if test == 1:
            attack += 1
        else:
            honest += 1
        
        if (honest >= n) and (honest - attack <= 0):
            return 1
        elif honest - attack > limite:
            return 0
    
    
def monte_carlo(n):
    nb_exp = 1000
    q_inter = np.linspace(0.001, 1/2.001, 100)
    
    list_q = []
    list_monte = []
    
    for q in q_inter:
        nb_attack_success = 0
        for i in range(nb_exp):
            
            test = attack(n,q)
            
            if test == 1:
                nb_attack_success += 1
            
        list_monte.append(nb_attack_success/nb_exp)
        list_q.append(q)
    
    plt.scatter(list_q,list_monte,marker="x")
""" graph(n)
    plt.legend(["Monte Carlo","Nakamoto","Grunspan"])
    plt.title("Graph for n = "+str(n)+" and number of tests = "+str(nb_exp)+"")"""
    


monte_carlo(4)
graph(4)
#chooser(1/100) #0.1%=0.1/100
"""
print(P_grunspan(1,0.001))
print(P_nakamoto(1,0.001))"""