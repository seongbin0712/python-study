import random

menu = """
    0. 앞
    1. 뒤
"""

while True:
    print("\n컴퓨터가 동전을 던졌습니다.")
    computer = random.randint(0,1)

    print(menu)
    num = int(input("\n동전의 앞면(0)인지 뒷면(1)인지를 선택하세요. : "))

    if computer == 0:
        print("\n컴퓨터의 선택은 '앞면'입니다.")
    else:
        print("\n컴퓨터의 선택은 '뒷면'입니다.")

    if num == 0:
        print("나의 선택은 '앞면'입니다.")
    else:
        print("나의 선택은 '뒷면'입니다.")

    if computer == num:
        print("\n축하합니다! 맞히셨습니다.")
    else:
        print("\n아쉽네요. 틀렸습니다.")
    
    stop = input("게임을 중단하시겠습니까? (y) : ")
    if stop == "y":
        break