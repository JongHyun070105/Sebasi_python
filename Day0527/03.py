# 리스트는 값 변경 O
li = [1,2,3]
li[0] = "asd"

print(li)

# 튜플은 값 변경 X
t = (1,2,3)
# t[0] = "asd" -> 에러 발생 TypeError: 'tuple' object does not support item assignment
print(t)

tu = ('민수', 18, '서울') #패킹
name, age, city = tu    # 언패킹
print(name, age, city)