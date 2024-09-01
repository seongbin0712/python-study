# 함수의 정의

#def 함수이름():
  #code_block
  #code_block
  #code_block
  #code_block

#함수 선언

def multiply(a, b, c):
  return a * b * c

def add(a, b, c):
  result = multiply(a, b, c)
  return result

# 정의한 함수를 호출하거나, 실행하기 위해서는,

result = add(3, 4, 5)
print(result)