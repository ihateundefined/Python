'''
# 사칙연산
def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("0으로 나눌 수 없습니다.")
        return 'invalid'
    return a / b

num1 = int(input("첫 번째 숫자를 입력하세요 >> "))
num2 = int(input("두 번째 숫자를 입력하세요 >> "))

print("덧셈 결과 : ", plus(num1, num2))
print("뺄셈 결과 : ", minus(num1, num2))
print("곱셈 결과 : ", multiply(num1, num2))
print("나눗셈 결과 : ", divide(num1, num2))
'''

'''
# 구구단 함수 만들기
def gugudan(dan):
    for val in range (1, 10 ,1):
        print('%d * %d = %d' % (dan, val, dan * val))    

dan = int(input("구구단 몇 단? >> "))
gugudan(dan)
'''

'''
# 아이디 비밀번호 확인
id = "admin"
password = "1234"

def accountCheck(userId, userPassword):
    if id == userId:
        if password == userPassword:
            print("로그인 성공")
        else:
            print("비밀번호가 틀립니다.")
    else:
        print("아이디가 틀립니다.")

userId = input("아이디를 입력하세요 >> ")
userPassword = input("비밀번호를 입력하세요 >> ")

accountCheck(userId, userPassword)
'''