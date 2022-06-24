# 리스트 선언
a = []
print(type(a))
b = [True, 2, "삼"]
print(b)

# 리스트 연산
# + : 연결, * : 반복, len() : 길이
li_1 = [1, 2, 3]
li_2 = ["안", "녕"]
print(li_1+li_2)
print(li_1*3)
print(len(li_2))
# len(문자열)도 가능
print(len("안농안농 ㅋㅋ"))

# 요소추가
# append(e) : 제일 뒤에 추가
li_1.append(5)
print(li_1)
# insert(idx, e) : 해당위치에 삽입
li_1.insert(3, 4)
print(li_1)
# extend(list) : 뒤에 리스트를 추가. '+'연산자와 달리 파괴적함수
li_1+li_1
print("+의 경우", li_1)
li_1.extend(li_1)
print("extend의 경우", li_1)

# 요소제거
# del list[idx] : 해당 인덱스 제거
# list.pop(idx) : idx 안넣으면 기본값 -1
# list.remove(ele)) : 최초로 등장하는 요소의 값만 제거. if문 처리
# list.clear() : 리스트 초기화

# 요소탐색 및 확인
# value in list -> bool
print(5 in li_1)
print(10 not in li_1)
# list.index(ele)) -> 인덱스값

# 반복문
# case 1
for i in range(5):
    print("5번출력", i)

# case 2
for i in range(1, 6):
    print("5번출력"+str(i))

# case 3
for k in range(1, 10, 2):
    print(k)

# case 4
for i in li_2:
    print(len(li_2), "만큼 출력", i)

# mutable : 가변 ... 일반적인 객체, list 등
# immutable : 불변 ... 기본타입, String객체, tuple 등

# list의 슬라이싱, copy ... 얕은 복사
# copy.deepcopy() ... 깊은 복사

# 리스트 사용시 주의점
# 리스트가 내부에 mutable객체를 포함하고있으면 list를 복사하여 사용해도 원본데이터가 바뀜
# 데이터값을 저장하는게 아닌 객체의 참조하기떄문

list_origin = [1, 2, [3, 4]]
list_copy = list_origin.copy()
list_copy[2][0] = 0
print(list_copy)
print(list_origin) # [1, 2, [0, 4]]
# 즉, 복사본을 수정했으나 원본 list가 바뀌어있음

import copy
list_deepcopy = copy.deepcopy(list_origin)
list_deepcopy[2][0] = -1
print(list_deepcopy)
print(list_origin)
