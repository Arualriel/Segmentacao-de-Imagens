#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  9 11:50:58 2019

@author: laura
"""



import numpy as np
from PIL import Image
import time

def EFG(fx,fy):
    traco,det,E,F,G=0,0,0,0,0
    l1,l2,maximo=0,0,0
    E=(1+fx**2)
    F=(fx*fy)
    G=(1+fy**2)
    traco=E+G
    det=E*G-F**2
    delta=(traco**2-4*det)
    l1=(traco+(delta)**(1/2))/2
    l2=(traco-(delta)**(1/2))/2
    if abs(l1)>=abs(l2):
        maximo=int(abs(l1))
    else:
        maximo=int(abs(l2))
    if maximo>255:
        maximo=255
    
    return maximo


def contorno(matriz): 
    n,m=matriz.shape
    fx,fy,ro=0,0,0

    M=np.empty((n,m))
    for i in range(n-1):
        for j in range(m-1):
            if (j==0) or (i==0) or (i==(n-1)):
                fy=(matriz[i,j+1]-matriz[i,j])
                fx=(matriz[i+1,j]-matriz[i,j])
            if(j==(m-1)):
                fy=(matriz[i,j]-matriz[i,j-1])
                fx=(matriz[i,j]-matriz[i-1,j])
                
            if (j!=0) and (i!=0) and (i!=(n-1)) and (j!=(m-1)):
                fy=((matriz[i,j+1]-matriz[i,j-1]))
                fx=((matriz[i+1,j]-matriz[i-1,j]))
            ro=EFG(fx,fy)    

            M[i,j]=ro
    return M

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
 

def contornolap(matriz): 
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
                fy=((matriz[i,j+1]-2*matriz[i,j]+matriz[i,j-1])/2)
                fx=((matriz[i+1,j]-2*matriz[i,j]+matriz[i,j-1])/2)
                
            norma=int(abs(fx+fy))
            if norma>255:
                norma=255
                
            M[i,j]= norma
    return M
      
                
img = Image.open('belzebu.jpeg').convert('L')
img.show()
matriz = np.array(img)
tempoinicio=time.time()
M=contornolap(matriz)
print (np.shape(M))
print("segundos",time.time()-tempoinicio)
img2 = Image.fromarray(M).convert('L')
img2.show()

M=contornoGrad(matriz)
img3 = Image.fromarray(M).convert('L')
img3.show()

M=contorno(matriz)
img4 = Image.fromarray(M).convert('L')
img4.show()

