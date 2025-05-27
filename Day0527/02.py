li = []
print(list("Happy"))

li2 = [1,2]
li2.append(3) # 리스트에 값 추가
li2.append([4,5])
print(li2)

li3 = [1,2,3,4,5]
print(li3[3]) # 원하는 인덱스 값 출력

li3.insert(2, 9) # 원하는 위치에 값 삽입
print(li3)

li4 = [1,2,3,4,5]
del li4[3] # 원하는 인덱스 삭제
print(li4)

li4.remove(3) #원하는 값 삭제
print(li4)

li5 = [1,2,3,4,5]
li5.pop(2) # 원하는 값 삭제
# li5.clear() -> 리스트 값 전부 삭제
print(li5)

li6 = [1,2,3,4,5]
print(len(li6)) # 리스트 길이 확인