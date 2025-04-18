'''
# 커피 자판기
def coffee_machine(coffee):
    print('1. 물을 준비한다')
    print('2. 컵을 준비한다')

    if coffee == '아메리카노':
        print('3. 아메리카노를 탄다')
    elif coffee == '카페라떼':
        print('3. 카페라떼를 탄다')
    elif coffee == '카푸치노':
        print('3. 카푸치노를 탄다')
    else:
        print('3. 이번만 특별히.. 해드립니다...', coffee, '드릴게요!')

    print('4. 물을 붓는다')
    print('5. 스푼으로 커피를 저어준다')
    print('6. 맛있게 드세요 :)')

coffee = ''

orderNum = int(input('몇 분이세여~? '))

for i in range(orderNum):
    print(i + 1, '번 손님 주문하세요~')
    coffee = input('커피를 선택하세요 (아메리카노, 카페라떼, 카푸치노): ')
    coffee_machine(coffee)
'''

'''
# 전역 변수
hap = 100

def sum(value):
    hap = 20
    hap += value
    print('hap >> ', hap)

sum(10)
print('hap >> ', hap)
'''

# global 키워드
hap = 100
num = 50

def sum(value):
    global hap
    hap += value
    print('hap >> ', hap)
    print('num >> ', num)

sum(10)
print('hap >> ', hap)

