# 주차 타워 구현
# 조건: 1층~5층, 층별로 1대만 주차
# 차량 번호: 숫자4자리
# 기능:
#   1) 차량 입고
#   2) 차량 출고
#   3) 차량 조회
#   4) 프로그램 종료

# 설정
max_car = 5     # 최대 5대
car_cnt = 0     # 주차 대수 카운트

# 결과: ["", "", "", "", ""]
#1. List Comprehension 기법
tower = ["" for i in range(max_car)]

# #2. for + list.append()
# tower = []
# for i in range(max_car):
#     tower.append("")

while True:
    print("="*50)
    print("== 주차 타워 시스템 ver1.1 ==")
    print("="*50)
    print("= 1.입고")
    print("= 2.출고")
    print("= 3.조회")
    print("= 4.종료")
    print("=" * 50)

    while True:
        select_num = int(input(">>번호: "))
        if 1 <= select_num <= 4:
            break
        else:
            print("MSG: 올바른 번호를 입력하세요.")

    if select_num == 1:     #입고
        #입고 1. 주차타워 공간 확인
        if car_cnt < max_car:   # 입고
            car_num = input(">>입고: ")
            for i, car in enumerate(tower):
                if car == "":
                    tower[i] = car_num
                    car_cnt += 1
                    break
        else:
            print("MSG: 입고가 불가능합니다.")   # 입고 불가
    elif select_num == 2:   #출고
        # 1. 차량번호
        # 2. 주차타워 차량번호 체크
        # 2-1 차가 없으면 다시 입력받음
        # 2-2 차가 있으면 출고(tower의 값을 ""으로 바꾸고 car_cnt를 -1해야 됨
        pass
    elif select_num == 3:   #조회
        pass
    elif select_num == 4:   #종료
        print("MSG: 프로그램을 종료합니다.")
        exit()
