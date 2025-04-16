# 논리연산자
a = 10
b = 11
c = 12
d = 10

print(not(a<10)) # True
print((a<b) and (a>c)) # False
print((a>=c) or (a==d)) # True

# 3항 연산자
# (a > b) ? A : B
# (a > b) and A or B

money = int(input("돈을 넣어주세요 >> "))
count = int(input("몇장 드릴까요? >> "))

ticket = 1200

money = money - (ticket * count)

result = (money < 0) and "잔돈이 부족합니다." or "잔돈 >> " + str(money) + "원입니다."
print(result)