import collections
import copy
import datetime

string = "안녕하세요"

result = "응 참이야" if 10 < 30 else 2

li_a = [0, 1, 2, "삼", [True, False], 5]
deepcopy = copy.deepcopy(li_a)
li_a[4].pop(1)

di = {
    1: True,
    2: False,
    3: None
}
li = [1, 3, 2, False, True, "hi"]

for (k, v) in di.items():
    print(k, v)

st = "이렇게 많은 문자열 사이사이에 글자를 넣는다면 어떨까?"
print("!".join(st))

li_1 = [11, 22, 33, 44, 55]
li_2 = [10, 20, 30, 40, 50, 60, 70]
print([k for k in map(lambda x, y: x * x * y, li_1, li_2)])

n = 10
try:
    if n > 10:
        raise Exception
    else:
        print("예외안뜸 ㅅㄱ")
except Exception as ex:
    print(ex)
else:
    print("예외 안뜬거 맞음 ㅋ")

# divmod(10, 3) -> (몫, 나머지)
print(divmod(10, 3))
# None 은 ==가 아니라 is로 비교하자
# << 딕셔너리 모듈 >>
di = {1: True, 2: "이", 3: [0, 1, 2]}
if di.get(4) is None:
    di[4] = 10
counter = collections.Counter(li_1)
# collections.Counter(리스트) 리스트의 각 원소들의 개수
# collections.Counter(리스트).most_common(n) 빈도 높은 순서로 n개 추출
print(counter.most_common(2))
print(collections.Counter(di))

# sorted() : sorted된 사본 리턴, .sort() : 원본 sort
# 문자열을 sort하는 방법
string_alpha = "eat"
sorted = "".join(sorted(string_alpha))
print(sorted)

# 리스트를 sort하는 방법1
li_s = ['aaa', 'bb', 'c', 'dddd']
li_s.sort(key=len)
print(li_s)

# 리스트를 sort하는 방법2
li_ss = ['asd', 'weq', 'zcs', 'csa', 'ads', 'ddqw']
li_ss.sort(key=lambda x: (x[0], x[1]))
print(li_ss)

# 리스트 인덱스 관련
# arr[a:b:c] : a번index부터 b번index미만(= (b-1)번 index)까지 c간격으로 배열을 만듦
# arr[::2] : 0번index부터 끝까지 2간격으로. -> 0, 2, 4, ... 번째 원소로 이루어진 배열을 만듦

# 리스트 합치기
# li_a + li_b 는 li_a.extend(li_b)와 같다

# 같은 길이의 리스트 원소들끼리 덧셈
# [li_a[k] + li_b[k] for k in range(len(li_a))]

# list 원소들 sum, max, min
li_sum = [1, 3, 5, 7, 9]
print(sum(li_sum))
print(max(li_sum))
print(min(li_sum))

# datetime관련 모듈
# time객체끼리는 연산이 안 됨. datetime + datetime 혹은 datetime + timedelta 는 연산 가능
datetime = datetime.datetime(1, 1, 1, 3, 15, 0)
print(datetime.hour)  # int로 반환

# split()과 split(" ")는 같다.

# enumerate(list) -> list를 (index, value)로 1개씩 리턴
# list.index(value) -> 리스트의 원소중 value값을 가지는 원소의 index를 리턴
for k in enumerate(li_sum):
    print(k)
for k, i in enumerate(li_sum):
    print(k, li_sum.index(i))

# if left_max < height[left]:
#     left_max = height[left]
# if right_max < height[right]:
#     right_max = height[right]
# 를 간단하게
# left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
