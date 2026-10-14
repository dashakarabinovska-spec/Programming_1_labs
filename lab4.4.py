a=list(map(int,input().split()))
b=int(input())
c=int(input())
if b in a:
  for i in range(len(a)):
    if a[i]==b:
        a[i]=c
  print (a)
else:
    print (' is impossible')
