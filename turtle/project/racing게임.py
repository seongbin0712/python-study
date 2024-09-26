import turtle as t
import time
import winsound
import random

# 기본 설정
t.bgcolor("lavender")
t.up()
t.speed(0)
t.goto(0, 200)
t.write("터틀 레이스", False, "center", ("", 35))


# 경기장 그리기
t.goto(-400, 170)
t.down()
t.color("lightpink")
t.begin_fill()

for i in range(2):
  t.forward(800)
  t.right(90)
  t.forward(400)
  t.right(90)

t.end_fill()

# 결승선 그리기
t.color("black")
t.up()
t.goto(330, 200)
t.down()
t.goto(330, -250)

# 터틀 선수 생성

start_ycor = [150, 90, 30, -30, -90, -150, -210]
color_list = ["hotpink", "white", "red", "green", "yellow", "purple", "blue"]

# 레이스 라인 생성
for i in range(6):
  t.up()
  t.goto(-400, start_ycor[i] - 30)
  t.color('white')
  t.down()
  t.goto(400, start_ycor[i] - 30)

turtles = []
for i in range(7):
  new_turtle = t.Turtle()
  new_turtle.color(color_list[i])
  new_turtle.up()
  new_turtle.shape("turtle")
  new_turtle.goto(-370, start_ycor[i])
  new_turtle.write(i,)
  new_turtle.goto(-350, start_ycor[i])
  turtles.append(new_turtle)

#응원하기

user_choice = int(t.textinput("터틀 레이스", "몇 번 거북이가 이길까요?"))
t.up()
t.goto(0, -300)
t.color("black")
t.write(f"{user_choice}번 거북이를 응원했습니다.", False, "center", ("", 30))
t.ht()

# 경기시작 알림

winsound.Beep(523, 300)
time.sleep(0.5)

game_over = False

while not game_over:
  for i in turtles:
    rand_speed = random.randint(1, 10)
    i.forward(rand_speed)
    if i.xcor() > 330:
      game_over = True
      
max_xcor = 0
winner = 0

#winner 선정
for i in range(len(turtles)):
  if turtles[i].xcor() > max_xcor:
    max_xcor = turtles[i].xcor()
    winner = i

# 응원결과 발표하기

t.goto(0,0)
if user_choice == winner:
  t.write("응원하신 거북이가 1등 했습니다.", False, "center", ("", 30))
else:
  t.write(f"아쉽습니다.\n{winner}번 거북이가 1등 했습니다.", False, "center", ("", 30))

t.mainloop()