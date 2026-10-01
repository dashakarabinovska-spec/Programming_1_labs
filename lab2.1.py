import math

r=float(input())
a=float(input())

S1=math.pi * r ** 2
S2=a*a
if S1 > S2:
    print ("circle")
if S2 > S1:
    print ('square')
