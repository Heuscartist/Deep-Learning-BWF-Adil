#!/usr/bin/env python
# coding: utf-8

# In[10]:


#BWT - Deep Learning Track
#Task#11 -- Linear Algebra and Statistical Functions using numpy
#Adil Mubashir Chaudhry

import numpy as np


#Linear Algebra using numpy
arr = np.random.randint(1,10,9)
arr = arr.reshape(3,3)

arr2 = np.random.randint(11,20,9)
arr2 = arr.reshape(3,3)

dot = np.dot(arr, arr2)
print('dot product of 2 arrays: \n', dot)


rank = np.linalg.matrix_rank(arr)
print('\nRank of the Matrix: ', rank)

det = np.linalg.det(arr)
print('\nDeterminent of Matrix: ', det)

print('\noriginal arr: \n', arr)
inverse_arr = np.linalg.inv(arr)
print('\ninverse of arr: \n', inverse_arr)



#statistical functions using numpy
arr_mean = np.mean(arr)
print('\nmean of array: ', arr_mean)

arr_std = np.std(arr)
print('\nstandard deviation of array: ', arr_std)

arr_var = np.var(arr)
print('\nvariance of array: ', arr_var)

arr_max  = np.max(arr)
print('\nmaximum of array: ', arr_max)

arr_min  = np.min(arr)
print('\nminimum of array: ', arr_min)


# In[ ]:




