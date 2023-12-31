##############################################################
# "스타벅스" 카페 키오스크 프로그램
#   - 일자: 2023년10월13일
#   - 작성자: LimDBi
#   - 내용: 카페 음료를 주문 및 판매하는 콘솔 프로그램

# - 조건
# 1. 사용자는 한번에 최대 음료 1개, 베이커리 1개, 굿즈 1개 구매 가능

#함수 사용
from service_kiosk import user_choice
from service_kiosk import show_menu

# 메뉴와 가격표
#   - Dict Type -> 데이터베이스
main_name = {1: "음료(Drink)", 2: "빵(Bakery)", 3: "굿즈(Goods)"}
drink_name = {1: "아메리카노", 2: "돌체콜드블루", 3: "딸기라떼", 4: "자몽에이드"}
bakery_name = {1: "카스테라", 2: "크로플", 3: "바움쿠헨"}
goods_name = {1: "텀블러", 2: "비치타월", 3: "무드등"}

drink_price = {1: 3000, 2: 4500, 3: 6000, 4: 5000}
bakery_price = {1: 4500, 2: 5000, 3: 7000}
goods_price = {1: 18000, 2: 7000, 3: 17000}

# 고객 주문 기록 저장
menu_save = []      # 고객 주문 메뉴 기록
price_save = []     # 고객 주문 금액 기록

# 1. 메인 메뉴 출력
print(""*50)
print("■■ ==스타벅스==")
print("■■ ==ver 1.2")
while True:
    print("="*50)
    print("MSG: 만나서 반갑습니다, 고객님.")
    print("■■ 메인 메뉴")
    for i in range(len(main_name)):
        print(f"■□ {i+1}. {main_name[i+1]}")
    print("■"*20)

    # 2. 메인 메뉴 선택
    choice = user_choice(len(main_name), "main")   #코드 보고 싶으면 ctrl + 클릭. (3, "main")을 전달

    # 3. 세부 메뉴 출력
    if choice == 1:     #음료
        # print("▲▲ 음료(Drink) 메뉴")
        # for i in range(len(drink_name)):
        #     print(f"▲△ {i+1}. {drink_name[i+1]}({drink_price[i+1]})")    #dict 인덱스 없음, key 있음.i+1해야 key의 첫번째값 가져옴.
        show_menu("음료(Drink)", drink_name, drink_price)
        # 4. 세부 메뉴 선택
        sub = user_choice(len(drink_name), "main")
        # 5. 음료 주문 저장
        menu_save.append(drink_name[sub])   # 비어있는 list menu_save에 값을 추가
        price_save.append(drink_price[sub])
    elif choice == 2:   #빵
        # print("▲▲ 빵(Bakery) 메뉴")
        # for i in range(len(bakery_name)):
        #     print(f"▲△ {i+1}. {bakery_name[i+1]}({drink_price[i+1]})")
        show_menu("빵(Bakery)", bakery_name, bakery_price)
        sub = user_choice(len(bakery_name), "main")     # 4. 세부 메뉴 선택
        menu_save.append(bakery_name[sub])
        price_save.append(bakery_price[sub])
    elif choice == 3:   #굿즈
        # print("▲▲ 굿즈(Goods) 메뉴")
        # for i in range(len(goods_name)):
        #     print(f"▲△ {i + 1}. {goods_name[i + 1]}({goods_price[i + 1]})")
        show_menu("굿즈(goods)", goods_name, goods_price)
        sub = user_choice(len(goods_name), "main")      # 4. 세부 메뉴 선택
        menu_save.append(goods_name[sub])
        price_save.append(goods_price[sub])
    elif choice == 99:
        print("MSG: 스타벅스 키오스크를 종료합니다.")
        exit()

    # 6. 추가 주문 or 결제 여부 선택
    print("●○ 추가 주문 하시겠습니까?(y/n)")
    flag = 0    #추가 주문 y/n
    while True:
        choice_yn = input("y/n: ")
        if choice_yn == "y" or choice_yn == "Y":
            break
        elif choice_yn.lower() == "n":  #lower()로 받는 문자를 소문자로 바꾸기
            flag = 1    #주문에서 결제창으로 이동
            break
        else:
            print("MSG: y 또는 n 만 입력하세요.")

    # 7. 주문 내역 출력
    if flag == 1:
        print("◆" * 50)
        print(f"◆◇ 고객님이 주문하신 메뉴 ")
        total_price = 0  # 총 주문 금액 합산
        for i, menu in enumerate(menu_save):
            print(f"◆◇   {i+1}.{menu}")
        for price in price_save:
            total_price += price
        print(f"MSG: 고객님이 주문하신 메뉴는 총 {len(menu_save)}개로 총 결제금액은 {total_price}원 입니다.")
        print("MSG: 이용해주셔서 감사합니다.")



