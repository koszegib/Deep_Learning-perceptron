#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 18:11:36 2023

@author: kbalazs
"""

class Perceptron:
    def __init__(self, num_inputs=2, weights=[1,1]):
        self.num_inputs = num_inputs
        self.weights = weights

# Creating the first instance of the Perceptron class (object)
cool_perceptron = Perceptron()
print(cool_perceptron)
        