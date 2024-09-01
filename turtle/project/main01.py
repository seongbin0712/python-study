import turtle as t

#선 색상을 지정하는 것

t.color('blue')

# 모양

t.shape("turtle")

# 선 굵기 지정

t.width(3) # 또는 t.pensize(3)

# 펜 들기

t.up()
t.down()

#앞으로 가기, 반시계 방향으로 돌기, 시계 방향으로 돌기, 뒤로 가기

t.forward(100)
t.left(90)
t.right(90)
t.back(100)

# turtle 위치 이동

t.up()
t.goto(300, 300)

position = t.pos()
print(position)

t.mainloop()