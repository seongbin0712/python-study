menu = """
    교통 수단 선택
  1. 버스 : 750원
  2. 지하철 : 1200원
  3. 택시 : 4800원
"""

charge = 0

while True:

  new_charge = input("\n교통카드 금액을 충전하세요. : ")

  if not new_charge.isdigit():
    print("\n잘못된 금액을 입력하였습니다.")
    continue

  charge = charge + int(new_charge)

  while True:
    price = 0
    print(menu)
    choice = int(input("교통 수단을 입력하세요. : "))

    if choice == 1:
      price = 750
    elif choice == 2:
      price = 1200
    elif choice == 3:
      price = 4800
    else:
      print("이용할 수 없는 교통 수단입니다.")
      continue

    if charge - price > 0:
      charge = charge - price
      print(f"현재 남은 금액은 {charge}원입니다.")
    else:
      print("잔액이 부족합니다.")
      break

    go = input("\n다른 교통 수단을 이용하시겠습니까? (y) : ")
    if go != 'y':
      exit()