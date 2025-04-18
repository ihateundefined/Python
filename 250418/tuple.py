'''
# 튜플 -> 읽기 전용 데이터 구조
# 튜플은 리스트와 비슷하지만, 수정이 불가능한 데이터 구조
tp1 = (1, 2, 3, 4, 5)
tp2 = 1, 2, 3, 4, 5

print(tp1)
print(tp2)

tp3 = (10,)
tp4 = (10) # 튜플이 아니다.
tp5 = 10,

print(tp3) # (10,)
print(tp4) # 10
print(tp5) # (10,)

# tp1.append(6) # AttributeError: 'tuple' object has no attribute 'append'

# 연산은 가능하나 값 자체 수정은 불가능하다.
sum = tp1[0] + tp1[1] + tp1[2] + tp1[3] + tp1[4]
print(sum)

print(tp1[1:3]) # (2, 3)
print(tp1[1:]) # (2, 3, 4, 5)
print(tp1[:3]) # (1, 2, 3)

print(tp1 + tp2)
print(tp1 * 3) # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
'''

'''
# 튜플을 리스트로 변환하여 수정 후 다시 튜플로 변환
# 튜플은 수정이 불가능하므로, 리스트로 변환 후 수정해야 한다.
mytp = ('나혼자', '파이썬')
print(mytp)

#mytp[0] = '다함께' # TypeError: 'tuple' object does not support item assignment

myList = list(mytp) # 튜플을 리스트로 변환
myList[0] = '다함께'
mytp = tuple(myList) # 리스트를 튜플로 변환
print(mytp)
'''