import math
import numpy as np
import sys


#with open(r"fort.401",'r') as f:
#with open(r"fort.111",'r') as f:
with open(r"fort.101",'r') as f:
    k=f.readlines()
    arr=[]
    for x in range(0,len(k),2):
        temp=k[x].split()
        arr.append([float(y) for y in temp[:7]])
    data=np.array(arr[:])

f.close

count=0
block=12
a=len(data)
c=int(a/block)
col=1
print a,c

xx=[]
for i in range[:c]:
    for j in data[i:i+6:c]:
        xx.append(j)
ff=open('lol.txt','w')
for i in xx[0,:]:
    print >> ff, xx[i]
ff.close  


print "#No of blocks", block, "Coloumn No", col+1
"""
k=[]
k1=[]
for i in data[0:]:
    k.append(str(i[col]))
k1=np.array(k,float)
j1=sum(k1)/float(len(k1))
print count, k1.mean(), k1.var() 

"""
"""
sum1=float(0)
d=[]
for j in range(block):
  count=count+1
  b=[]
  t=np.array(data[col])
   
  for i in data[j*c:(j+1)*c]:
      b.append(str(i[col]))
  d=np.array(b,float)
  t1=sum(d)/float(len(d))
  sum1 =sum1+(t1*t1-j1*j1)
  print count, d.mean(), d.var()
del b
b=[]  
for i in data[block*c:]:
      b.append(str(i[col]))
d=np.array(b,float)
"""
