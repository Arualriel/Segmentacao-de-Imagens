#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 29 12:32:52 2018

@author: laura
"""

import numpy as np
from PIL import Image
import time

#
#def fx(a,b):
#
#def fy(a,b):
#
#def E(matriz):
#    
#def F(matriz):
#    
#def G(matriz):
##########cpnsiderando g(x,y)=(x,y,f(x,y))
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
                fy=((matriz[i,j+1]-matriz[i,j-1])/2)
                fx=((matriz[i+1,j]-matriz[i-1,j])/2)
            ro=EFG(fx,fy)    

            M[i,j]=ro
    return M
      
nome='circulo.png'          
img = Image.open(nome).convert('L')
img.show()
matriz = np.array(img)
tempoinicio=time.time()
M=contorno(matriz)
print("segundos",time.time()-tempoinicio)
img2 = Image.fromarray(M).convert('L')

img2.save("miniatura_"+nome)
img2.show()