dic_eng = {
  "apple" : "사과",
  "peach" : "복숭아",
  "banana" : "바나나",
  "mango" : "망고",
  "watermelon" : "수박",
  "melon" : "멜론"
}

menu = """
  메뉴 선택

  1. 단어 보기
  2. 단어 외우기
  3. 단어 추가
  4. 단어 삭제
  5. 단어 수정
"""

while True:
  print(menu)
  choice = int(input("메뉴를 선택하세요. : "))

  if choice == 1:
    for i in dic_eng:
      print(f"{i} : {dic_eng[i]}", end=" ")

  elif choice == 2:
    for i in dic_eng:
      user_input = input(f"\n{i}의 뜻은 무엇일까요? : ")
      if user_input == dic_eng[i]:
        print("\n정답입니다!")
      else:
        print(f"틀렸습니다. 정답은 {dic_eng[i]}입니다.")

  elif choice == 3:
    eng = input("새로운 영어 단어를 입력하세요. : ")
    han = input("영어의 뜻을 입력하세요. : ")
    dic_eng[eng] = han

  elif choice == 4:
    del_word = ("삭제할 영어 단어를 입력하세요. : ")
    del dic_eng[del_word]

  elif choice == 5:
    mod_word = input("뜻을 수정할 영어 단어를 입력하세요. : ")
    mod_han = input("뜻을 입력하세요. : ")
    dic_eng[mod_word] = mod_han