# 수를 입력받아서 입력받은 수까지 역순으로 별찍기
a = int(input())

for i in range(a, 0, -1):
    print("*" * i)
print()
