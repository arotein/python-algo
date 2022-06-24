import collections
import re
from typing import List


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
class Solution:
    # p.138
    def isPalindrome(self, s: str) -> bool:
        str_lower = s.lower()
        sub = re.sub("[^0-9a-z]", "", str_lower)
        return sub == sub[::-1]

    # p.148
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        li_str, li_int = [], []
        for log in logs:
            if log.split()[1].isalpha():
                li_str.append(log)
            else:
                li_int.append(log)
        li_str.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return li_str + li_int

    # p.151
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = []
        p_split = re.sub("[^a-z ]", " ", paragraph.lower()).split((" "))
        for k in range(len(p_split)):
            if p_split[k] not in banned + [""]:
                words.append(p_split[k])
        return collections.Counter(words).most_common(1)[0][0]

    # p.153
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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
        return empty_li

    # p.159
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
                left -= 1
                right += 1
            return s[left + 1:right - 1]

        if len(s) < 2 or s == s[::-1]:
            return s
        result = ""
        for k in range(len(s) - 1):
            result = max(result, expand(k, k + 1), expand(k, k + 2), key=len)
        return result
