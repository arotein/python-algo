# class 선언
# <함수 내에서 변수선언시>
# 변수 = 값 : 함수 내에서만 쓰는 변수선언. 생성자 종료와 함께 사라짐. 함수내 변수선언과 같음.
# self.변수 = 값 : 객체자신만 가지는 속성
# Class.변수 = 값 : 모든 객체가 공유하는 속성

class Shavondi:
    # 클래스변수 선언 : 모든 객체가 공유하는 공간, static
    # 단, init에서 같은 변수명으로 재생성하면 공유안됨
    # pubic
    members = {}
    # private : getter, setter함수로 핸들링
    __ages = []
    # 생성자 Contructor : 객체 생성시 호출됨

    def __init__(self, name, age):
        # self는 자바의 this와 같음
        self.name = name
        self.age = age
        # 'self.변수'와 'Class.변수'의 차이점
        # self는 객체 자기자신만 해당함
        # Class 자체를 지시함. 즉, 클래스를 공유하는 모든 객체의 값에 영향을 줌. static.
        Shavondi.members[name] = age
        Shavondi.__ages.append(age)
        # 따라서, 객체생성시(init에서) 변수를 static으로 사용할건지, 아닌지 결정.

    # 소멸자 Destructor : 객체 소멸시 호출됨
    def __del__(self):
        pass

    # 객체명 설정 자바의 toString함수
    def __str__(self):
        pass

    # 메소드, 멤버 함수(member function), 인스턴스 함수(instance function)
    def func(self, name):
        pass

    # 클래스함수, 첫번째 인자로 클래스 자체가 들어감
    @classmethod
    def add_member(cls, name, age):
        # Shavondi.members를 cls.members로 사용가능
        cls.members[name] = age

    # getter생성 데코레이션
    @property
    def ages(self):
        return Shavondi.__ages

    # setter생성 데코레이션
    @ages.setter
    def ages(self, value):
        pass


# 객체 생성
member = Shavondi("통길", 30)

# 객체의 클래스확인
# isinstance(instance, class) -> bool : type()과 다르게 상속관계까지 확인. 부모클래스여도 True 리턴

# 데코레이터 : 함수 데코레이터, 클래스 데코레이터

# <예제>
class Sha:
    id = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_id(self, num):
        self.id = num

member1 = Sha("통길", 30)
member2 = Sha("통현", 31)
member1.set_id(10)
print(member1.id, member2.id, Sha.id)

Sha.id = 20
print(member1.id, member2.id, Sha.id)

"""
<결론>
클래스 변수('클래스 내부, 함수 밖'에 선언 또는 'Class.변수'로 선언)는
기본적으로 모든 객체와 데이터가 공유됨
하지만, 이후 객체가 self.를 이용해서 재선언하게되면 객체 자신만 가지는 데이터로 바뀜.
즉, 이름만 같고 실질적으로 다른 변수가 됨.
"""