# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:19:01 2022

@author: Lenovo
"""

import pandas as pd
import numpy as np 
# read by default 1st sheet of an excel file
df = pd.read_excel("C:/Users/Tarun Yadav/Documents/CE331/Lab/traverse.xlsx")
df = df.dropna()

# Design Matrix A
A1 = df.loc[:, ('Northing(L)', 'Easting(L)')]
A1["one"] = 1
A1["zero"] = 0

A2 = df.loc[:, ('Northing(L)', 'Easting(L)')]
A2["Easting(L)"] = -A2["Easting(L)"]
A2["zero"] = 0
A2["one"] = 1

A1 = A1.to_numpy()
A2 = A2.to_numpy()
# print(A1)
# print(A2)
A = np.concatenate((A1, A2), axis=0)

# ##Global Measurement
L1 = df["Northing(G)"].to_numpy()
L2 = df["Easting(G)"].to_numpy()
L = np.concatenate((L1, L2), axis=0)
# print(L1)
# print(L2)
# Estimate(A,B,TN,TE)
X1 = np.linalg.inv(np.dot(A.T, A))
X2 = np.dot(A.T, L)
X = np.dot(X1, X2)

print(X)
