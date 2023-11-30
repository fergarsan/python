# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 21:53:15 2023

@author: vayam
"""
            
import pandas as pd
import numpy as np
from sklearn import linear_model

#This function calculates the coefficients of the matrix
# that results from expresing the optimization equations on its matricial form
def statparams(n, data, i):
    meanx = 0
    meany = 0
    d = 0
    c = 0
    for idx in range(0,n):
        meanx = meanx + data[idx][i]
        meany = meany + data[idx][-1] 
        c = data[idx][-1]*data[idx][i]+ c
        d = data[idx][i]**2 + d
        
    meanx = meanx/n
    meany = meany/n
    c = c/n
    d = d/n
     
    return meanx, meany, c, d
        
def invmat(M):
    D = M[0][0]*M[1][1]- M[1][0]*M[0][1]
    #Case for 2x2 matrix:
    return [[M[1][1]/D, -1*M[0][1]/D],[-1*M[1][0]/D, M[0][0]/D]]
    
#This function calculates the product of the reversed matrix of coefficients
#And the array that contains the independent terms of the optimization equations
def prodmat(A,B):
    result = [[0]]*2
    # Iterate through rows of r1
    for z in range(len(B)):
    #Since we are calculating the betas, we are only interested in the first term
        result[0][0]+= A[0][z] * B[z][0]
    return result

#This function obtains the beta asociated to the i column of x values
#it's meant to be iterated
def linearregsim(n, data, i):
    #This line calls the function responsable of the calculation of the 
    #statistical parameters that are part of the matrix of coefficients
    meanx, meany, c, d = statparams(n, data, i)
    M = [[d,  meanx], [meanx, 1]]
    N = [[c], [meany]]
    #Once the matrix of coeficients has been made, it's necessary to reverse it
    Mr = invmat(M)
    #The beta array is the result of the product of the reversed matrix of coefficients and
    # The array that contains the independent terms of the optimization equations
    x_feature = prodmat(Mr, N)
    return x_feature

def linearregmult(data):
    n = len(data)
    ny = len(data[0])
    betas = []
    #Iterating each column of x one by one
    for i in range(0, ny-1):
        x = linearregsim(n, data, i)
    #The results are stockpilled in a beta array
        betas.append(x[0])
    return betas
    
with open("C:\\Users\\vayam\\Desktop\\CX305\\Programación\\Programación\\Python\\test.csv","r") as f: 
    #This part of the code, prepares the data and creates and indexed list with them
    datos = f.read() 
    data = datos.split("\n")
    data = list(map(lambda rowfile: rowfile.split(","), data))
    data = data[1:-1]
    data [0][0] = float(data[0][0])
    data = list(map(lambda ind_rowdata: list(map(lambda ind_coldata: float(ind_coldata), ind_rowdata)), data))
    
    betas = linearregmult(data)

    #Test
    df = pd.read_csv("C:\\Users\\vayam\\Desktop\\CX305\\Programación\\Programación\\Python\\test.csv", sep=",")
    size=df.shape
    x = df.loc[:,df.columns[0:size[1]-1]].values
    y = df.loc[:,df.columns[size[1]-1]].values
    if size[0] > 3:
        lr = linear_model.LinearRegression(normalize = True)
        lr.fit(x, y)
        m = lr.coef_
    else:
        print("Unavailable regression")
        
    # This part of the code evaluates the percentual difference between the betas 
    #obtained with the linearregmult function and the ones obtained using the machine learning 
    #libraries    
    a = np.zeros(len(m))
    size = m.shape[0]
    for i in range(0,size):
        a[i] = abs(100*(m[i] - betas[i])/m[i])
    
    
    
        
        
    