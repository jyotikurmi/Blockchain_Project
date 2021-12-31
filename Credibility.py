import math
import pandas as pd
import numpy as np
#import pymc3 as pm 
import hashlib
import random 
from functools import reduce


D=[]
def credibility(b,g ,mes,eve,idx):
   C=[]
   #for i in range(0,1):
       #x =[12 ,4]
       #y=np.random.uniform(low=10.5, high=100, size=(2,))
       # y=[int(y) for y in input().split()]
   
       # x = [int(x) for x in input().split()]
   point1 = np.array((19 ,17 ))
   point2 = np.random.uniform(low=10, high=15, size=(2,))
  
         # calculating Euclidean distance
          # using linalg.norm()
   djk = np.linalg.norm(point1 - point2)
   D.append(djk)
    
   #djk= math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
   print(f"distance between event\t{eve} and sender  \t{idx+1} =",djk) 
    
   
 
   if reporter==0:
      cj=0
      C.append(cj)
      print(cj)
   else:
    cj=b+eve**(-g*djk)
    C.append(cj)
    return cj
    print(C)
r=[]   
b=0
g=1
l=[]
msg=[]
#k=[int(x) for x in input().split()]
#e=np.random.uniform(low=1, high=10, size=(5,))
e=[1]
reporter=int(input("number of reporter\t"))

for i in range(reporter):
  
  message=input("enter the message\t")
 

  if message=="yes":
     #msg1=hashlib.sha256(message.encode()).hexdigest()
     msg.append(message)
  elif message=="no":
     #msg1=hashlib.sha256(message.encode()).hexdigest()
     msg.append(message)
  else:
    pass
print("total number of messages from the reporters",msg)

#ms=[]

for eve in e:
 for idx ,mes in enumerate(msg): 

   a=credibility(b,g,mes,eve,idx)
   
   l.append(a)
  
   if 0<a==1:
     r.append(a)
     #ms.append(mes)
print("credibility",l)
#print(l)

#print(r)
if r==[]:
  print("no messages")
else:
  v=int((reduce(max, r)))
  D.sort()
  if v==1:
    if D[-1]:
     
     ms=mes
     R=idx+1
     j=int(v)
     print ("max credibility=",j)
     print ("message=>",ms)
