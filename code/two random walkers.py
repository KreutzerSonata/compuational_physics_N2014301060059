# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 21:25:31 2016

@author: lenovo
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import math
def randpath(tt):
    b=[]
    bb=[]
    b.append(0)
    bb.append(0)
    b2=[]
    for i in range(tt):
        c=random.random()
        bb.append(i+1)
        b.append(b[-1]-1+2*c)
    for j in range(len(b)):
        b2.append(b[j])
    return b,bb,b2

a,b,c=randpath(1000)
a1,b1,c1=randpath(1000)
for k in range(len(b)):
    plt.scatter([b[k],],[c[k],], 7, color ='red')
    plt.scatter([b1[k],],[c1[k],], 7, color ='blue')
plt.xlim(0,1000)
plt.grid(True)
plt.xlabel('time/step number')
plt.ylabel('X')
plt.title('random walk in one dimesion')
plt.show()