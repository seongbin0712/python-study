import turtle as t
import random
import time

t.bgcolor("pink")
t.hideturtle
t.up()

num_times = int(t.textinput("숫자 기억게임", "몇 개의 숫자로 진행하시겠습니까? : "))

t.write("숫자 기억하기 게임을 시작합니다", False, "center", ("", 30))
time.sleep(3)
t.clear()

num = ""

for x in range(num_times):
  rand_num = random.randint(1, 50)
  t.write(rand_num, False, "center", ("", 70))
  num += str(rand_num) + " "
  time.sleep(1)
  t.clear()
  print(num)

user_input = t.textinput("숫자 기억 게임", "기억한 숫자를 입력하세요")

if user_input == num.strip():
  t.write("정답입니다.", False, "center", ("", 30))
else:
  t.write("멍청하네요.", False, "center", ("", 30))
  t.goto(0, -50)
  t.write(f"정답은 {num}입니다", False, "center", ("", 30))
  t.goto(0, -100)
  t.write(f"당신이 입력한 숫자는 {user_input}입니다", False, "center", ("", 30))

t.mainloop()