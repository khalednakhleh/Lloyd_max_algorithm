#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 16:37:55 2018

Name: khalednakhleh
"""
import numpy as np
from lloyd_max import Lloyd_max
import time

#####################################################################
"""
Scalar quantization of a 1-D input source vector x. 

Lloyd-max algorithm was used to find the optimal quantization points 
and intervals that best minimize the quantization error rate. 

The script file starts with an inital set of intervals. Algorithm implementation
can be found in the lloyd_max.py file.
"""
#####################################################################

def main():
        
    # number of samples for random variable
    n = 10 ** 6
    # number of iterations
    iterations = 300
    # number of quantization intervals
    m = 10
    # variance for Gaussian distributed values            
    variance = 1    
    # mean for Gaussian distributed values     
    mean =  0       
    # sample values
    x = variance * np.random.randn(n) + mean
    
#####################################################################
    
    start = time.time()                            # Starting timer
    model = Lloyd_max(n, m, x, iterations)         # Initalizing the algorithm
    end = time.time()                              # Ending timer
    
    # Printing the results and elapsed time
    print("\nFinal centroids values: \n\n" + str(model.centroids))
    print("\nFinal intervals values: \n\n" + str(model.intervals))
    print("\n\nTotal run time: " + str(round(end - start, 3)) + " seconds.\n")


if __name__ == "__main__":
    main()
        

 
    
