#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Qquestion b-i( for the age)

import statistics
import math

def var(list):
    list_mean = statistics.mean(list)
    var_sum = 0
    for element in list:
        var_sum = var_sum + (element - list_mean)**2
        
    variance = var_sum / (len(list)-1)
    std_dev = variance**(1/2)
    return variance, std_dev

age = [61, 60, 60, 60, 60, 59, 59, 59, 59, 59]

var,std = var(age)

print(var,std)
 


# In[3]:


#Qquestion b-i( for the height)

import statistics
import math

def var(list):
    list_mean = statistics.mean(list)
    var_sum = 0
    for element in list:
        var_sum = var_sum + (element - list_mean)**2
        
    variance = var_sum / (len(list)-1)
    std_dev = variance**(1/2)
    return variance, std_dev

height = [1.85, 1.71, 1.55, 1.46, 1.58, 1.71, 1.70, 1.72, 1.46, 1.83]

var,std = var(height)

print(var,std)


# In[5]:


#Question b-ii

import itertools

Age = [61, 60, 60, 60, 60, 59, 59, 59, 59, 59]
Height = [1.85, 1.71, 1.55, 1.46, 1.58, 1.71, 1.70, 1.72, 1.46, 1.83]

for a, b in zip(Age, Height):
    print(a, b)


# In[6]:


import itertools
import statistics

def cov_lists(listx, listy):
    meanx = statistics.mean(listx)
    meany = statistics.mean(listy)

    sumxy = 0
    for elex, eley in zip(listx, listy):
        sumxy = sumxy + (elex - meanx) * (eley - meany)

    covariance = sumxy / (len(listx)-1)
    return covariance


# In[7]:


Age = [61, 60, 60, 60, 60, 59, 59, 59, 59, 59]
Height = [1.85, 1.71, 1.55, 1.46, 1.58, 1.71, 1.70, 1.72, 1.46, 1.83]

cov = cov_lists(Age, Height)

print(cov)


# In[ ]:




