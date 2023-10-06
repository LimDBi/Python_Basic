# 제어문
#   1. 조건문(if)
#   2. 반복문(for, while)

# 반복문(Loop)
#   - 반복적인 작업을 가능하게 해주는 도구
#   - list, str, tuple 등 컬렉션 타입의 아이템을 하나씩 순회하면서 사용가능(for)
#   - 특정 조건을 만족하는 경우(while)

# 반복횟수 알 때 for문 사용  ex) 구구단, 게시판
# 반복횟수 모를 때 while문 사용   ex) 키오스크

# *for문 기본 문법
# for i in [1, 2, 3]:
#   print(i)
# *range() 함수
#  - default: 시작(0), 증감(+1)
#  - range(시작, 끝, 증감)  // 시작과 끝은 인덱스 값
#  - range(3)          => [0, 1, 2]
#  - range(1, 10)      => [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  - range(2, 5, 2)    => 2, 4 출력

# range()를 활용하여 1~9까지 출력하는 for문
for i in range(1, 10):
    print(i)

# List를 활용한 for문
temp = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
for alpha in temp:
    print(alpha)

# *enumerate()
#   - 반복횟수(index)를 출력하고 싶은 경우
#   - enumerate() : 0번 인덱스부터 시작
for i, alpha in enumerate(temp):
    print(i, alpha)

print("="*200)

# 구구단 2단 출력
# 2X1 = 2
# 2X2 = 4
# ...
# 2X9 = 18

# input() 활용해서 사용자가 입력한 값(2~9) => 해당 단 출력
for i in range(1,10):
    print(f"2X{i}={i*2}")

# dict를 사용한 for문
temp = {"A": 1,
        "B": 2,
        "C": 3,
        "D": 4}
print("="*100)
# dict => for => Key값 출력
# Keys(), values(), items()
for element in temp.values():    # default: temp.keys() = temp
    print(element)  # A, B, C, D
for key, value in temp.items():  # key와 value를 뽑아서 tuple값으로 바꿔줌.
    print(key)
    print(value)    #unpacking을 활용하여 key와 value를 따로 출력

# break, continue
# break: 즉시 반복문을 빠져 나감
# continue: 즉시 다음 반복으로 넘어감

print("="*200)
# a를 출력하다가 3을 만나면 멈추시오.
num = [1, 2, 3, 4, 5]
for i in num:
    if num == 3:
        break
    print(i)

print("="*200)
# 홀수만 출력
for i in range(30):
    if i % 2 == 0:
        continue
    print(i)
