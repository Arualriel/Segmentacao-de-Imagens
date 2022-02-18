#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 16:46:00 2019

@author: laura
"""

import numpy as np
from PIL import Image


n=500
M=np.zeros((n,n))

x0=1
xn=50
y0=1
yn=100
M[x0,y0]=255
M[xn,yn]=255
distx=xn-x0
m=(yn-y0)/(xn-x0)

#se m >1 x em funcao de y
if m<=1:
    print('oi1')
    b=y0+m*x0
    x=x0
    for i in range(distx):
        y=int(m*x+b)
        M[x,y]=255
        
        x=x+1
else:
    print('oi2')
    disty=yn-y0
    #m=(xn-x0)/(yn-y0)
    b=x0+m*y0
    y=y0
    for i in range(disty):
        x=int(m*y+b)
        M[x,y]=255
        
        y=y+1
    
import matplotlib.pyplot as plt
plt.matshow(M)
img = Image.fromarray(M).convert('L')
img.show()
    