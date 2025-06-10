# 수를 입력받아서 입력받은 수까지 별찍기
a = int(input())

for i in range(a):
    for k in range(i + 1):
        print("*", end="")
    print()