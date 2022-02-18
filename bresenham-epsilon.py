#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 17:21:52 2019

@author: laura
"""

import numpy as np
from PIL import Image


n=500
M=np.zeros((n,n))

x0=1
xn=100
y0=10
yn=400
M[x0,y0]=255
M[xn,yn]=255
distx=xn-x0
m=(yn-y0)/(xn-x0)
b=y0+m*x0
x=x0
y=int(y0+0.5)
epsilon=y-y0
print (m)
for i in range(distx):
    M[x,y]=255
    if (epsilon+abs(m))<0.5:
        epsilon=epsilon+m
    else:
        y=y+1
        epsilon=epsilon+m-1
    x=x+1
print(M)
import matplotlib.pyplot as plt
plt.matshow(M)
img = Image.fromarray(M).convert('L')
img.show()