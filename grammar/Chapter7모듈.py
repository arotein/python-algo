# import math
# ceil(x) : 올림
# floor(x) : 버림
import math as m
print(m.ceil(2.5))
# from math import *
# from math import ceil, floor

# 참고로 round()함수는 반올림이 아님.
print(round(2.5))
print(round(3.5))


# import random as r
# random() : [0, 1) float 랜덤 리턴
# uniform(a, b) : [a, b) float 랜덤 리턴
# randrange(a) : [0, a) int 랜덤 리턴
# randrange(a, b) : [a, b) int 랜덤 리턴
# choice(list) : list요소 랜덤 리턴
# shuffle(list) : list요소 섞음(파괴적)
# sample(list, k = n) : list요소 n개 추출

# import sys : 시스템관련

# import os : 폴더, 파일 관련

# import datetime : 날짜관련
# now = datetime.datetime.now()

# import time : 코드 실행시간 및 일시정지
# time.sleep(2)

# import urllib : URL관련

# 개발자가 모듈의 함수 호출, 일반적인 제어 -> library
# 개발자가 만든 함수를 모듈이 실행, 제어역전(IoC; Inverse of Control) -> Framework

# 모듈만들기 p.350~