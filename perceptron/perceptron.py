#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:11:36 2023

@author: kbalazs
"""

class Perceptron:
    def __init__(self, num_inputs=2, weights=[2,1]):
        self.num_inputs = num_inputs
        self.weights = weights
    
    #method for weighted_sum
    def weigthed_sum(self, inputs):
        #create variable to store weighted sum
        weigthed_sum = 0
        for i in range(self.num_inputs):
            weigthed_sum += self.weights[i] * inputs[i]
            
        return weigthed_sum
    
    #method for activation funciton
    def activation(self, weighted_sum):
        if weighted_sum >= 0:
            return 1
        else:
            return -1

# Creating the first instance of the Perceptron class (object)
cool_perceptron = Perceptron()
print(cool_perceptron.weigthed_sum([24, 55]))
print(cool_perceptron.activation(103))
        