import turtle as t

# 함수는 x, y의 좌표값을 제공(활용하면 됨)
def draw_ondrag(x, y):
  t.ondrag(None)
  t.goto(x, y)
  t.ondrag(draw_ondrag)

def green_color():
  t.color("greenyellow")

def pink_color():
  t.color("pink")

def black_color():
  t.color("black")

def white_color():
  t.color("white")

def penup():
  t.up()

def pendown():
  t.down()

def begin_fill():
  t.begin_fill()

def end_fill():
  t.end_fill()

t.speed(0)

t.bgcolor("lightblue")
t.pensize(3)

# event 활용법

# screen에 마우스를 클릭했을 때 event를 받는 함수
t.onscreenclick(draw_ondrag)

#키보드 event 처리 방법
t.onkeypress(green_color, "g")
t.onkeypress(pink_color, "p")
t.onkeypress(black_color, "b")
t.onkeypress(white_color, "w")
t.onkeypress(penup, "Up")
t.onkeypress(pendown, "Down")
t.onkeypress(begin_fill, "Left")
t.onkeypress(end_fill, "Right")
t.listen()

t.mainloop()