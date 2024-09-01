import turtle as t

t.bgcolor("black")
t.color("pink")
t.speed(0)

for i in range(200):
  t.pensize(i/50)
  t.forward(i)
  t.left(65)


# 줄기 그리기

t.color("lightblue")
t.setheading(270)

for i in range(50):
  t.pensize(25 - i / 2)
  t.forward(i / 4)

#꽃잎 그리기

t.color("yellowgreen")
t.setheading(60)

for x in range(100):
  t.pensize(100 - x)
  t.forward(x / 10)

t.hideturtle()

t.mainloop()