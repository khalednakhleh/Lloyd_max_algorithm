#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 07:52:28 2018

Name: khalednakhleh

testing implementations for the LBG algorithm 
first presented in the 1980 paper titled:
    An Algorithm for Vector Quantizer Design
"""

import numpy as np
from sklearn.metrics import mean_squared_error as mse

def distance_distortion(x, A):
    """ measuring distance between input vector x 
    and codebook A through L2 metric.
    Mapping the least distance to the S symbol it represents.
    Mapping input vectors to four symbols s_1 to s_4."""
    
    s_1 = []
    s_2 = []
    s_3 = []
    s_4 = []
    
    distortion = 0
    a = 0
    
    while a < x.shape[1]:
        
        diff = 1000
        i = 0
        while i < A.shape[1]:
            val = np.sqrt(np.sum((np.abs(x[:, a] - A[:, i])) ** 2))
                
            if val < diff:
                q = x[:, a]
                e = i
                diff = val
                
            i = i + 1
        
        distortion = distortion + val
        
        if e == 0:
            s_1.append(q)
        elif e == 1:
            s_2.append(q)    
        elif e == 2:
            s_3.append(q)
        elif e == 3:
            s_4.append(q)

        a = a + 1
        
    return s_1, s_2, s_3, s_4, distortion/x.shape[1]


def initalize_codebook(dim, N):
    return np.random.randint(-2,2, size = (dim,N))  
    
def LBG(x, dim, N, e):
    
    D_1 = 10 ** 8
    A = initalize_codebook(dim, N)
    
    s_1, s_2, s_3, s_4, D_0 = distance_distortion(x, A)
    
    d = (D_1 - D_0) / D_0
    
    print(s_4[0][0])
    print(A)
    print(A[1])
    
    count = 0
    #while d > e:
        
        
    
        
    
    return s_1, s_2, s_3, s_4, D_0

def main():
    
    # seed for random number generation
    seed = 14
    np.random.seed(seed)    
    # number of samples for input vectors
    n = 10
    # number of iterations
    iterations = 200
    # input vector's dimension
    dim = 2
    # number of quantization intervals
    m = 10
    # Codebook dimension
    N = 4
    # variance for Gaussian distributed values            
    variance = 1    
    # mean for Gaussian distributed values     
    mean =  0 
    # epsilon value 
    e = 0.001
    # sample values
    x = variance * np.random.randn(dim, n) + mean
 
###############################################################    
    


    s_1, s_2, s_3, s_4, distortion = LBG(x, dim, N, e)

    w = np.shape(s_1)[0]

    print(np.shape(s_1))
    print(np.shape(s_2))
    print(np.shape(s_3))
    print(np.shape(s_4))
    
if __name__ == "__main__":
    main()
    
    
    
    
    
  
    
    
    
    
    