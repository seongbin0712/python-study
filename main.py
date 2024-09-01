def add(a, b):
  print(a + b)
  return a + b

def sub(a, b):
  print(a - b)
  return a - b

def mul(a, b):
  print(a * b)
  return a * b

def div(a, b):
  print(a / b)
  return a / b

def fourCalc(a, b):
  result = add(a, b)
  result = sub(result, b)
  result = mul(result, b)
  result = div(result, b)

fourCalc(3, 4)