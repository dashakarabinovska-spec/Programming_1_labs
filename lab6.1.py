a=input().split()
b=0
for x in a:
    for i in x:
        if i.isupper():
            b+=1
b1=0
for x in a:
    for i in x:
        if i.islower():
            b1+=1
print("UPPER CASE",b)
print("LOWER CASE", b1)
