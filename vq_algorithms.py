#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 11:55:15 2018

Name: khalednakhleh
"""
import numpy as np
from scipy.stats import norm
from scipy import integrate


class Lloyd_max(object):
    
    # Initalizing
    def __init__(self, m, x, iterations):
            
        self.m = m
        self.x = x
        self.iterations = iterations
        self.centroids, self.intervals = Lloyd_max.algorithm(self, x)      
            
    def algorithm(self, x):
        
        # Setting some initial values to be updated
        self.centroids = np.zeros(self.m - 1)
        self.intervals = np.linspace(np.min(self.x) - 1, np.max(self.x) + 1, self.m)
        
        print("\nInitial interval values: \n\n" + str(self.intervals))
        
        # Counter
        v = 0
        
        # Iterating the Lloyd max algorithm for "iterations" number of times
        while v < self.iterations:
            
            i = 0
            
            # Calculating centroids' values for the "v" iteration
            while i < self.centroids.shape[0]:
                
                n_1 =  integrate.quad(lambda x: x * norm.pdf(x), self.intervals[i], self.intervals[i + 1])[0]
                n_2 =  integrate.quad(lambda x: norm.pdf(x), self.intervals[i], self.intervals[i + 1])[0]              
                    
                self.centroids[i] = n_1/n_2           
                i = i + 1
                          
            q = 0
            
            # Calculating intervals' values for the "v" iteration
            while q < self.centroids.shape[0] - 1:
        
                self.intervals[q + 1] = (self.centroids[q] + self.centroids[q + 1]) / 2
                    
                q = q + 1
            
            v = v + 1
        
        # Appending and returning final results
        return self.centroids, self.intervals


class LBG(object):
    
    def __init__(self, dim, x, m):
        self.x = x
        self.dim = dim
        self.m = m


    def distortion(self):
        
        """ squared error distortion """
        








if __name__ == "__main__":
    
    print("\n\nPlease access this file by using lloyd_max.py file.")
    exit
