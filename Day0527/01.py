# 8을 입력 받아 1~8 곱한 값 출력

a = int(input())

result = 1

for i in range(2, a + 1):
    result *= i

print(result)