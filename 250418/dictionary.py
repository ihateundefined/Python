# 딕셔너리
# 딕셔너리 변수 = {키: 값, 키: 값, ...}
product = {'컵라면': 800, '삼각김밥': 1000, '비타500': 500}
word = {'boy': '소년', 'girl': '소녀', 'family': '가족'}

print(product) # {'컵라면': 800, '삼각김밥': 1000, '비타500': 500}
print(word)

print(product['컵라면']) # 800
print(word['girl']) # 소녀

# 딕셔너리 추가
# product[키] = 값

product['아이스크림'] = 2000
product['닭다리'] = 3000
print(product)

# 딕셔너리 삭제
# del 딕셔너리[키]
del product['비타500']
print(product)

# 키를 통해서 딕셔너리 값에 접근
# 딕셔너리름.get(키) -> 값
print(product.get('삼각김밥')) # 800

# 딕셔너리의 모든 키 반환
# 딕셔너리.keys() -> 키 리스트
print(product.keys()) # dict_keys(['컵라면', '삼각김밥', '아이스크림', '닭다리'])
# 리스트로 변환 -> type casting
print(list(product.keys())) # ['컵라면', '삼각김밥', '아이스크림', '닭다리']

# 딕셔너리의 모든 값 반환
# 딕셔너리.values() -> 값 리스트
print(product.values()) # dict_values([800, 1000, 2000, 3000])

# 리스트로 변환 -> type casting
print(list(product.values())) # [800, 1000, 2000, 3000]

# 딕셔너리에 해당 키가 있는지 확인
# 키 in 딕셔너리 -> True/False
print('컵라면' in product) # True
print('비타500' in product) # False

'''
item = input('궁금한 상품명 입력 >> ')

if (item in product):
    print('해당 상품을 찾았습니다')
    print(f'{item}의 가격은 {product[item]}원입니다.')
else:
    print('그런 상품은 없네요 ㅜㅜ 유감')
'''

# 나라 별 수도 찾기
capital = {'네팔' : '카트만두',
           '대한민국' : '서울',
           '일본' : '도쿄',
           '중국' : '베이징',
           '이탈리아' : '로마',
           '러시아' : '모스크바',
           '독일' : '베를린',
           '미국' : '워싱턴',
           '프랑스' : '파리',
           '영국' : '런던'}

while (True):
    country = input(str(list(capital.keys())) + '나라의 수도는 어디일까요?')

    if country in capital:
        print(country, '의 수도는', capital.get(country), '입니다.')
        print(f'{country}의 수도는 {capital[country]}입니다.')
    elif country == 'exit':
        print('프로그램을 종료합니다.')
        break
    else:
        print('그런 나라 없습니다.')
