'''
# 리스트이름 = [값1, 값2, 값3, ...]
ktx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#sum = ktx[0] + ktx[1] + ktx[2] + ktx[3] + ktx[4] + ktx[5] + ktx[6] + ktx[7] + ktx[8] + ktx[9]

sum = 0
for i in range(10):
    sum += ktx[i]

print(sum)
'''

'''
# append() : 리스트에 값을 추가하는 함수 ... C++의 push_back()과 비슷
sum = 0
ktx = [] # 빈 리스트 생성

ktx.append(1)
ktx.append(2)
ktx.append(3)
ktx.append(4)
ktx.append(5)
'''

'''
# for문 활용
sum = 0
ktx = [] # 빈 리스트 생성

for i in range(5):
    ktx.append(i + 1)

for i in range(5):
    sum += ktx[i]
print(sum)
'''

'''
# 리스트는 자료형이 다를 수 있다.
ktx = []
ktx = [1, 2, 3, 4, 5]
ktx = [3.14, 1.59, 2.65, 3.58]
ktx = [1, 2, 3.14, 'hello', True]
ktx = [1, 2, 'hi', 'hello', 5]
'''

'''
# 리스트의 접근 범위 지정
# 리스트의 이름[시작인덱스:끝인덱스+1]
ktx = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ktx[0:5]) # 리턴 타입은 리스트
print(ktx[2:6]) # [3, 4, 5, 6]
print(ktx[:3])
print(ktx[3:])
print(ktx[:])
'''

'''
# 리스트 연산
# 리스트 + 리스트 : 두 리스트를 합친다.
# 리스트 * 정수 : 리스트를 정수만큼 반복한다.
ktx = [10, 20, 30]
tgv = [40, 50, 60]
print(ktx + tgv) # [10, 20, 30, 40, 50, 60]
print(ktx * 3) # [10, 20, 30, 10, 20, 30, 10, 20, 30]

ktx[0] = 100
print(ktx) # [100, 20, 30]

del ktx[1]
print(ktx) # [100, 30]

ktx[1:4] = []
print(ktx) # [100]
'''

'''
# 리스트 제공 함수
ktx = [100, 20, 30]

ktx.append(200)
print(ktx) # [100, 20, 30, 200]

ktx.sort()
print(ktx)

ktx.insert(1, 'happy :)')
print(ktx) # [100, 'happy :)', 20, 30, 200]
'''