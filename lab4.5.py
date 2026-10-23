n = input()
k, m = map(int, input().split())
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
          'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
          'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
          'U', 'V', 'W', 'X', 'Y', 'Z']
sign = ''
if n[0] == '-':
    sign = '-'
    n = n[1:]
num = int(n, k)
result = ''
if num == 0:
    result = '0'
while num > 0:
    r = num % m
    result = digits[r] + result
    num = num // m
print(sign + result)
