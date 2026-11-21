numbers = input().split()
seen = set()
repeated = set()
for n in numbers:
    if n in seen:
        repeated.add(n)
    else:
        seen.add(n)
print(*repeated)
