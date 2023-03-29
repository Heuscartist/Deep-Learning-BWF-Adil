#!/usr/bin/env python
# coding: utf-8

# In[9]:


#BWT-Deep Learning Track
#Task#10 -- Introduction to Numpy
#Adil Mubashir Chaudhry


import numpy as np

# Creating a 1D numpy array
arr1 = np.array([1, 2, 3, 4, 5])
print('One Dimensional Array: ',arr1)
print('1-d array shape: ',arr1.shape)

# Creating a 2D numpy array
arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Two Dimentional Array: \n',arr2) 
print('2-d array shape: ',arr2.shape)

arr3 = arr1.reshape((5, 1))
print('reshaped array: \n', arr3)
print(arr3.shape)


#array with only ones
arr = np.ones((3, 3))
print('array with just ones: \n',arr)

#array with only zeros
arr = np.zeros((3, 3))
print('array with just zeros: \n',arr)

#creating evenly spaced array with 5 spaces between 0 and 1
arr = np.linspace(0, 1, 5)
print('using linspace: ',arr) 

#creating evenly spaced array with spaces between 0 and 4
arr = np.arange(5)
print('using arange: ',arr) 


# In[ ]:




