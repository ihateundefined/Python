'''
# 두 개의 숫자를 입력받아, 둘 중 큰 숫자를 출력하는 프로그램을 작성하세요.
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

print('큰 수는 >> ',(num1>num2) and num1 or num2)
'''

'''
# 사용자로부터 나이를 입력받아
# 19세 이상이면 "성인", 미만이면 "미성년자"를 출력하세요.
age = int(input("나이를 입력하세요 >> "))

if age >= 19:
    print("성인")
elif age < 19 and age >= 0:
    print("미성년자")
else:
    print("잘못된 입력입니다")
'''

'''
# 사용자로부터 정수를 입력받아, 해당 숫자가 짝수인지 홀수인지를 판별하여 출력
number = int(input("정수를 입력하세요 >> "))
if number % 2 == 0:
    print("짝수입니다.")
elif number % 2 == 1:
    print("홀수입니다.")
else:
    print("잘못된 입력입니다.")
'''

'''
# 사용자로부터 세 개의 숫자를 입력받아, 세 숫자 중 가장 큰 수를 출력하세요.
num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))
num3 = int(input("세 번째 숫자를 입력하세요: "))

print('가장 큰 수는 >> ', max(num1, num2, num3))
'''

'''
# 사용자로부터 시간(시간과 분)을 입력받아
# "새벽", "아침", "오후", "저녁" 중 어느 시간대인지를 출력하세요.
# (5-10 : 아침, 11-15 :  점심, 16-24 : 저녁, 0~4 : 새벽)
hour = int(input("시간을 입력하세요 (0-23): "))
minute = int(input("분을 입력하세요 (0-59): "))

print("입력한 시간은 ", hour, "시", minute, "분입니다.")

if hour >= 5 and hour < 11 and minute >= 0 and minute < 60:
    print("아침입니다.")
elif hour >= 11 and hour < 16 and minute >= 0 and minute < 60:
    print("점심입니다.")
elif hour >= 16 and hour < 24 and minute >= 0 and minute < 60:
    print("저녁입니다.")
elif hour >= 0 and hour < 5 and minute >= 0 and minute < 60:
    print("새벽입니다.")
else:
    print("잘못된 입력입니다.")
'''

'''
# 1부터 100까지의 숫자 중 짝수만 출력하세요.
for i in range(2, 101, 2):
    print(i)
'''

'''
# 1부터 100까지의 숫자 중 3의 배수의 합을 출력하세요.
sum = 0
for i in range(3, 101, 3):
    sum += i
print("1부터 100까지의 숫자 중 3의 배수의 합은 >> ", sum)
'''

'''
# 사용자로부터 시작 숫자와 끝 숫자를 입력받아, 그 사이의 모든 숫자를 출력하세요.
start = int(input("시작 숫자를 입력하세요 >> "))
end = int(input("끝 숫자를 입력하세요 >> "))

print(start, '부터', end, '까지의 숫자 출력하기')
for i in range(start, end + 1):
    print(i, end=' ')
'''