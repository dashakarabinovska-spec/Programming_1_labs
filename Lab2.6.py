n=int(input())
a=n//100
b=n//10%10
c=n%10
max = max(a,b,c)
min= min(a,b,c)
if a==b==c:
    print (a)
else:
    print(max, min)
