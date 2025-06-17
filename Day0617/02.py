a = list(map(int, input().split()))

if a == sorted(a):
    print("a")
elif a == sorted(a, reverse=True):
    print("b")
else :
    print("c")
