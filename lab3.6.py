n=int(input())
for i in range(1,n+1):
    original=i
    reverse=0

    while i>0:
       digit=i%10
       reverse=reverse*10+ digit
       i=i//10
    if original==reverse:
       print(original)

