a = "안농칭구"

# 인덱싱
print(a[0], end="")
print(a[1])
# 슬라이싱
print(a[2:])

# [핵심] index를 n번째 글자가 아닌 n번째 커서의 위치로 생각하면 이해하기 편함
# 즉, I를 커서의 위치라고 하면 string = "안녕하세요"에서 0번째는 "I안녕하세요", 3번째는 "안녕하I세요"
# 따라서 num[0:3]은 0번커서와 3번커서 사이의 subString이므로 "I안녕하I세요"가 되어 "안녕하"가 출력되게 된다.
num = "1234"
print("num = " + num[0:3])

# 문자열 길이
print(len("안농안농"))
# type
print(type(52.1))
print(type(52))
print(type("안넝"))
# 연산자
# // 몫
# % 나머지
# ** 제곱
# 입력, input함수는 str로 리턴
a = input("숫자 입력 : ")
print(a)
print("a타입 :", type(a))
# 형변환 casting
b = int("100")
print("b타입 :", type(b))
c = str(b)
print("c타입 :", type(c))
# format()
print("이건 printf와 같음.\na : {0}\nb : {1}\nc : {2}".format(a, b, c))
# upper(), lower(), strip()
sentence = "   Hello~ Nice to meet you~   "
print(sentence.upper())
print(sentence.lower())
print(sentence.strip())
# 문자열구성파악 함수
print("isalnum, isalpha, isdecimal(정수형인지), isspace(공백만있는지), islower, isupper 등")
# 문자열 탐색
# find : 있으면 index 리턴, 없으면 -1 리턴)
# rfind: 오른쪽에서부터찾음
output_1 = sentence.find("Nice")
print(output_1)
output_2 = sentence.find("ㅋ")
print(output_2)
# in연산자 : bool형태로 리턴
output_3 = "Nice" in sentence
print(output_3)
# split : 특정문자로 나눔 -> list로 리턴
output_4 = sentence.strip().split(" ")
print(output_4)

# 나눗셈 연산자 특징 : 정수를 나누면 float타입으로 리턴
print(type(4))  # int
print(type(4 // 2))  # int
print(type(4 / 2))  # float
