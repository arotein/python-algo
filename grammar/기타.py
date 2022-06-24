# Naming Convention
#   camelCase
#   snake_case
#   PascalCase
#   kebab-case

# 3.7부터 구조체 지원
import collections
from dataclasses import dataclass


@dataclass
class Product:
    weight: int = None
    price: float = None


apple = Product()
apple.price = 100
print(apple.price)


# 클래스 선언시에도 dataclass데코레이션 이용가능 -> 내부함수기능 자동구현해줌
@dataclass
class Rectangle:
    width: int
    height: int

    def area(self):
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area())

# Generator : iterator 를 생성해 주는 function. 생성조건만 저장하는 방법.
#   배열자체를 저장하는게 아니라서 메모리절약됨
#   yield구문, next()함수 등을 이용해서 요소 하나씩 가져올 수 있음
#   yield구문 : 값의 리턴과 동시에 함수를 정지시킴. 따라서 메모리에 내부변수들이 여전히 존재하는 상태.

# enumerate() : index와 요소를 묶어서 보관하는 enumerate객체, 일회용임
list_ori = [10, 2, 34, 40, 59]
list_enum = enumerate(list_ori)
print(list_enum)
print(list(list_enum))
list_enum = enumerate(list_ori)
for i, v in list_enum:
    print(i, v)

# divmod(dividend, divisor) -> (quotient, remainder):
print(divmod(10, 3))

# 가독성
# if len(users) = 0:    (X)
# if not users:         (O)

# if foo is not None and not foo:   (X)
# if foo == 0:                      (O)

# <시간 복잡도>
# 빅오(O) : 상한. 최악의 상황과는 무관. 적당히 잘 표현하기위한 표현식
#   ex) O(nlogn)이 참 -> o(n^2), o(n^3)도 참. 당연히 nlogn 보다 낮으므로.
# 빅오메가(Ω) : 하한
# 빅세타(Θ) : 평균

# (2.4부터 int로 통합) int형의 값이 충분하지않으면 자동적으로 long타입으로 바뀜.

# primitive type, reference type객체 비교시 유의사항
# is 연산자 : id()값 비교
# == 연산자 : 값만 비교
# None : null로 값자체가 정의되어있지 않음. 따라서 is로만 비교가능

# defaultdict객체 : 존재하지 않는 키를 조회 -> 에러대신 아이템 추가
a = collections.defaultdict(int)
a['A'] = 5
a['B'] = 3
a['C'] += 1  # 일반 dict형이면 에러남
print(a)

# Counter객체 : 아이템 개수 리턴
b = [1, 2, 3, 5, 7, 9, 2, 5, 2, 3, 8, 0, 7, 6, 8, 5, 1, 2, 3, 2, 3, 3, 0]
print(collections.Counter(b))
print(collections.Counter(b).most_common(2))  # 빈도수가 높은 요소 2개

# list.[::-1]이 list.reverse()보다 빠름
# [::-1]는 사본 리턴, reverse()는 리스트 자체를 변경
# str도 [::-1] 사용가능

# 파이썬 정렬함수 : Timsort알고리즘 사용

# list.sort() -> None : 파괴적함수
# sort(key=func) : 함수의 값을 기준으로 정렬
#   func이 배열을 리턴시 0번, 1번, ...인덱스 값을 기준으로 정렬

# sorted(list) -> list : 리스트정렬, 복사본리턴
# sorted(str) -> 인덱스 하나하나 정렬해서 list로
str_a = "eat"
print(sorted(str_a))
print(''.join(sorted(str_a)))

# max(*비교할요소들, key=func) : 기준을 func로 설정가능
