a = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
b=input()
result=0
for i in range(len(b)-1):
    c=a[b[i]]
    next_a=a[b[i+1]]
    if c<next_a:
        result=result-c
    else:
        result=result+c
result=result+a[b[-1]]
print(result)

