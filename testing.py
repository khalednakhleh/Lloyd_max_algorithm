#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:05:59 2018

Name: khalednakhleh
"""

import numpy as np
from scipy import integrate
from scipy.stats import norm

#####################################################################
"""
Scalar quantization of a 1-D input source vector x. 

Lloyd-max algorithm is for finding the optimal quantization points 
and boundires that best minimze the quantization error rate. 

The script file starts with an inital set of intervals. 
"""
#####################################################################
   
def lloyd_max(x, m, iterations):
  
    intervals = np.linspace(np.min(x) - 1, np.max(x) + 1, m)
    centroids = np.zeros(m - 1)
    
    print("\nInitial interval values: \n\n" + str(intervals))
          
    v = 0
    
    while v < iterations:
        
        i = 0
         
        while i < centroids.shape[0]:
            
            n_1 =  integrate.quad(lambda x: x * norm.pdf(x), intervals[i], intervals[i + 1])[0]
            n_2 =  integrate.quad(lambda x: norm.pdf(x), intervals[i], intervals[i + 1])[0]              
                
            centroids[i] = n_1/n_2           
            i = i + 1
                      
        q = 0
            
        while q < centroids.shape[0] - 1:
    
            intervals[q + 1] = (centroids[q] + centroids[q + 1]) / 2
                
            q = q + 1
            
        
        v = v + 1

    return centroids, intervals      


def main():
        
    # number of samples for random variable
    n = 10 ** 6
    # number of iterations
    iterations = 10
    # number of quantization intervals
    m = 20
    # variance for Gaussian distributed values            
    variance = 1    
    # mean for Gaussian distributed values     
    mean =  0       
    # sample values
    x = variance * np.random.randn(n) + mean
    
#####################################################################
    
    centroids, intervals = lloyd_max(x, m, iterations)
    
    print("\nFinal centroids value: \n\n" + str(centroids))
    print("\nFinal intervals value: \n\n" + str(intervals))
    


if __name__ == "__main__":
        
    main()
        
        
    
 
    
    
    
    
    