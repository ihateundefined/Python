'''
# 무한 루프에 빠지지 않게 주의
iLoop = 0
while iLoop < 5:
    print("Hello World")
    iLoop += 1
'''

'''
# break문을 사용하여 무한 루프 탈출하기
hap = 0
iNum = 0

while True:
    iNum = int(input("정수를 입력하세요(-1: 종료) >> "))
    if iNum == -1:
        print("프로그램을 종료합니다.")
        break
    hap += iNum
    print("현재까지의 합계 : ", hap)
'''

# continue문을 사용하여 특정 조건을 건너뛰기
hap = 0
iNum = 0
iLoop = 0

while iLoop < 10:
    iNum = int(input("정수를 입력하세요(-1: 종료) >> "))
    if iNum == -1:
        print("프로그램을 종료합니다.")
        break
    if iNum % 2 == 0:
        print("짝수는 건너뜁니다.")
        iLoop += 1
        continue
    hap += iNum
    print("현재까지의 합계 : ", hap)