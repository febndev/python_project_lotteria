waiting_number=1
order_number = 1  # 주문번호 끄면 초기화됌
import datetime
import os, sys, time
def main():
    print("AutoRes is starting")
    executable = sys.executable
    args = sys.argv[:]
    args.insert(0, sys.executable)

    time.sleep(1)
    print("Respawning")
    os.execvp(executable, args)

def print_logo():
    print("""
    ===============================================================
    ██╗      ██████╗ ████████╗████████╗███████╗██████╗ ██╗ ██████╗
    ██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██║██╔═══██╗
    ██║     ██║   ██║   ██║      ██║   █████╗  ██████╔╝██║██║█████║
    ██║     ██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗██║██║   ██║
    ███████╗╚██████╔╝   ██║      ██║   ███████╗██║  ██║██║██║    █║
    ╚══════╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝    ╚╝
    ===============================================================
    """)

def print_line():
    print("=" * 67)

while True:
    print("1.시작 2.대기번호 및 주문번호 초기화")
    manager = input()
    if manager == "1":
        os.system("clear")  # 위에 코드 안보이게 해줌
        break
    while True:
        if manager == "2":
            os.system("clear")  # 위에 코드 안보이게 해줌
            re = input(f"1.대기번호 초기화 2.주문번호 초기화 3.아무 숫자나 입력시 돌아감")
            if re == "1":
                waiting_number = 1  # 대기번호
                print("대기번호 초기화")
                time.sleep(1)
            elif re == "2":
                order_number = 1  # 주문번호 끄면 초기화됌
                print("주문번호 초기화")
                time.sleep(1)
            elif re != "1" and re != "2":
                os.system("clear")  # 위에 코드 안보이게 해줌
                break
        else:
            print("다시 입력")
            break

def print_logo():
    print("""
    
    ██╗      ██████╗ ████████╗████████╗███████╗██████╗ ██╗ ██████╗
    ██║     ██╔═══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗██║██╔═══██╗
    ██║     ██║   ██║   ██║      ██║   █████╗  ██████╔╝██║██║█████║
    ██║     ██║   ██║   ██║      ██║   ██╔══╝  ██╔══██╗██║██║   ██║
    ███████╗╚██████╔╝   ██║      ██║   ███████╗██║  ██║██║██║    █║
    ╚══════╝ ╚═════╝    ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝╚═╝    ╚╝
    
    """)

def print_line():
    print("=" * 67)

