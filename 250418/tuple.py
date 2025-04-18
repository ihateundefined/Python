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