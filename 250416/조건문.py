'''
# 조건문
a = 11

if a > 10:
    print('a는 10보다 큽니다.')
elif a == 10:
    print('a는 10입니다.')
else:
    print('a는 10보다 작습니다.')
print('프로그램 종료')
'''

'''
# if 문의 중첩
id = 'charlie'
password = '1234'
userId = input('아이디를 입력하세요 >> ')
userPassword = input('비밀번호 입력하세요 >> ')

if id == userId:
    if password == userPassword:
        print('로그인 성공!!')
    else:
        print('비밀번호가 틀렸습니다.')
else:
    print('아이디가 틀렸습니다.')
'''

'''
# elif 문을 사용한 중첩
subject = input('좋아하는 과목 입력하기 >> ')

if subject == 'python':
    print('당신은 파이썬을 좋아하는군요!')
elif subject == 'java':
    print('당신은 자바를 좋아하는군요!')
elif subject == 'c':
    print('당신은 C를 좋아하는군요!')
else:
    print("파이썬, 자바, C는 당신의 선호도에서 벗어나는군요?")
'''

'''
# 단축키 예제
shortCut = int(input('단축키를 입력하세요 >> '))

if shortCut == 1:
    print('엄마에게 전화 걸기')
elif shortCut == 2:
    print('아빠에게 전화 걸기')
elif shortCut == 3:
    print('여자친구에게 전화 걸기')
else:
    print('해당 단축키 없음')
'''

'''
# 입력한 월에 해당하는 계절 출력
month = int(input('몇 월의 계절이 궁금하신가요? >> '))

if month == 1 or month == 2 or month == 12:
    print('겨울입니다.')
elif month > 2 and  month < 6:
    print('봄입니다.')
elif month > 5 and month < 9:
    print('여름입니다.')
elif month > 8 and month < 12:
    print('가을입니다.')
else:
    print('잘못된 입력입니다.')
'''

'''
# 점수 > 학점 변환기
score = int(input('당신의 점수를 입력하세요 >> '))

if score >= 90 and score <= 100:
    print('A 학점')
elif score >= 80:
    print('B 학점')
elif score >= 70:
    print('C 학점')
elif score >= 60:
    print('D 학점')
elif score >= 0 and score < 60:
    print('F 학점')
else:
    print('입력값이 잘못되었니다')
'''

'''
# 자판기 예제
print('********* 자판기의 메뉴 ***********')
print('1. 사이다 1000원')
print('2. 콜라 1200원')
print('3. 환타 1100원')
print('4. 물 800원')
print('***********************************')

sprite = 1000
coke = 1200
fanta = 1100
water = 800

money = int(input('돈을 넣어주세요 >> '))
if money >= coke:
    print('모든 메뉴 구매 가능')
elif money >= fanta:
    print('사이다, 물, 환타 구매 가능')
elif money >= sprite:
    print('사이다, 물 구매 가능')
elif money >= water:
    print('물 구매 가능')
else:
    print('구매 불가능')
    print('돈을 더 넣어주세요')
'''

'''
# 나이 예제
age = int(input('당신의 나이를 입력하세요 >> '))

if age >= 19:
    pass
else:
    print("신분증 보여주세요~")
'''