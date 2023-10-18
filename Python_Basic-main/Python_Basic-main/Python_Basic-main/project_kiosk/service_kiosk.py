# 키오스크 기능들

# 사용자 메뉴 선택 기능
# 1. 메인메뉴 선택(1, 2, 3, 99)
# 2. 세부메뉴 선택(1~4 또는 1~3)
# 3. max_cnt : 메뉴별 갯수
# 4. menu_type : main메뉴 or sub메뉴
def user_choice(max_cnt, menu_type):
    while True:
        choice = int(input(">> 번호: "))
        # main 메뉴에서 99를 입력하면 프로그램 종료
        if choice == 99 and menu_type == "main":
            return choice
        # 메인 또는 서브에서 메뉴 선택
        if 1 <= choice <= max_cnt:
            return choice
        else:
            print("MSG: 올바른 번호를 입력하세요.")

def show_manu(menu_type, menu_name, menu_price):
    print(f"▲▲ {menu_type} 메뉴")
    for i in range(len(menu_name)):
        print(f"▲△ {i+1}. {menu_name[i+1]}({menu_price[i+1]})")
