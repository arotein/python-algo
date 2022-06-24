# 실행 전 에러 : 구분 오류 Syntax error
# 실행 중 에러 : 예외Exception 또는 런타임 오류 Runtime error

# 예외처리Exception handling : if문, try구문
"""
<try-except-else-finally구문>

try:
    예외발생 가능성있는 코드. except(또는 finally)를 무조건 작성해야됨
except:
    예외 발생시 실행할 코드
else:
    예외가 발생하지 않았을 때 실행할 코드(try블록에 넣어서 else문 안써도 됨)
finally:
    마지막에 무조건 실행할 코드. return, break 키워드와 관계없이 무조건 실행됨(개꿀)
    특히 파일의 close()함수 사용시 자주 이용됨
"""

"""
try:
    코드
except 예외종류1 as 예외객체명:
    코드
except 예외2:
    코드
except 예외3:
    코드
...
except Exception:
    코드
"""
# Exception : 최상위 예외클래스

# raise 예외객체 : 임의로 예외발생