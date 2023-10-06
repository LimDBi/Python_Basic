# 문제 1. 입력 된 단수를 출력하는 코드
# dan = input("단수: ")     #dan은 string타입
# dan = int(input("단수: "))  문자를 받자마자 int타입으로 바꿀 수 있음.
# for i in range(1, 10):
#    print(f"{dan}X{i}={i*int(dan)}")    #dan을 int타입으로 바꿔야 함.


# 문제 2. 2단부터 9단까지 출력하는 코드
# 2단부터 9단까지 출력 => for
for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i}X{j}={i*j}")
    print("-"*20)


# 문제 3. list a의 평균값을 계산하시오.
a = [1, 2, 3, 4, 5, 99, 87, 54, 2, 5, 4]
total = 0
for num in a:
    total += num  # total = total + num
length = len(a)
result = total/length
# round(값, 소숫점 숫자): 반올림 처리
print(round(result, 2))   # 평균값

# 문제 4. list b에서 최소값 찾기 (정렬 안하고 그냥 찾기만)
b = [22, 1, 4, 7, 98]
num_min = b[0]  # 최솟값 담을 공간
for x in b:   # 5번 반복
    if x < num_min:
        num_min = x
print(num_min)  # 1 출력

# 문제 5. list c의 최솟값, 최댓값 찾기
c = [2, 5, 7, 1, 8]
num_min = c[0]
num_max = c[0]
for i in c:
    if i < num_min:
        num_min = i
    if i > num_max:
        num_max = i
print(num_min)  # 1출력
print(num_max)  # 8출력


print("="*200)
# # 문제 6. 사용자가 입력한 값이 1, 2, 3인 경우 통과하고 아닌 경우 다시 입력하도록 작성
# count = 0 # 틀린 횟수
# while True:
#     if count >= 3:
#         print("프로그램을 사용할 수 없습니다.")
#         break
#     num = int(input("값: "))
#     # if 4 > num > 0: # num = 1, 2, 3
#     if num in [1, 2, 3]:
#         print(f"{num}을 입력하셨습니다.")
#         break
#     else:
#         print("1, 2, 3의 값만 입력해주세요.")
#         count += 1

# 문제 7. 1부터 100까지 총합을 출력하는 코드
# - for문으로 작성
sum = 0
for i in range(1, 101):
    sum += i
print(f"총합(for)문: {sum}")
# - while문으로 작성
num = 0
total = 0
while True:
    num += 1
    if num == 101:
        break
    total += num
print(f"총합(while문): {total} {num}")


