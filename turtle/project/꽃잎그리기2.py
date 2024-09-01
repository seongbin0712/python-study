import turtle as t
import random

#  start - color를 생성하는 함수 (결과값이 튜플로 return됨)
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return r, g, b
# end - color를 생성하는 함수

# start - 꽃잎을 그리는 함수
def petal(size, angle):
  for j in range(2):
    t.circle(size, angle)
    t.left(180 - angle)
# end - 꽃잎을 그리는 함수

# start - 꽃을 그리는 함수
def draw_flower(petal_num, size, angle):
  # random_color : 0 ~ 255 사이의 r, g, b 값이 return 된다.
  t.color(random_color())
  t.begin_fill()

  for i in range(petal_num):
    petal(size, angle)
    t.left(360 / petal_num)

  t.end_fill()

  t.goto(3, -30)
  t.color(random_color())
  t.begin_fill()
  t.circle(30)
  t.end_fill()
#end - 꽃을 그리는 함수

t.speed(0)
t.bgcolor("ivory")
t.hideturtle()
t.colormode(255)

petal_num = random.randint(4, 10)
petal_size = random.randint(50, 120)
petal_angle = random.randint(90, 130)

draw_flower(petal_num, petal_size, petal_angle)

t.mainloop()