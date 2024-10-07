import random

print("\n1~50사이의 임의의 숫자를 컴퓨터가 선택합니다. 그 숫자를 맞혀 보세요.\n")

num = random.randint(1, 50)

user_guess = 0
count = 0

while num != user_guess:
  user_guess = int(input("\n숫자를 입력하세요. : "))
  count += 1
  if num > user_guess:
    print("\n더 큰 수입니다.")
  elif num < user_guess:
    print("\n더 작은 수입니다.")

print(f"\n정답입니다. {count}번 만에 맞추었습니다. ")
