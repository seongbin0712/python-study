import turtle as t
import random

color = ("red", "orange", "blue", "green", "white", "yellow", "indigo", "pink")
t.hideturtle()

t.bgcolor("black")
t.speed(0)

#별 그리는 위치를 random으로 x,y값을 생성하는 부분

for x in range(20):
  t.up()
  t.goto(random.randint(-300, 300), random.randint(-300, 300))
  t.down()

  t.color(random.choice(color))
  t.begin_fill()

  start_size = random.randint(5, 15)

#별 그리는 로직

  for i in range(5):
    t.forward(start_size)
    t.left(72)
    t.forward(start_size)
    t.right(144)

  t.end_fill()

t.mainloop()