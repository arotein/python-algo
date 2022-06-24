from typing import Dict

# 함수 선언 및 타입 힌트(강제성 없음, typing모듈 이용)


def func(a: int, b: int, *c, d=0, e=1) -> None:
    print("매개변수 a~d")
    print("일반 매개변수 a, b. 순서에 맞게 필수로 입력")
    print("가변 매개변수 c")
    print("기본 매개변수(기본값이 정해짐) d, e")
    print("키워드 매개변수(이름을 직접 지정해서 값을 입력하는 매개변수)\
        가령 fun(10, 20, e=10, d=20)같은 방법.")
    return


# 변수 타입 선언
v: Dict[str, int] = {"A": 100, "B": 50}

print(v)

# 함수 내부에서 함수 외부변수 참조불가. 따라서 함수의 인자로 넣던지 내부에서 global키워드를 사용해야됨.
counter = 0


def count(n):
    for i in range(n):
        global counter
        counter += 1
    return counter


print(count(10))


# tuple 선언
tuple_a = ()
tuple_b = ("하이")
tuple_c = ("헬로", )
print(type(tuple_a))
print(type(tuple_b))
print(type(tuple_c))

# 튜플 : 내부요소 변경 불가능. 추가는 됨.
tuple_aa = ("A", "B", "C", "D")
print(tuple_aa)
tuple_aa += ("E", "F")
print(tuple_aa)
# tuple_aa[0] = 1 : 에러뜸
print(tuple_aa[0])

# 튜플 활용
a, b = 0, 100
print(a, b)

a, b = b, a
print(a, b)

c = 10, 20, 30
print(c)

# 함수를 매개변수로 가지는 함수
# map(func, list) -> list : 각 요소를 함수에 넣은 '결과를 list로 생성'
# filter(func, list) -> list : 각 요소를 함수에 넣어 True이면 '인자로 사용된 list의 요소를 list로 생성'
# filter의 경우 func의 return값이 bool이어야 함

# 람다lambda : 간단하게 함수를 선언하는 방법 (익명함수)
print([k for k in map(lambda x: x*x, [1, 2, 3, 4, 5])])

li_1 = [1, 3, 4, 5, 6, 7, 8, 9]
li_2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(map(lambda x, y: x*y, li_1, li_2))
