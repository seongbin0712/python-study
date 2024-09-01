import turtle as t
# start - 꽃잎을 그리는 함수

def petal():
  for j in range(2):
      t.circle(150, 110)
      t.left(70)

# end - 꽃잎을 그리는 함수

# start - 꽃을 그리는 함수
def draw_flower():
  t.color("pink")
  t.begin_fill()

  for i in range(5):
    petal()
    t.left(70)
    t.left(360/5)
  t.end_fill()

  t.goto(3, -30)
  t.color("hotpink")
  t.begin_fill()
  t.circle(30)
  t.end_fill()
#end - 꽃을 그리는 함수

t.speed(0)
t.bgcolor("ivory")
t.hideturtle()

draw_flower()


t.mainloop()