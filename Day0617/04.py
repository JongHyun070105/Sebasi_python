a,b = map(int, input().split())
c = list(map(int, input().split()))
result = 0

for i in range(a-2):
    for j in range(i + 1, a - 1):
        for k in range(j + 1, a):
            best = c[i] + c[j] + c[k]
            if result< best < b:
                result = best
print(result)