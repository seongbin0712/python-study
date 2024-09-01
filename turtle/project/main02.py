import turtle as t

t.shape("turtle")

t.speed(0)

#for steps in range(100):
  #for c in ('blue', 'red', 'green'):
   # t.color(c)
   # t.forward(steps)
   # t.right(30)

t.color('red')
t.fillcolor('yellow')
t.begin_fill()

while True:
  t.forward(200)
  t.left(170)
  if abs(t.pos()) < 1:
    break

t.end_fill()




t.mainloop()