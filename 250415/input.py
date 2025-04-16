#fruit = input("종아하는 과일 뭐에요?? >> ")
#print("내가 좋아하는 과일은 >> ", fruit)

#userId = input('아이디를 입력하세요 >> ')
#userPassword = input('비밀번호 입력하세요 >> ')
#print("당신이 입력한 아이디는 >> ", userId)
#print("당신의 비밀번호는 >> ", userPassword)

# input을 통해서 입력받은 데이터는 string
strNum1 = input("첫번째 숫자 >> ")
strNum2 = input("두번째 숫자 >> ")
print(strNum1 + strNum2)
print(type(strNum1 + strNum2)) # <class 'str'>

# type casting
# 정수 형변환 int(variable)
print(int(strNum1) + int(strNum2))
