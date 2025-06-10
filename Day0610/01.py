# 5보다 작은 1 2 3 4 가 출력되게 하는 알고리즘

a, b = map(int,input().split())
li = list(map(int,input().split()))

for i in range(len(li)):
    if(li[i] < b):
        print(li[i], end=" ")