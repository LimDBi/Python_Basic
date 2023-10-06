#조건문(Condition) : if~elif~else

#   - 특정 조건을 만족하는 경우에만 수행학 작업이 있는 경우
#   - 모든 조건은 boolean으로 표현 됨
#   - 조건문의 경우 if, elif, else 블록 내 종속된 코드 들여쓰기
#   - 모든 블록문의 시작점은 마지막에 :(콜론, colon) 추가
#   - python애서 블록내에 코드는 반드시 들여쓰기(tab)하도록 강제성 부여

# python의 if문 구조                #C, Java의 if문 구조
#   if 조건1:                        if () {
#       code                            code
#   else 조건2:                      } else if () {
#       code                            code
#                                    }
#
# 제어문 기본 문법
#  1. chain으로 묶인 구조 -> True가 나올 때까지 실행하다가 나오면 빠져나옴. 무조건 1개만 실행
#  if 조건1:
#     code
#  elif 조건2:
#     code
#  elif 조건3:
#     code
#  else:
#     code
#  2. 별개의 구조 -> 조건만 만족하면 실행
#  if 조건1:
#     code
#  if 조건2:
#     code
#  if 조건3:
#     code

# 조건문 4가지 조합
# 1. if
# 2. if~elif~elif
# 3. if~else
# 4. if~elif~else


# 점수계산기
#   - 91~100: A
#   - 81~90: B
#   - 71~80: C
#   - 61~70: D
#   - 60이하: F
score = 89 #0~100점
if score>=91:
    print("A")
elif score>=81:
    print("B")
elif score>=71:
    print("C")
elif score>=61:
    print("D")
else:
    print("F")

# 논리연산자: AND, OR, NOT  // 기말 필기 시험 출제
# 1. AND (조건이 모두 참이여야지만 참으로 출력)
# 조건1  조건2  결과
#   F      F      F
#   T      F      F
#   F      T      F
#   T      T      T
# 2. OR (조건 중에 하나라도 참이라면 참으로 출력)
# 조건1  조건2  결과
#   F      F      F
#   T      F      T
#   F      T      T
#   T      T      T
# 3. NOT
# T -> F
# F -> T

# 문제1. 어떤 종류의 학생인지 맞히기
# (초등, 중등, 고등, 대학생, 학생X)

# input(): 키보드 값 입력 => String(문자열)타입
from datetime import datetime
born = input("당신이 태어난 년도를 입력하세요: ")  # input 이 scanf + printf느낌. 출력할때는 print(born)
today =  datetime.today().year 
age = today - int(born) +1   # String타입의 born을 숫자로 바꿔서 뺄셈

if 8 <= age <= 26:
    if age >= 20:  # age <= 26 and age >= 20 와 26 >= age >= 20는 같음.
        print("대학생")
    elif age >= 17:
        print("고등학생")
    elif age >=14:
        print("중학생")
    elif age >= 8:
        print("초등학생")
else:
    print("학생이 아닙니다.")
