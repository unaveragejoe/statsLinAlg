#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import math

class statsLinAlg():
    def __init__(self):
        pass
    def dot(self, vec1, vec2):
        result = 0
        for i,j in zip(vec1, vec2):
            result += i*j
            
        return result
    
    def mean(self, vec):
        total = 0
        vec_len = len(vec)
        
        for ele in vec:
            total += ele
        
        return total / vec_len
        
    def var(self, vec):
        try:
            some_object_iterator = iter(vec)
        except TypeError as te:
            print(vec, "Please input a non-string iterable")
            
        len_vector = len(vec)
        
        vec_mean_subtracted = [val - self.mean(vec) for val in vec]
    
        return self.dot(vec_mean_subtracted, vec_mean_subtracted) / (len_vector-1)
        
    def cov(self, vec1, vec2):
        if (type(vec1) not in [list, type(np.array([]))]) or (type(vec2) not in [list, type(np.array([]))]):
            return "One of your vectors is not a python list or a numpy array!"
        if len(vec1) != len(vec2):
            return "Vectors must be the same length!"

        len_vector = len(vec1)

        vec1_mean_subtracted = [val - self.mean(vec1) for val in vec1]
        vec2_mean_subtracted = [val - self.mean(vec2) for val in vec2]
        
        return self.dot(vec1_mean_subtracted, vec2_mean_subtracted) / (len_vector-1)

    def pearsonr(self, vec1, vec2):
        if (type(vec1) not in [list, type(np.array([]))]) or (type(vec2) not in [list, type(np.array([]))]):
            return "One of your vectors is not a python list or a numpy array!"
        if len(vec1) != len(vec2):
            return "Vectors must be the same length!"

        len_vector = len(vec1)

        vec1_mean_subtracted = [val - self.mean(vec1) for val in vec1]
        vec2_mean_subtracted = [val - self.mean(vec2) for val in vec2]
        
        vec1_std = math.sqrt(self.var(vec1))
        vec2_std = math.sqrt(self.var(vec2))
        
        return self.dot(vec1_mean_subtracted, vec2_mean_subtracted) / (vec1_std * vec2_std * (len_vector-1))
    
    def covMatrix(self, list_of_lists):
        result = []
        for i in list_of_lists:
            inner_result = []
            result.append(inner_result)
            for j in list_of_lists:
                inner_result.append(self.cov(i,j))
        return np.array(result)
    
    def corrMatrix(self, list_of_lists):
        result = []
        for i in list_of_lists:
            inner_result = []
            result.append(inner_result)
            for j in list_of_lists:
                inner_result.append(self.pearsonr(i,j))
                
        return np.array(result)
    
    def T(self, mat):
        result = []
        for i in range(mat.shape[1]):
            end = mat.shape[1]+1
            t_result = mat[0:end+1,i:i+1].flatten()
            result.append(list(t_result))
            
        return np.array(result)

    def matMul(self, m1, m2):
        # (i,j)th entry is dot product between ith row and jth column
        # Transpose the second matrix and then take the dot product of each inner list

        if m1.shape[1] != m2.shape[0]:
            return "Inner dimensions do not match!"
        print(f"The resulting matrix will be {m1.shape[0]} x {m2.shape[1]}")
        
        result = []
        for row1 in m1:
            inner = []
            for row2 in self.T(m2):
                row_mult_col = self.dot(row1, row2)
                inner.append(row_mult_col)
            result.append(inner)
            
        return np.array(result)

# Move input checks into its own function that runs at the start of each other method
# Add a method for matrix inverse
# Add a method for determinant
# Add a method for a diagonalization
# Add a method for eigendecomposition, output evec and evals/principal components
# BONUS: account for nonsquare matrices

