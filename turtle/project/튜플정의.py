# 튜플의 정의 방법

t = (1, 2, 3)
t1 = 1, 2, 3
t2 = 1,         # t2 = (1,)

print(t, type(t))
print(t1, type(t1))
print(t2, type(t2))

# 튜플은 값이 변경되어서는 안되는 경우에 사용한다.
# 터틀에서는 주로 좌표값을 나타낼 때 많이 사용됨. (x,y)

t[0] = 5

print(t, type(t))


