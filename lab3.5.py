n = int(input())
max_a= 0
min_a=9
while n >0 :
    a=n%10

    if a > max_a:
        max_a=a
    if a <min_a :
        min_a=a
    n=n//10

ruznitsa= max_a - min_a
if ruznitsa%2==0:
    print("true")
else :
    print("false")



