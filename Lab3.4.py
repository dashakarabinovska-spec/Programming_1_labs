n=int(input())

for i in range (100,1000):
    n3 = i % 10
    n2 = i // 10 % 10
    n1 = i // 100 % 10
    if  n1+n2+n3==n:
         print(i)
