import datetime

# 1번 문제.
# 24시간을 표시하는 시계를 보는데 현재시간이 s, x분(1~1440)마다 시계를 볼때 '시간과 분'이 팰린드롬인 경우의 수는?
# input
s = "22:30"
x = 27


# 풀이
def palind_check(datetime):
    if divmod(datetime.hour, 10) == divmod(datetime.minute, 10)[::-1]:
        return True
    return False


count = 0
h, m = s.split(":")
input_time = datetime.datetime(1, 1, 1, int(h), int(m), 0)

if palind_check(input_time):
    count += 1

added_time = input_time + datetime.timedelta(minutes=x)

while [added_time.hour, added_time.minute] != [input_time.hour, input_time.minute]:
    if palind_check(added_time):
        count += 1
    added_time += datetime.timedelta(minutes=x)

# print("1번 문제 정답", count)

# 2번 문제.
# 길이 n의 배열 input_data가 주어짐. 연산 1번마다 배열의 양 끝 중 한 원소를 제거할 수 있음. 배열의 합이 s가 되게 하는 최소 연산횟수는? s가 되는 경우가 없으면 -1리턴. (n,s는 1이상)

n = 16  # 길이
s = 2  # 합
input_data = "1 1 0 0 1 0 0 1 1 0 0 0 0 0 1 1"
# input_data = "1 1 0"
arr = list(map(int, input_data.split()))

if sum(arr) < s:
    print(-1)

# 방법1. brute force
min = n
oper = n
tmp_len = 1

for k in range(0, n):
    for i in range(k + tmp_len, n + 1):
        if sum(arr[k:i]) == s:
            oper = n - len(arr[k:i])
            tmp_len = len(arr[k:i])
        if oper < min:
            min = oper
print("2번 문제 정답", min)

# 방법2.