while True:
    while True:
        print_logo()
        print_line()
        print("식사 장소를 선택해 주세요")
        print("")
        print("1. 매장식사", "2. 포장주문")  # 장소 선택메뉴 출력
        print("")
        print_line()
        select = int(input("숫자를 입력해 주세요.:  "))

        if select == 1:
            print("매장에서 드실 메뉴를 선택해 주세요.")
            oder_method = 1

            break
        elif select == 2:
            print("포장하실 메뉴를 선택해 주세요.")
            oder_method = 2

            break
        else:  # 선택오류
            print("다시 선택해 주세요.")
            print()       # 출력결과 지우고 첫화면으로 이동

    # 버거 리스트
    burger_lst = ["1.더블한우불고기버거", "2.한우불고기버거", "3.모짜렐라인더버거베이컨", "4.리아불고기더블(빅불)", "5.전주비빔라이스버거",
                 "6.더블엑스투버거","7.핫크리스피치킨버거","8.리아불고기베이컨","9.리아새우베이컨","10.맛피아모짜렐라(토마토바질)",
                 "11.맛피아모짜렐라(발사믹바질)","12.리아사각새우더블","13.리아불고기","14.리아새우","15.티렉스버거","16.더블치킨버거","17.치킨버거",
                 "18.더블데리버거","19.데리버거","20.더블클래식치즈버거(버터번)","21.클래식치즈버거(버터번)","22.더블미라클버거","23.미라클버거",
                 "24.한우명품팩","25.한우연인팩"]
    burger_price = [13000, 9000, 8000, 7600, 7300, 7200, 6200, 6100, 6100, 9100, 9100, 6100, 5000, 5000, 5000, 5800, 4300, 5000, 3700, 7200, 5500, 7200, 5700, 18500, 16700]

    # # 음료 , 커피 리스트
    # drink_lst = ["1.펩시콜라(L)", "2.칠성사이다(L)", "3.펩시콜라(R)", "4.칠성사이다(R)", "5.펩시콜라(S)","6.칠성사이다(S)",
    #              "7.펩시제로(L)","8.펩시제로(R)", "9.아메리카노","10.아이스아메리카노(R)","11.아이스아메리카노(L)","12.허쉬핫초코",
    #              "13.레몬에이드(L)","14.레몬에이드(R)","15.아이스티(L)", "16.아이스티(R)","17.아이스카페라떼(살균우유)",
    #              "18.카페라떼(살균우유)","19.오렌지주스(PET)","20.캐모마일티","21.애플캐모마일티","22.아이시스에코"]
    # drink_price = [2200, 2200, 2000, 2000, 1400, 1400, 2200, 2000, 2500, 2500, 3000, 2500, 3000, 2700, 2600, 2300, 3300, 3300, 2500, 2200, 2700, 1000]

    # 버거토핑 리스트
    topping_lst = ["1.반숙계란토핑","2.치즈토핑","3.토마토토핑","4.베이컨토핑","5.비프페티토핑"]
    topping_price = [1000, 800, 600, 700, 2100]

    # 세트 드링크 리스트
    set_drink_lst = ["1.펩시콜라(R)", "2.레몬에이드(L)", "3.아이스아메리카노(R)", "4.아이스아메리카노(L)", "5.허쉬핫초코", "6.아메리카노",
                     "7.캐모마일티","8.아이스티(R)","9.아이스티(L)", "10.레몬에이드(R)","11.카페라떼(살균우유)","12.아이스카페라떼(살균우유)",
                     "13.칠성사이다(R)","14.펩시제로(R)","15.펩시콜라(L)","16.칠성사이다(L)","17.펩시제로(L)","18.아이시스에코","19.오렌지주스(PET)"]
    set_drink_price = [0, 1000, 500, 1000, 500, 500, 200, 300, 600, 700, 1300, 1300, 0, 0, 200, 200, 200, 0, 500]

    # 진이 부분

    # 디저트 메뉴 리스트
    dessert_lst = ["1.쥐포튀김","2.못난이치즈감자","3.NEW치킨너겟","4.양념너겟","5.포테이토","6.포테이토(L)","7.양념감자","8.치즈스틱","9.롱치즈스틱","10.통오징어링",
                   "11.코울슬로","12.토네이도더블초코","13.토네이도망고젤리","14.토네이도-초코쿠키","15.토네이도-스트로베리","16.토네이도요고트맛초코쿠키","17.토네이도요거트맛망고젤리",
                   "18.토네이도요거트맛스트로베리","19.선데아이스크림-허쉬초코","20.선데아이스크림-스트로베리","21.선데아이스크림-플레인","22.소프트콘","23.지파이허바네로L",
                   "24.지파이 고소한맛S","25.치킨휠레4조각","26.치킨휠레2조각","27. 화이어윙4조각","28. 화이어윙2조각","29.순살치킨-풀팩","30.순살치킨-하프팩","31.치킨다리 1조각",
                   "32.청양마요소스","33.크리미마늘소스","34.크리미양념소스","35.데리야끼소스","36.머스타드소스","37.잠발라야소스","38.실비김치맛시즈닝","39.어니언시즈닝",
                   "40.치즈시즈닝","41.칠리시즈닝","42.허니머스타드","43.스위트앤사워"]
    dessert_price_lst = [4200,3500,3100,3300,2000,
                         2500,2600,2800,2400,2800,
                         1900,3200,3200,3200,3200,
                         3400,3400,3400,2300,2300,
                         2100,1300,5500,4500,5300,
                         3100,5500,3200,17500,10500,
                         2900,200,500,500,500,500,300,
                         200,200,200,200,100,100]

    # 세트 디저트 첫번째줄 메뉴 리스트
    set_dessert_lst = ["1.포테이토","2.쥐포튀김","3.못난이치즈감자","4.양념감자","5.치즈스틱","6.NEW치킨너겟","7.포테이토(L)","8.지파이하바네로L",
                    "9.지파이고소한맛","10.통오징어링","11.선데이아이스크림-플레인","12.토네이도-초코쿠키","13.토네이도-스트로베리]",
                        "14.토네이도요거트맛초코쿠키","15.토네이도요거트맛망고젤리","16.토네이도요거트맛스트로베","17.롱치즈스틱",
                        "18.코울슬로","19.치킨다리 1조각","20.화이어윙-2","21.치킨휠레-2","22.선데이아이스크림-허쉬초코",
                        "23.선데이아이스크르림-스트로베","양념너겟"]

    # 세트 디저트 첫번째줄 가격 리스트
    set_dessert_price_lst = [0, 2200, 1500, 600, 800, 1100, 500, 3500, 2500, 800, 100, 1200, 1200, 1400,1400,1400,400,0,900,1200,1100,300,300,1300]


    # # 세트 디저트 두번째줄 메뉴 리스트
    # set_dessert2_lst = ["14.토네이도요거트맛초코쿠키","15.토네이도요거트맛망고젤리","16.토네이도요거트맛스트로베","17.롱치즈스틱",
    #                     "18.코울슬로","19.치킨다리 1조각","20.화이어윙-2","21.치킨휠레-2","22.선데이아이스크림-허쉬초코",
    #                     "23.선데이아이스크르림-스트로베","양념너겟"]

    # 세트 디저트 두번째 줄 가격 리스트
    # set_dessert2_price_lst = [1400,1400,1400,400,0,900,1200,1100,300,300,1300]

    # 시즈닝 종류 리스트
    seasoning_lst = ["1.치즈시즈닝", "2.칠리시즈닝","3.어니언시즈닝","4.실비김치맛시즈닝"] #"5.선택 안함" 삭제

    # 음료/커피 메뉴 리스트
    drink_lst = ["1.펩시콜라 (L)","2.칠성사이다 (L)","3.펩시콜라 (R)","4.칠성사이다 (R)","5.펩시콜라 (S)","6.칠성사이다 (S)",
                 "7.펩시제로 (L)","8.펩시제로 (R)","9.아메리카노","10.아이스아메리카노 (R)","11.아이스아메리카노 (L)","12.허쉬핫초코",
                 "13.레몬에이드 (L)","14.레몬에이드 (R)","15.아이스티 (L)","16.아이스티 (R)","17.아이스카페라떼 (살균우유)",
                 "18.카페라떼 (살균우유)","19.오렌지주스 (PET)","20.캐모마일티","21.애플캐모마일티","22.아이시스에코"]

    # 음료/커피 가격 리스트
    drink_price_lst = [2200,2200,2000,2000,1400,
                       1400,2200,2000,2500,2500,
                       3000,2500,3000,2700,2600,
                       2300,3300,3300,2500,2200,2700,1000]
    # 진이 부분 끝
    # 카테고리 정의
    category = ["1.버거", "2.디저트/치킨", "3.음료/커피"]
    category_in_burger = ["1.버거만", "2.콤보", "3.세트"]

    # 메뉴명 리스트와 가격 리스트 요소 갯수 동일 확인 완료.
    # print("버거리스트: ", len(burger_lst), len(burger_price))
    # print("음료, 커피리스트: ", len(drink_lst), len(drink_price))
    # print("버거 토핑 리스트:", len(topping_lst), len(topping_price))
    # print("세트드링크리스트: ", len(set_drink_lst),len(set_drink_price))

    # 숫자 외 공백 입력시 무시하는 함수
    def onlyNum(numStr):
        numStr = str(numStr)
        numStr = numStr.replace(' ','')
        numStr = numStr.strip(',. ')
        num = int(numStr)
        return num

    # 장바구니 메뉴, 메뉴별 가격, 선택이 끝났는지, 총 결제 금액 선언
    order_items = []
    order_price = []
    end_selected = False
    total_price = 0
    # 추가주문 답변 리스트
    answer = ["Y", "y", "N", "n"]

    # 선택 시작
    os.system("clear")
    print_logo()

    # 카테고리 메뉴 선택 시작
    turn = 0 # for문을 사용하는 대신 변수 i 만 남겨놓은 상황인데 변수명을 변경할 필요가 있음.
    while end_selected == False :
        order_items.append([])
        order_price.append([])
        # 카테고리 선택 출력 창
        print_line()
        print(f'{"카테고리 선택":^62}')
        print_line()
        print("\n", category[0], "\n", category[1], "\n", category[2], "\n")

        print_line()
        selected_category = onlyNum(input("카테고리를 선택해주세요.>> "))
        while selected_category not in range(1, len(category) + 1):
            print("1~3 사이로 입력해주세요.")
            selected_category = onlyNum(input("숫자 입력: "))

        os.system("clear")
        print_logo()
        # 카테고리 선택

        if selected_category == 1:
            print_line()
            print(f'{"버거 세트 선택":^62}')
            print_line()
            print("\n", category_in_burger[0], "\n", category_in_burger[1], "\n", category_in_burger[2], "\n")
            print_line()

            selected_burger_set = onlyNum(input("버거만, 콤보, 세트 중 골라주세요.>> "))

            os.system("clear")
            print_logo()
            # 버거만 선택시 진행
            if selected_category == 1 and selected_burger_set == 1:
                # 버거 메뉴 화면 띄우기
                print_line()
                print(f'{"버거를 선택해주세요.":^62}')
                print_line()
                print()
                # 버거 선택
                # selected_burger = onlyNum(input("버거 숫자 입력>> "))
                while True:
                    print("")
                    print_line()
                    selected_burger = input("버거 숫자 입력>> ").strip()

                    if selected_burger == "" or selected_burger == " ":
                        print("다시 입력해주세요.")

                    elif selected_burger in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"                                                                                                        "14", "15",
                                             "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]:
                        break

                    else:
                        print("1~25 까지 숫자를 입력해주세요.")

                while selected_burger == " " or selected_burger == "" or selected_burger == "0":
                    print("System: 필수선택항목입니다.")
                    selected_burger = onlyNum(input("버거 숫자 입력: "))
                else:
                    selected_burger = onlyNum(selected_burger) - 1
                    for j in range(len(burger_lst)):
                        if selected_burger == burger_lst.index(burger_lst[j]):
                            print(burger_lst[j], "을(를) 선택하셨습니다.")
                            order_items[turn].append(burger_lst[j])
                            order_price[turn].append(burger_price[j])
                            total_price = total_price + burger_price[j]
                # 버거 토핑 선택
                # selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ")

                os.system("clear")
                print_logo()
                while True:
                    print("")
                    print_line()
                    print_line()
                    selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ").strip()

                    if selected_topping == "" or selected_topping == " ":
                        print("다시 입력해주세요.")

                    elif selected_topping in ["1", "2", "3", "4", "5"]:
                        break

                    elif selected_topping == "0" :
                        break

                    else:
                        print("1~5 까지 숫자를 입력해주세요.")

                selected_topping = onlyNum(selected_topping) - 1
                for l in range(len(topping_lst)):
                    if selected_topping == topping_lst.index(topping_lst[l]):
                        print(topping_lst[l], "을(를) 선택하셨습니다.")
                        order_items[turn].append(topping_lst[l])
                        order_price[turn].append(topping_price[l])
                        total_price += topping_price[l]

                os.system("clear")
                print_logo()

                # 추가 주문 여부 확인
                print("")
                add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                # answer = ["Y", "y", "N", "n"]
                while add_order not in answer:
                    print("System : 다시 입력해주세요.")
                    add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                if add_order == "Y" or add_order == "y":
                    turn += 1
                else:
                    end_selected = True

                os.system("clear")
                print_logo()

            # 콤보 선택시 진행
            elif selected_category == 1 and selected_burger_set == 2:
                # 콤보일때 버거 선택
                # selected_burger = onlyNum(input("버거 숫자 입력>> "))
                while True:
                    print("")
                    print_line()

                    print_line()
                    selected_burger = input("버거 숫자 입력>> ").strip()

                    if selected_burger == "" or selected_burger == " ":
                        print("다시 입력해주세요.")

                    elif selected_burger in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                             "13","14","15","16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]:
                        break

                    else:
                        print("1~25 까지 숫자를 입력해주세요.")

                while selected_burger == " " or selected_burger == "" or selected_burger == "0":
                    print("System: 필수선택항목입니다.")
                    selected_burger = onlyNum(input("버거 숫자 입력: "))
                else:
                    selected_burger = int(selected_burger)
                    selected_burger = selected_burger - 1
                    for j in range(len(burger_lst)):
                        if selected_burger == burger_lst.index(burger_lst[j]):
                            print(burger_lst[j], "을(를) 선택하셨습니다.")
                            order_items[turn].append(burger_lst[j])
                            order_price[turn].append(burger_price[j])
                            total_price = total_price + burger_price[j]

                os.system("clear")
                print_logo()

                # 콤보일 때 드링크 선택
                # selected_set_drink = onlyNum(input("세트 드링크 숫자 입력>>"))
                while True:
                    print("")
                    print_line()
                    print_line()
                    selected_set_drink = input("세트 드링크 숫자 입력>>").strip()

                    if selected_set_drink == "" or selected_set_drink == " ":
                        print("다시 입력해주세요.")

                    elif selected_set_drink in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                             "13", "14", "15", "16", "17", "18", "19"]:
                        break

                    else:
                        print("1~19 까지 숫자를 입력해주세요.")

                while selected_set_drink == " " or selected_set_drink == "" or selected_set_drink == 0:
                    print("System: 필수선택항목입니다.")
                    selected_set_drink = onlyNum(input("세트 드링크 숫자 입력>>"))

                else:
                    selected_set_drink = int(selected_set_drink)
                    selected_set_drink = selected_set_drink - 1
                    for k in range(len(set_drink_lst)):
                        if selected_set_drink == set_drink_lst.index(set_drink_lst[k]):
                            print(set_drink_lst[k], "을(를) 선택하셨습니다.")
                            order_items[turn].append(set_drink_lst[k])
                            order_price[turn].append(set_drink_price[k])
                            total_price = total_price + set_drink_price[k]

                    os.system("clear")
                    print_logo()

                # 콤보일 때 버거토핑 선택
                # selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ")

                while True:
                    print("")
                    print_line()
                    print_line()
                    selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ").strip()

                    if selected_topping == "" or selected_topping == " ":
                        print("다시 입력해주세요.")

                    elif selected_topping in ["1", "2", "3", "4", "5"]:
                        break

                    elif selected_topping == "0" :
                        break

                    else:
                        print("1~5 까지 숫자를 입력해주세요.")

                selected_topping = onlyNum(selected_topping) - 1
                for l in range(len(topping_lst)):
                    if selected_topping == topping_lst.index(topping_lst[l]):
                        print(topping_lst[l], "을(를) 선택하셨습니다.")
                        order_items[turn].append(topping_lst[l])
                        order_price[turn].append(topping_price[l])
                        total_price += topping_price[l]

                os.system("clear")
                print_logo()

                # 추가주문 여부 확인
                add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                answer = ["Y", "y", "N", "n"]
                while add_order not in answer:
                    print("System : 다시 입력해주세요.")
                    add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                if add_order == "Y" or add_order == "y":
                    turn += 1
                else:
                    end_selected = True

                os.system("clear")
                print_logo()

            # 버거 세트 선택시
            elif selected_category == 1 and selected_burger_set == 3:
                # 세트일때 버거 선택
                while True:
                    print("")
                    print_line()
                    selected_burger = input("버거 숫자 입력>> ").strip()

                    if selected_burger == "" or selected_burger == " ":
                        print("다시 입력해주세요.")

                    elif selected_burger in ["1", "2", "3", "4", "5","6","7","8","9","10","11","12","13"
                                             "14","15","16","17","18","19","20","21","22","23","24","25"]:
                        break

                    else:
                        print("1~25 까지 숫자를 입력해주세요.")

                while selected_burger == " " or selected_burger == "" or selected_burger == "0":
                    print("System: 필수선택항목입니다.")
                    selected_burger = input("버거 숫자 입력: ")
                else:
                    selected_burger = onlyNum(selected_burger) - 1
                    for j in range(len(burger_lst)):
                        if selected_burger == burger_lst.index(burger_lst[j]):
                            print(burger_lst[j], "을(를) 선택하셨습니다.")
                            order_items[turn].append(burger_lst[j])
                            order_price[turn].append(burger_price[j])
                            total_price = total_price + burger_price[j]

                os.system("clear")
                print_logo()

                # 세트일 때 디저트 선택
                while True:
                    print("")
                    print(set_dessert_lst)
                    set_dessert = input("세트 디저트 메뉴를 선택해주세요.: ").strip()

                    if set_dessert == "" or set_dessert == " ":
                        print("다시 입력해주세요.")

                    elif set_dessert in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13",
                                          "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]:
                        # print(set_dessert1)

                        set_dessert = int(set_dessert)
                        # print(type(set_dessert1))

                        # cart1_menu = []
                        # cart1_price = 0
                        # cart2_menu = []

                        for i in range(len(set_dessert_lst)):

                            if set_dessert - 1 == set_dessert_lst.index(set_dessert_lst[i]):
                                print(set_dessert_lst[i], "을(를) 선택하셨습니다.")
                                order_items[turn].append(set_dessert_lst[i])
                                order_price[turn].append(set_dessert_price_lst[i])

                                # print("")
                                # print("[장바구니]")
                                # print(cart1_menu)
                                # print(cart1_price)

                        break

                    else:
                        print("다시 입력해주세요.")

                os.system("clear")
                print_logo()

                while True:
                    print("")
                    selected_set_drink = input("세트 드링크 숫자 입력>>").strip()

                    if selected_set_drink == "" or selected_set_drink == " ":
                        print("다시 입력해주세요.")

                    elif selected_set_drink in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",
                                                "13", "14", "15", "16", "17", "18", "19"]:
                        break

                    else:
                        print("1~19 까지 숫자를 입력해주세요.")

                while selected_set_drink == " " or selected_set_drink == "" or selected_set_drink == "0":
                    print("System: 필수선택항목입니다.")
                    selected_set_drink = input("세트 드링크 숫자 입력>>")
                else:
                    selected_set_drink = onlyNum(selected_set_drink) - 1
                    for k in range(len(set_drink_lst)):
                        if selected_set_drink == set_drink_lst.index(set_drink_lst[k]):
                            print(set_drink_lst[k], "을(를) 선택하셨습니다.")
                            order_items[turn].append(set_drink_lst[k])
                            order_price[turn].append(set_drink_price[k])
                            total_price = total_price + set_drink_price[k]

                os.system("clear")
                print_logo()

                # 세트일 때 버거토핑 선택
                # selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ")
                while True:
                    print("")
                    print_line()
                    selected_topping = input("버거 토핑 숫자 입력(선택 종료시 0)>> ").strip()

                    if selected_topping == "" or selected_topping == " ":
                        print("다시 입력해주세요.")

                    elif selected_topping in ["1", "2", "3", "4", "5"]:
                        break

                    elif selected_topping == "0" :
                        break

                    else:
                        print("1~5 까지 숫자를 입력해주세요.")

                selected_topping = onlyNum(selected_topping) - 1
                for l in range(len(topping_lst)):
                    if selected_topping == topping_lst.index(topping_lst[l]):
                        print(topping_lst[l], "을(를) 선택하셨습니다.")
                        order_items[turn].append(topping_lst[l])
                        order_price[turn].append(topping_price[l])
                        total_price += topping_price[l]

                os.system("clear")
                print_logo()

                # 추가주문 여부 확인
                add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                answer = ["Y", "y", "N", "n"]
                while add_order not in answer:
                    print("System : 다시 입력해주세요.")
                    add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
                if add_order == "Y" or add_order == "y":
                    turn += 1
                else:
                    end_selected = True

                os.system("clear")
                print_logo()

        elif selected_category == 2:
        # elif choose_kategorie in ["1"]:
            print("")
            print(dessert_lst)

            while True:
                print("")
                choose_dessert = input("디저트 번호를 선택해주세요. :").strip()

                if choose_dessert == "" or choose_dessert == " ":
                    print("다시 입력해주세요.")

                elif choose_dessert in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                                          "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26",
                                          "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38",
                                          "39", "40", "41", "42", "43"]:
                    break

                else:
                    print("다시 입력해주세요.")

            # 숫자로 변환
            choose_dessert = int(choose_dessert)
            # 장바구니
            order_items[turn] = [] # cart1_menu = []에서 변경
            order_price[turn] = []  # cart1_price = 0 에서 변경
            # cart2_menu = [] / 삭제 order_items[i] cart1_menu와 합쳐짐

            # 선택한 디저트 메뉴
            for a in range(len(dessert_lst)):

                if choose_dessert - 1 == dessert_lst.index(dessert_lst[a]):
                    print(dessert_lst[a], "(을)를 선택하셨습니다.")
                    order_items[turn].append(dessert_lst[a])

                    order_price[turn].append(dessert_price_lst[a])

                    total_price += dessert_price_lst[a]
                    # print(cart1_price)

            os.system("clear")
            print_logo()

            # 시즈닝 선택

            if (choose_dessert == dessert_lst.index(dessert_lst[23]) or
                    choose_dessert == dessert_lst.index(dessert_lst[24]) or
                    choose_dessert == dessert_lst.index(dessert_lst[4]) or
                    choose_dessert == dessert_lst.index(dessert_lst[7])):

                print("")
                print(seasoning_lst)

                while True:
                    print("")
                    choose_seasoning = input("시즈닝 맛을 선택해주세요. :").strip()

                    if choose_dessert == "" or choose_dessert == " ":
                        print("다시 입력해주세요.")

                    elif choose_seasoning in ["1", "2", "3", "4", "5"]:
                        break

                    else:
                        print("다시 입력해주세요.")

                choose_seasoning2 = int(choose_seasoning)

                for i in range(4):
                    if choose_seasoning2 - 1 == seasoning_lst.index(seasoning_lst[i]):
                        print(seasoning_lst[i], "을(를) 선택하셨습니다.")
                        order_items[turn].append(seasoning_lst[i])

                os.system("clear")
                print_logo()

            add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
            while add_order not in answer:
                print("System : 다시 입력해주세요.")
                add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
            if add_order == "Y" or add_order == "y":
                turn += 1
            else:
                end_selected = True

            os.system("clear")
            print_logo()

        elif selected_category == 3:

        # elif choose_kategorie in ["2"]:
            print("")
            print(drink_lst)
            choose_drink = input("음료/커피 번호를 선택해주세요. :").strip()

            if choose_drink == "" or choose_drink == " ":
                print("다시 입력해주세요.")

            elif choose_drink in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                                  "15", "16", "17", "18", "19", "20", "21", "22"]:

                choose_drink = int(choose_drink)

                # 장바구니
                order_items[turn] = []  # cart1_menu = []에서 변경
                order_price[turn] = []  # cart1_price = 0 에서 변경
                # cart2_menu = [] / 삭제 order_items[i] cart1_menu와 합쳐짐

                # 선택한 음 메뉴
                for i in range(len(drink_lst)):

                    if choose_drink - 1 == drink_lst.index(drink_lst[i]):
                        print("")
                        print(drink_lst[i], "(을)를 선택하셨습니다.")
                        order_items[turn].append(drink_lst[i])

                        order_price[turn].append(drink_price_lst[i])
                        total_price += drink_price_lst[i]
                        # print(cart1_price)
                choose_drink = int(choose_drink)

                os.system("clear")
                print_logo()

                #
                # print("")
                # print("[장바구니]")
                # print(f"{cart1_menu}")
                # print(f"{cart1_price}")

                # break - 기존의 break 지웠음.

            else:
                print("다시 입력해주세요.")

            add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
            while add_order not in answer:
                print("System : 다시 입력해주세요.")
                add_order = input("추가로 더 주문하시겠습니까?(Y/N) >>")
            if add_order == "Y" or add_order == "y":
                turn += 1
            else:
                end_selected = True

            os.system("clear")
            print_logo()

        # 확인용 출력 코드
        # print(order_items)
        # print(order_price)
        # print(total_price)
        #
        # # 메뉴 항목을 리스트로 정의 (번호와 매칭하기 쉽게 순서대로 작성)
        # menu_items = []

        # 주문 번호 초기값 지정 (예: 1001부터 시작) - 0이나 1로 시작하면 헷갈릴 수 있기 때문에
        # order_number = 1001

        # # 사용자가 선택한 주문 내역을 저장할 빈 리스트
        # order_items = []

        # 무한 반복: 사용자가 주문 완료할 때까지 계속 메뉴 보여주고 입력 받음
        while True:
            print("\n===== 롯데리아 메뉴 =====")
            # for문을 이용해 메뉴 리스트의 길이만큼 반복하며 메뉴 출력
            # i는 0부터 시작하는 인덱스, 메뉴 번호는 i+1로 출력
            for i in range(len(order_items)):
                print(f"{i + 1}. {order_items[i]} - {order_price[i]}원")  # 상품과 가격을 표시 중
            print(f"총 결제 금액: {total_price}원")  # 총 가격을 표시하고 있음

            # --- 결제 취소하면 이전 단계인 버거주문으로 돌아가도록 수정함 ---
            print("0. 결제 하시려면 0번")
            print("1. 결제를 취소 하시려면 1번")

            try:
                choice = int(input("선택하세요 : "))
            except ValueError:
                print("다시 입력해주세요.")
                continue  # 숫자가 아닌 입력 시 다시 입력 요청

            if choice == 0:
                if not order_items:
                    print("주문 내역이 없습니다. 최소 1개 이상 선택하세요.")
                    continue
                print("\n===============================")
                print("       주문이 완료되었습니다       ")
                print("===============================")
                print("주문 번호:", order_number)
                print("주문 내역:")
                for item_list, price_list in zip(order_items, order_price):
                    for item, price in zip(item_list, price_list):
                        print(f"- {item} ({price}원)")
                print("감사합니다. 잠시만 기다려 주세요.")
                print("===============================\n")
                break
            elif choice == 1:
                print("결제가 취소되었습니다. 다시 주문을 시작합니다.")
                time.sleep(2)
                os.system("clear")
                total_price = 0
                order_items = []
                order_price = []
                end_selected = False
                turn = 0
                break  # 결제 취소 시, 현재 주문 프로세스(루프)를 종료하고 상위 루프로 돌아감
            else:
                print("다시 입력해주세요.")
                # 0, 1 이외의 숫자가 입력되어도 동일 메뉴가 계속 추가되는 현상을 방지하기 위해 continue 추가
                continue

        if choice == 1:  # 주문이 취소되었을 경우, 메인 주문 루프의 처음부터 다시 시작하세요.
            continue

            os.system("clear")

            # 주문 완료했으므로 반복 종료
            break
        # 1부터 메뉴 길이까지의 번호를 입력한 경우 메뉴 추가 처리1
        elif 1 <= choice <= len(order_items):
            # 선택한 메뉴를 주문 내역 리스트에 추가
            order_items.append(order_items[choice - 1])
            # 추가된 메뉴 이름 출력 (친절한 안내)
            print(f"{order_items[choice - 1]}가 추가되었습니다.")
        # 0과 1~메뉴번호 범위 외 숫자 입력 시 안내 메시지 출력
        else:
            print("유효하지 않은 번호입니다. 다시 입력해 주세요.")

            print_logo()

    os.system("clear")
    print_logo()
    print("금액을 확인하신 후 결제수단을 선택해 주세요.")
    print_line()
    print("주문금액:", total_price)
    print("결제할 금액:", total_price)
    print_line()

    while True:
        print("1.신용/체크카드(삼성페이, LG페이, 애플페이)")
        print("2.간편결제(카카오페이, 네이버페이)")
        print("3.교환권")
        print("4.L.pay")
        print("5.페이코")
        print("6.처음으로")
        print_line()
        payment_method = int(input("결제방법을 선택해 주세요 >> "))
        if payment_method == 1:
            os.system("clear")
            print_logo()
            print("카드를 단말기에 인식시켜 주세요.")
            print("카드 삽입 대기")
            print_line()
            print("결제할 금액:", total_price)
            # 카드 그림
            print("""
                      █████████████████╗
                      █    IC CARD    █║
                      █   ═════════   █║
                      █               █║
            ══════════█═══════════════█║═════
                      █               █║
                      █               █║
                      █               █║
                      █               █║
                      █████████████████║
                      ╚════════════════╝
            """)
            print_line()
            print("이전으로 가실려면 0을 입력해주세요.")
            print("처음으로 가실려면 9를 입력해주세요.")
            card_number = int(input("카드번호: "))
            if card_number == 0:
                os.system("clear")
                print_logo()
                print("취소하셨습니다.")
                print("결제방법을 다시 선택해 주세요.")
                print_line()
            if card_number == 9:
                if __name__ == "__main__":  # 이 함수가 재시작
                    main()
            if card_number != 0 and card_number != 9:
                os.system("clear")
                print_logo()
                print("카드 데이터 로딩 완료")
                print("결제가 완료되었습니다.")
                print_line()
                break
        elif payment_method == 2:
            os.system("clear")
            print_logo()
            print("바코드를 스캔해주세요.")
            # 바코드 그림
            print()
            b = "간편결제"
            print(f"{b:^12}")
            print("║█║▌║█║▌│║▌║▌█║")
            a = "1234567"
            print(f"{a:^15}")
            print_line()
            print("이전으로 가실려면 0을 입력해주세요.")
            print("처음으로 가실려면 9를 입력해주세요.")
            barcode_number = int(input("바코드번호:"))
            if barcode_number == 0:
                os.system("clear")
                print_logo()
                print("취소하셨습니다.")
                print("결제방법을 다시 선택해 주세요.")
                print_line()
            if barcode_number == 9:
                if __name__ == "__main__":  # 이 함수가 재시작
                    main()
            if barcode_number != 0 and barcode_number != 9:
                os.system("clear")
                print_logo()
                print("결제가 완료되었습니다.")
                print_line()
                break
        elif payment_method == 3:
            os.system("clear")
            print_logo()
            print("교환권 바코드를 스캔해주세요.")
            print()
            # 바코드 그림
            b = "교환권"
            print(f"{b:^13}")
            print("║█║▌║█║▌│║▌║▌█║")
            a = "1234567"
            print(f"{a:^15}")
            print_line()
            print("이전으로 가실려면 0을 입력해주세요.")
            print("처음으로 가실려면 9를 입력해주세요.")
            exchange_coupon = int(input("바코드번호:"))
            if exchange_coupon == 0:
                os.system("clear")
                print_logo()
                print("취소하셨습니다.")
                print("결제방법을 다시 선택해 주세요.")
                print_line()
            if exchange_coupon == 9:
                if __name__ == "__main__":  # 이 함수가 재시작
                    main()
            if exchange_coupon != 0 and exchange_coupon != 9:
                os.system("clear")
                print_logo()
                print("결제가 완료되었습니다.")
                print_line()
                break
        elif payment_method == 4:
            os.system("clear")
            print_logo()
            print("바코드를 스캔해주세요.")
            print()
            # 바코드 그림
            b = "L.pay"
            print(f"{b:^15}")
            print("║█║▌║█║▌│║▌║▌█║")
            a = "1234567"
            print(f"{a:^15}")
            print_line()
            print("이전으로 가실려면 0을 입력해주세요.")
            print("처음으로 가실려면 9를 입력해주세요.")
            L_pay = int(input("바코드번호:"))
            if L_pay == 0:
                os.system("clear")
                print_logo()
                print("취소하셨습니다.")
                print("결제방법을 다시 선택해 주세요.")
                print_line()
            if L_pay == 9:
                if __name__ == "__main__":  # 이 함수가 재시작
                    main()
            if L_pay != 0 and L_pay != 9:
                os.system("clear")
                print_logo()
                print("결제가 완료되었습니다.")
                print_line()
                break
        elif payment_method == 5:
            os.system("clear")
            print_logo()
            print("바코드 읽는 곳에 PAYCO 바코드를 인식해주세요.")
            print()
            # 바코드 그림
            b = "PAYCO"
            print(f"{b:^15}")
            print("║█║▌║█║▌│║▌║▌█║")
            a = "1234567"
            print(f"{a:^15}")
            print_line()
            print("이전으로 가실려면 0을 입력해주세요.")
            print("처음으로 가실려면 9를 입력해주세요.")
            payco_barcode = int(input("바코드번호:"))
            if payco_barcode == 0:
                os.system("clear")
                print_logo()
                print("취소하셨습니다.")
                print("결제방법을 다시 선택해 주세요.")
                print_line()
            if payco_barcode == 9:
                if __name__ == "__main__":  # 이 함수가 재시작
                    main()
            if payco_barcode != 0 and payco_barcode != 9:
                os.system("clear")
                print_logo()
                print("결제가 완료되었습니다.")
                print_line()
                break
        elif payment_method == 6:
            if __name__ == "__main__":  # 이 함수가 재시작
                main()
        else:
            os.system("clear")
            print_logo()
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    os.system("clear")  # 위에 코드 안보이게 해줌

    if waiting_number > 1000:
        waiting_number = 1
    if order_number > 10000:
        order_number=1

    b_b = str(order_number).zfill(4)  # 4자리수로 출력하기 위해서

    print_logo()
    print_line()
    print(f'{"주문번호":^62}')
    print(f"{waiting_number}")
    print("")
    print("1.영수증 출력 2.영수증 출력(X)")
    print("출력한 주문번호를 받아가세요.")
    print_line()

    receipt=input("영수증 유무 숫자를 입력하세요:")#영수증
    time.sleep(1)  # 1초후 넘어감
    os.system("clear")#위에 코드 안보이게 해줌
    while receipt not in ("1","2"):
        if receipt=="1":
            print(f'{"결제가 완료되었습니다.":^62}')
            print("    주문번호")
            print(f"     {waiting_number}")
            print("영수증 출력")
            print("출력한 주문번호를 받아가세요")
            break
        elif receipt=="2":
            print("결제가 완료되었습니다.")
            print("    주문번호")
            print(f"     {waiting_number}")
            print("영수증 출력(X)")
            print("출력한 주문번호를 받아가세요")
            break
        else:
            print("다시 입력해주세요")
            print("1.영수증 출력 2.영수증 출력(X)")
            receipt = input("영수증 유무 숫자를 입력하세요:")  # 영수증
    time.sleep(1)  # 1초후 넘어감
    os.system("clear")#위에 코드 안보이게 해줌
    print_logo()
    print("")
    if receipt =="1":
        print("      [ 무  인 ]")
        print("       대기번호")
        print(f"       {waiting_number}")
        if select == 1:
            print(f"     [ 매장 식사 ]")#{}안에 포장 매장식사 넣어야함 넣어야함
        else:
            print(f"         [ 포장 주문 ]")  # {}안에 포장 매장식사 넣어야함 넣어야함
        print("롯데리아 광주XX점 000-00-00000")
        print("광주 XX구 XX로 140 1층")
        print("대표 아무개 전화번호 000-000-0000")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print(f"거래일:{datetime.datetime.now()} POS:00")
        print(f"판매담당:0001/아무개       거래번호:{b_b}")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print("제품명                  금액")
        print(order_items,order_price)#시킨 메뉴
        print(f"총 합 계 {total_price}",f"청 구 액 {total_price}",f"받 은 돈 {total_price}",sep=" ")#총 합계및 부가세 과세 청구액 받은돈 면세금액
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        if payment_method == 1:
            print("XXXX카드",card_number,"KICC/A")#카드 번호와 인증 방식 필요
        elif payment_method ==2:
            print("간편결제",barcode_number)
        elif payment_method ==3:
            print("교환권 결제",exchange_coupon)
        elif payment_method ==4:
            print("L.pay",L_pay)
        elif payment_method ==5:
            print("페이코 결제",payco_barcode)
        print(f"결제금액:{total_price}     승인번호:00000000")
        print(f"할부개월:일시불        가맹점번호:0000000000")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print("wi-fi 비밀번호  00000000")
        print("║█║▌║█║▌│║▌║▌█║")
        print(" 0 0 0 0 0 0 0")
        time.sleep(6)
    else:
        print("[주 문 서]")
        print(" 대기번호")
        print(f"       {waiting_number}")
        print("고객님이 주문한 제품을 준비하고 있습니다.")
        print("제품이 완료되면 대기번호가 주문표시기에 안내됩니다.")
        print("[ 매장식사 ]")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print(f"거래일:{datetime.datetime.now()} POS:00")
        print(f"판매담당:0001/아무개       거래번호:{b_b}")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print("       제 품 명             포장유무")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        if select == 1:
            print(f"{order_items,order_price}")#주문한 품목 및 포장유무
        elif select == 2:
            print(f"                             포장")
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print(f"합  계                    {total_price}")#마지막 부분에 합계 필요
        print("￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣￣")
        print("wi-fi 비밀번호 00000000")
        print("║█║▌║█║▌│║▌║▌█║")
        print(" 0 0 0 0 0 0 0")
        time.sleep(6)  # 3초후 넘어감

    waiting_number = waiting_number + 1
    order_number = order_number + 1
    #시작지점 실행 시키기