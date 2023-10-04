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

# 문제 4. list b에서 최소값 찾기
b = [22, 1, 4, 7, 98]
print(num_min) # 1 출력

