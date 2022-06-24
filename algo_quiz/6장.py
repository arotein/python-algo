import collections
import re


# 리스트 평탄화 함수
def flat(nested_list):
    empty_list = []
    for k in nested_list:
        if type(k) != list:
            empty_list.append(k)
        else:
            empty_list.extend(flat(k))
    return empty_list


# 6장 문자열 조작
# p.138
string = "A man, a Plan, a canal: Panama".lower()
sub = re.sub("[^0-9a-z]", "", string)
print(sub == sub[::-1])

# p.148
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6 3", "let2 won kit dog", "let3 art zero"]
li_str = []
li_int = []
for log in logs:
    if log.split()[1].isalpha():
        li_str.append(log)
    else:
        li_int.append(log)

li_str.sort(key=lambda x: (x.split()[1:], x.split()[0]))
print(li_str + li_int)

# p.151
paragraph = "Bob hit a ball, the hit BALL flew far after it was git."

split = re.sub("[^a-z ]", "", paragraph.lower()).split((" "))
common = collections.Counter(split).most_common(1)[0][0]
print(common)

# p.153
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
empty_map = {}
for s in strs:
    sorted_str = "".join(sorted(s))
    if sorted_str not in empty_map.keys():
        empty_map[sorted_str] = [s]
    else:
        empty_map[sorted_str].append(s)
empty_li = []
for e in empty_map.values():
    empty_li.append(e)
print(empty_li)

# p.159
str_pal = "babadcabab"
longest = ""
for k in range(len(str_pal)):
    for i in range(k + 1, len(str_pal) + 1):
        if str_pal[k:i] == str_pal[k:i][::-1] and len(longest) < len(str_pal[k:i]):
            longest = str_pal[k:i]
print(longest)
