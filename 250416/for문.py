'''
# 기본 for문
for num in range (0, 5, 1):
    print(num, 'hi there :)')
'''

''' 
# for문을 이용한 합계
sum = 0
for number in range (1, 6, 1):
    sum += number
    print(sum)
'''

'''
# 365까지 합 구하기
sum = 0
for days in range (1, 366, 1):
    sum += days
print("1부터", days, "까지의 합은", sum, "입니다.")
'''

'''
# 1부터 100까지 짝수의 합 구하기
sum = 0
for evenNum in range (0, 101, 2):
    sum += evenNum
print("1부터", evenNum, "까지의 짝수의 합은", sum, "입니다.")
'''

'''
# 내가 좋아하는 숫자 맞추기
favoriteNum = int(input("내가 좋아하는 숫자는? >> "))
start = int(input("시작 숫자 >> "))
end = int(input("끝 숫자 >> "))

for i in range (start, end + 1, 1):
    if i == favoriteNum:
        print("정답입니다.")
        break
    else:
        print("못찾았습니다.")
'''

'''
# 구구단 2단 출력
for val in range (1, 10 ,1):
    print('2 * %d = %d' % (val, 2 * val))
'''

'''
dan = int(input("구구단 몇 단? >> "))
for val in range (1, 10 ,1):
    print('%d * %d = %d' % (dan, val, dan * val))
'''

'''
# 구구단 2단부터 9단까지 출력
print("구구단 시작")
for dan in range (2, 10, 1):
    print("구구단 %d단" % (dan))
    for val in range (1, 10 ,1):
        print('%d * %d = %d' % (dan, val, dan * val))
    print('*******************')
print("구구단 끝")
'''

# *로 직각삼각형 만들기
for i in range (1, 6, 1):
    for j in range (1, i + 1, 1):
        print("*", end='')
    print()
print("직각삼각형 끝")