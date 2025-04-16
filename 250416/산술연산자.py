money = int(input("돈을 넣어주세요 >> "))
count = int(input("몇장 드릴까요? >> "))

ticket = 1200

money = money - (ticket * count)
print("잔돈은", money, "원입니다.")