#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 19:40:16 2018

@author: laura
"""



import numpy as np
from PIL import Image
import time

def contornoGrad(matriz): 
    n,m=matriz.shape
    fx,fy=0,0
    norma=0
    M=np.zeros((n,m))
    for j in range(m-1):
        for i in range(n-1):
            if (j==0) or (i==0) or (i==(n-1)):
                fy=(matriz[i,j+1]-matriz[i,j])
                fx=(matriz[i+1,j]-matriz[i,j])
            if(j==(m-1)):
                fy=(matriz[i,j]-matriz[i,j-1])
                fx=(matriz[i,j]-matriz[i-1,j])
                
            if (j!=0) and (i!=0) and (i!=(n-1)) and (j!=(m-1)):
                fy=((matriz[i,j+1]-matriz[i,j-1]))
                fx=((matriz[i+1,j]-matriz[i-1,j]))
                
            norma=int((fx**2+fy**2)**(1/2))
            if norma>255:
                norma=255
                
            M[i,j]= norma
    return M
      
                
img = Image.open('belzebu.jpg').convert('L')
img.show()
matriz = np.array(img)
tempoinicio=time.time()
M=contornoGrad(matriz)
print (np.shape(M))
print("segundos",time.time()-tempoinicio)
img2 = Image.fromarray(M).convert('L')
img2.show()

