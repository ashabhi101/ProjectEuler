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

  # Question 4
# Palindrome Number
  
def get_digit(number,n):
    return number//10**n%10
plist = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        if len(str(i*j)) ==6:
            if get_digit(i*j,0) == get_digit(i*j,5) and get_digit(i*j,1) == get_digit(i*j,4) and get_digit(i*j,2) == get_digit(i*j,3):
                plist.append(i*j)
    print((sorted(plist)))

 # Question 5
# Smallest multiple
from functools import reduce
from fractions import gcd
def lcm(a,b):
    return a*b//gcd(a,b)
def lcms(*numbers):
    return reduce(lcm,numbers)

def smallestmultiple(n):
    smallnumber = 1
    for i in range(1,n+1):
        smallnumber = lcms(smallnumber,i)
    return smallnumber
        
smallestmultiple(20) 

# Question 6
# Square sum difference

def squaresum(n):
    sumsquare = 0
    squaresum = 0
    for i in range(1,n+1):
        sumsquare = sumsquare+i**2
        squaresum = (squaresum+i)
    return (squaresum**2-sumsquare)
 
squaresum(100)

# Question 6
# Prime NUmber

def primenumber(n):
    primes = [2]
    for i in range(3, 10000000000000,2):
        for j in range(3, math.sqrt(i)):
            if i%j==0

# Question 7
            
            
            
            
            
            
            
            
            
            
            
            


# Question 8
# Largest product in a series
import re
number = (7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450)
def get_digit(number,n):
    return number//10**n%10
numberlist = []
len(str(number))
for i in range(1000):
    numberlist.append(get_digit(number,i))

numberlist = list(reversed(numberlist))
numberlist[0:10]

from functools import reduce
import operator
def prod(iterable):
    return reduce(operator.mul, iterable,1)
multiply =[]
for i in range(0,997,1):
    local=[]
    local = numberlist[i:i+13]
    multiply.append(prod(local))

multiply = sorted(multiply)
print(multiply[-1])6

# Question 9
# Pythogous Theorem

import itertools
for i in range(1,499):
    for j in range(1,500):
        for k in range(1,500):
            if i**2 + j**2 == k**2 and i+j+k ==1000:
                print(i*j*k)
                # or if you want to use a single for statement to iterate:
for i,j,k in itertools.product(range(1,500), range(1,500), range(1,500)):
    if i**2 + j**2 == k**2 and i+j+k ==1000:
        print(i*j*k)
        
# Question 10


def sum_primes(n):
    primes = [2]
    attempt = 3
    sum=2
    while attempt in range(3,n):
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
            sum+=attempt
        attempt += 2
    return sum

sum_primes(2000000)

# Problem 12
# divisors list
        
for i in range(62370000,76576550):
    sum.append(sum[-1] + i)
sum
factorlist=[]
def factors():
    for i in sum:
        templist =[i]
        for j in range(1,int(i**0.5)+1):
            if i%j == 0:
                templist.append(j)
                if j != i/j:
                    templist.append(i/j)
        factorlist.append(templist)
    elem = []
    for list in factorlist:
        elem.append(len(list))
    return elem
x =[]   
x = (factors())
type(x)
if any( num >= 499 for num in x):
    print(True)
else:
    print("Nope")

       
       
    
    
