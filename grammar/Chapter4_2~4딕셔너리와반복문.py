import time

# 딕셔너리 선언
a = {}

a = {
    "a": 1,
    "b": 2,
    "c": False,
    4: True
}

print(a["b"])
print(a[4])
# 요소추가
a["hi"] = "hello"

# 요소 삭제
del a["c"]

print(a)
# 요소 탐색 key in dict
if "hi" in a:
    print("hi들어있고 값은", a["hi"])
else:
    print("응 \"hi\"는없어")

if "c" in a:
    print("c도 들어있음")
else:
    print("응 c는없어")

# dict[key] : key가 없으면 에러. 따라서 if문 필요
# dict.get(key) : key가 없으면 None리턴

# for key in dict:

# 타입체크
result1 = type("") == str
result2 = type(a) is not dict
print("result1 :", result1)
print("result2 :", result2)

# list conprehensions
print("<list conprehensions>")
list_a = [k*10 for k in range(11)]
print(list_a)
list_aa = [k for k in range(1, 11) if k % 2 == 0]
print(list_aa)

for e in range(len(list_a)):
    print("현재 {}번째 출력".format(e))

# while문
while len(list_a) != 0:
    print("list_a : ", list_a)
    list_a.pop()

# 3초간 반복, import time 추가
num = 0
target = time.time() + 3
while time.time() < target:
    num += 1
print(num)

# min(list), max(list), sum(list)

# 리스트 뒤집기 list[::-1], 비파괴적
# 문자열 뒤집기 "str"[::-1]

# enumerate(list) : 튜플타입의 (index, element)세트로 변환하여,
#   iterator(일회용)형태로 저장(메모리효율). next(iterable)함수로 요소 하나씩 꺼낼수있음.

# dict.items() : 튜플타입의 (key, value)세트로 변환하여 dict_items타입으로 변환

list_b = [k for k in range(10)]
enum = enumerate(list_b)
for e in enum:
    print(e)
print("끝")
for e in enum:
    print(e, "출력안됨. iterator이기떄문. 따라서 변수저장이 아닌 필요할떄마다 매번 생성해야됨")

list_1 = [k for k in range(3)]
dict_1 = {1: 1, 2: 2, 3: "삼"}
print(type(enumerate(list_1)))
print(enumerate(list_1))
print(type(dict_1.items()))
print(dict_1.items())

for key, value in dict_1.items():
    print("key : {}, value : {}".format(key, value))

# dict.values() -> dict_values([list])형태로 value들만 리턴
print(dict_1.values())
# dict.keys() -> dict_keys([list])형태로 keys 리턴
print(dict_1.keys())
for value in dict_1.values():
    print(value)

# 3.7부터 dict의 내부순서 유지됨

# str.join(list[str]) -> str : list요소 사이사이에 문자열 삽입
print("!".join(["앙", "기", "모", "띠"]))
st = "이렇게 많은 문자열 사이사이에 글자를 넣는다면 어떨까?"
print("!".join(st))
