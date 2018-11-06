# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 19:24:41 2018

@author: HP
"""
import math


# Question 1

# Multiples of 3 or 5
x=[]
for i in range(1000):
    if i%3==0 or i%5==0:
        x.append(i)
print(sum(x))

# Question 2
# Even Fibonacci Numbers
def fibonacci(y):
    import numpy as np
    flist = [1,2]
    sum = 2
    p = np.log(y*(np.sqrt(5)))/np.log(0.5*(1+np.sqrt(5)))
    for i in range(2,int(p)):
            if flist[i-2] < y:
                flist.append(flist[i-1]+flist[i-2])
            if (flist[i])%2 == 0:
                sum+= flist[i]
    return sum
fibonacci(4000000)

# Question 3
# Prime factors
def primefactors(n):
    flist=[]
    import math
    if n%2 ==0:
        n = n/2
        flist.append(2)
    for i in range(3,int(math.sqrt(n))+1,2):
        if n%i == 0:
            flist.append(i)
            n = n/i
    print(flist)
    
primefactors(600851475143)         
       
       
    
    