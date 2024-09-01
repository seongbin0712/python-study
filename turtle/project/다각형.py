import turtle as t

#shape에는 triangle, square, arrow, circle, turtle
t.shape('turtle')
t.bgcolor('pink')
t.color('blue')

polygon = int(t.numinput("다각형 그리기", "몇각형을 그릴지 입력하세요."))

for i in range(polygon):
  t.forward(100)
  t.left(360/polygon)

t.mainloop()