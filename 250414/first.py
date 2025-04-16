print(1+2)
print("hello")
for i in range (3):
    print("hi there")
print("********************************")
for i in range (1,10):
    print("2 * ",i, " = ", 2*i)
print("********************************")
for i in range (2, 10):
    for j in range (1,10):
        print(i, " * ", j, " = ", i*j)
print("********************************")
name = input("당신의 이름은 뭐죠? >> ")
print(name)
number = int(input("정수 입력하기 >> "))
print(number)
print(number + 1)
a = int(input("첫번째 정수 입력 >> "))
b = int(input("두번째 정수 입력 >> "))
print(a+b)
print("********************************")
age = int(input("당신의 나이는? >> "))
if age >= 19:
    print("당신은 성인이군요!")
else:
    print("당신은 미성년자군요@@")
print("********************************")
if age >= 19:
    print("성인")
elif age >= 15 and age < 19:
    print("청소년")
else:
    print("아이")
print("********************************")
n = int(input("몇 줄 출력할까요? "))
for i in range(1, n + 1):
    print("*" * i)
print("********************************")
m = int(input("개행 없이 * 출력하기 몇줄 ?? >> "))
print(m)
for i in range(1, m+1):
    print("*" * i, end="")
print("------------------")
reverseNum = input("숫자를 길게 입력하기 >> ")
reversedNum = reverseNum[::-1]
print("숫자 뒤집기 출력 : ", reversedNum)
