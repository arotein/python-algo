# Boolean형은 True, False -> 대문자!
print(True)
print(False)
# 부정문은 not을 붙임
print(not True)
# or, |, and, &, ^ 사용가능
print(True | True)
print(True ^ False)
# ^는 비트연산자
# 바이너리 코드의 각 자리수가 다르면 1(True) 같으면 0(False)


# if문
if 0 ^ 1:
    print("1은 True와 같으므로 실행됨")
else:
    print("실행안됨")

num = 132
if num % 3 == 1:
    print("{}을 3으로 나눈 나머지가 1".format(num))
elif num % 3 == 2:
    print("{}을 3으로 나눈 나머지가 2".format(num))
else:
    print("{}은 3으로 나누어 떨어짐 ㅅㄱ".format(num))


# 삼항연산자
# 자바 : (평가식) ? (true일 때 리턴할 값) : (false일 때 리턴할 값);
# 파이썬 : (True일 때 리턴할 값) if (조건식) else (False일 때 리턴할 값)
print("안농" if True else False)
