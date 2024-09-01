art = """
            S     S
        S        S
       S    S      S
        S     S  S
  ************************   **
   **                  **  ***
     **    Coffee    ** ****
       **          **
          ********
"""

menu = """

     - 커피 자판기 메뉴 -

  1. 아메리카노       1,800원
  2. 카페라떼         2,700원
  3. 핫초코           2,300원
"""

print(art)

order_end = False


print(menu)
print("=" * 50)

order = int(input("커피 종류를 선택해주세요. : "))