# 주석(comment): 단순 메모, 개발 실행 x

# 출력 함수(print)
# - ()안에 값을 추력
# - 변수 값 확인 용도 또는 메시지 출력 용도
print("="*200)
print("Hello Python")

# 문자열 타입(String Type)
# - Python: '', "" -> String
# - C, JAVA: ''(Char), ""(String)

# 참고: Escape Code
# - 문법: \(역 슬러쉬) + @
# - 문자열(String) 내의 일부 문자의 의미를 달리하여 특정한 효과 주기
# - 예) \n: 한 줄 개행, \t: 탭(8칸 공백)
print("="*200)
print("Hello\nWorld")
print("Hello\tWorld")

# 실행: ctrl + shift + f10
# 공부 tip)
# - 몇 버전부터 ~ 나온 기술(신기술) -> 신기술 공부, 구기술 공부 X -> 코드를 못 읽을 수 있음.

#자료형(type)
# - Python의 모든 자료형은 객체(Object)
# - c, Java 언어 문자형(char): 'A', 'E' 키보드 제어에 사용
# 1) 문자열(String): "Hello", 'Hi'
# 2) 정수형(int): 3, 0, -1
# 3) 실수형(float): 3.14, 0.0, -2.2
# 4) 논리형(boolean): True, False

# 예) 다양한 종류의 자료형을 사용하는 이유?
# - Java에서 정수형: byte, short, int, long
# - Python 정수형: int
# 만들어진지 오래된 언어는 다양한 종류의 자료형을 사용 -> 자원(메모리)을 효율적으로 사용하기 위함.
# 자료형은 담을 수 있는 크기의 범위가 지정되어 있어서, 만약에 크기가 작은 값을 크기가 큰 자료형으로 사용하면 메모리 낭비 유발

# Python 동적 타이핑 언어 -> Python 실행될 때 Type을 지정!
# type() 함수: ()안의 값의 Type을 확일할 때 사용.
print("="*200)
print(type("ABC"))
print(type(123))

#형 변환(Type Casting) *중요*
# - Type Casting을 사용하면 값을 원하는 자료형으로 변환 가능
# 1) int(): 정수형으로 변환
# 2) float(): 실수형으로 변환
# 3) str(): 문자열형으로 변환
print("="*200)

# Type Casting 실습
int_a = 3
float_b = 3.14
str_c = "9"
str_d = "9.2"
# 1) 문자열 정수형("9") -> 정수형(9)
print(int(str_c))
# 2) 문자열 정수형("9") -> 실수형(9.0)
print(float(str_c))
# 3) 문자열 실수형("3.14") -> 정수형 (Error: X)
# print(int(str_d))
# 4) 문자열 실수형("9.2") -> 실수형(9.2)
print(float(str_d))
# 5) 정수형(3) -> 실수형(3.0)
print(float(int_a))
# 6) 정수형(3) -> 문자열("3") *실행될 때 겹따옴표가 같이 나오지는 않음.
print(str(int_a))
# 7) 실수형(3.14) -> 정수형(3)
print(int(float_b))
# 8) 실수형(3.14) -> 문자열("3.14")
print(str(float_b))
# *주의* float("Hello"), int("Hello") 형 변환 불가!

# None
# - 아무런 값을 갖지 않을 때 사용
# - 일반적으로 변수가 초기값을 가지 않게 변수만 생성하고 싶을 때 사용
# - 기타 언어의 Null과 같은 의미로 사용
# 예) student_name -> 에러남.
print("="*200)
student_name = None  # 적극 권장 X(절대 사용 금지)
student_name = ""    # 적극 권장
# 이유는 "Null Point Exception" 이라는 Error가 뜨는데 개발자 공포의 대상임. 프로그램이 다 꺼짐.

# 기본 자료형(Primitive Type) : 변수에 값이 저장
# - int num = 4;
# 객체 자료형(Reference Type) : 변수에 값의 "주소"가 저장
# - String name = "10";
# * Java: 기본, 객체 모두 사용
# * Python: 객체만 사용


# C언어 변수 생성 -> int b;  (변수 생성, 값 x)
# Python 변수 생성 -> b (변수 호출, 변수 생성X) 동적 타이핑 변수라서.

# 변수(Variable)
# - 변수: "하나의 값"을 저장할 수 있는 메모리 공간.
print("="*200)
num = 4
num = 10
print(num)  # 출력: 10

# - 변수 생성 및 초기화
# num = 5 문법
# 대입연산자(=) : 우측의 값을 좌측에 저장
# 동등연산자(==) : Equal



