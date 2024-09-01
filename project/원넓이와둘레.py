print("\n반지름을 입력하면, 원의 넓이와 원의 둘레를 계산해 줍니다.\n")

r = float(input("반지름을 입력하세요. : "))

area = r * r * 3.14
circumference = 2 * r * 3.14

print(f"원의 면적은 : {area}입니다.")
print(f"원의 둘레는 : {circumference}입니다.")