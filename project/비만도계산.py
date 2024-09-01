print("\n비만도 검사에 오신것을 환영합니다.\n")

print("""
        - 검사결과 판정 기준 -
      
        18.5 미만     :     저체중
        18.5 ~ 22.9     :   정상
        23 ~ 24.9       :   과체중
        25이상          :   비만
""")

height = float(input("키를 입력하세요. (Cm) : "))
weight = float(input("몸무게를 입력하세요. (Kg) :"))

bmi = weight / (height * height) * 10000

if bmi < 18.5:
    print(f"당신은 저체중 입니다. 결과 : {bmi}")
elif bmi < 23:
    print(f"당신은 정상 입니다. 결과 : {bmi}")
elif bmi < 25:
    print(f"당신은 과체중 입니다. 결과 : {bmi}")
else:
    print(f"당신은 비만 입니다. 결과 : {bmi}")