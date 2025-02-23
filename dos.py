# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys
import os
import math
import string
import glob
import numpy as np
from scipy import interpolate
#os.system('cp dos.dat dos_original.dat')
#os.system('sed "1d" dos_original.dat > dos.dat')
f=open('dos.dat','r')
a=f.readlines()
f.close

c=[]
c2=[]

for i in range(1,len(a)):
    x=a[i].split()
#    b.append(x[0:2])
    c.append(x[1])
    c2.append(x[0])
    del x
del a

d=np.sign(np.gradient(np.array(c,float)))

e=[]

for i in range(len(d)-1):
    if d[i+1] == float(-1) and d[i] == float(1.0):
         e.append(i)  
del d
f=[]
f1=[]

for i in e:
    for j in range(0,i):
        l = float(c[j]) - (float(c[i]) /float(2))
        if l <= float(0.001):
           m = float(c2[j])
        n=m
    f.append(n) 

#for i in e:
    for j in range(len(c2)-1,i,-1):
        l = float(c[j]) - (float(c[i]) /float(2))
        if l <= float(0.001):
           m = float(c2[j])
        n=m
    f1.append(n)
#print(c2[933],c[933])
