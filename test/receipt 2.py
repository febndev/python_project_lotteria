os.system("clear")  # 위에 코드 안보이게 해줌
if waiting_number > 1000:
    waiting_number = 1
if order_number > 10000:
    order_number = 1
print_logo()
order_items1 = []
order_price1 = []
for i in range(len(order_items)):
    order_items1 = order_items1 + order_items[i]
    order_price1 = order_price1 + order_price[i]

b_b = str(order_number).zfill(4)  # 4자리수로 출력하기 위해서
print(f"{"결제가 완료되었습니다.":^65}")
print(f"{"주문번호":^67}")
print(f"{f"{waiting_number}번":^67}")
print(f"{"1.영수증 출력 2.영수증 출력(X)":^67}")
print(f"{"출력한 주문번호를 받아가세요":^65}")
print(f"{"영수증 유무 숫자를 입력하세요:":^66}")
receipt = input()  # 영수증
os.system("clear")  # 위에 코드 안보이게 해줌
print_logo()

while receipt not in ("1", "2"):
    if receipt in ["1", "2"]:
        break
    else:
        print(f"{"다시 입력해주세요.":^67}")
        print(f"{"1.영수증 출력 2.영수증 출력(X)":^67}")
        print(f"{"영수증 유무 숫자를 입력하세요:":^66}")
        receipt = input()  # 영수증
if receipt == "1":
    print(f"{"결제가 완료되었습니다.":^67}.")
    print(f"{"주문번호":^67}")
    print(f"{f"{waiting_number}번":^67}")
    print(f"{"영수증 출력":^67}")
    print(f"{"출력한 주문번호를 받아가세요":^65}.")
elif receipt == "2":
    print(f"{"결제가 완료되었습니다.":^67}.")
    print(f"{"주문번호":^67}")
    print(f"{f"{waiting_number}번":^67}")
    print(f"{"영수증 출력(X)":^67}")
    print(f"{"출력한 주문번호를 받아가세요":^65}.")
time.sleep(1)  # 1초후 넘어감
os.system("clear")  # 위에 코드 안보이게 해줌
if receipt == "1":
    print(f"{"[ 무  인 ]":^40}.")
    print(f"{"대기번호":^40}.")
    print(f"{f"{waiting_number}번":^40}")
    if select == 1:
        print(f"{"[매장 식사]":^40}")  # {}안에 포장 매장식사 넣어야함 넣어야함
    else:
        print(f"{"[ 포장 주문 ]":^40}")  # {}안에 포장 매장식사 넣어야함 넣어야함
    print(f"{"롯데리아 광주XX점 000-00-00000":^40}")
    print(f"{"광주 XX구 XX로 140 1층":^40}")
    print(f"{"대표 아무개 전화번호 000-000-0000":^40}")
    print("￣" * 30)
    print(f"{f"거래일:{datetime.datetime.now()} POS:00":^40}")
    print(f"{f"판매담당:0001/아무개       거래번호:{b_b}":^40}")
    print("￣" * 30)
    print(f"{"제품명                  금액":^40}")
    for i in range(len(order_items1)):
        print(f"{f"{order_items1[i]}  {order_price1[i]}":^40}")  # 시킨 메뉴
    print(f"{f"총 합 계 {total_price} 청 구 액 {total_price} 받 은 돈 {total_price}":^40}")  # 총 합계및 부가세 과세 청구액 받은돈 면세금액
    print("￣" * 30)
    if payment_method == 1:
        print(f"{f"XXXX카드{card_number}KICC/A":^40}")  # 카드 번호와 인증 방식 필요
    elif payment_method == 2:
        print(f"{f"간편결제{barcode_number}":^40}")  # 카드 번호와 인증 방식 필요
    elif payment_method == 3:
        print(f"{f"교환권 결제{exchange_coupon}":^40}")
    elif payment_method == 4:
        print(f"{f"L.pay{L_pay}":^40}")
    elif payment_method == 5:
        print(f"{f"페이코 결제{payco_barcode}":^40}")
    print(f"{f"결제금액:{total_price}     승인번호:00000000":^40}")
    print(f"{f"할부개월:일시불        가맹점번호:0000000000":^40}")
    print("￣" * 40)
    print(f"{"wi-fi 비밀번호  00000000":^40}")
    print(f"{"║█║▌║█║▌│║▌║▌█║":^40}")
    print(f"{" 0 0 0 0 0 0 0":^40}")
    time.sleep(6)
else:
    print(f"{"[주 문 서]":^40}")
    print(f"{"대기번호":^40}")
    print(f"{f"{waiting_number}":^40}")
    print(f"{"고객님이 주문한 제품을 준비하고 있습니다.":^40}")
    print(f"{"제품이 완료되면 대기번호가 주문표시기에 안내됩니다.":^40}")
    print(f"{"[ 매장식사 ]":^40}")
    print("￣" * 40)
    print(f"{f"거래일:{datetime.datetime.now()} POS:00":^40}")
    print(f"{f"판매담당:0001/아무개       거래번호:{b_b}":^40}")
    print("￣" * 40)
    print(f"{"제 품 명             포장유무":^40}")
    print("￣" * 40)

    if select == 1:
        for i in range(len(order_items1)):
            print(f"{f"{order_items1[i]}  {order_price1[i]}":^40}")  # 시킨 메뉴
    elif select == 2:
        print(f"{f"포장":^40}")
    print("￣" * 40)
    print(f"{f"합  계                    {total_price}":^40}")  # 마지막 부분에 합계 필요
    print("￣" * 40)
    print(f"{"wi-fi 비밀번호 00000000":^40}")
    print(f"{"║█║▌║█║▌│║▌║▌█║":^40}")
    print(f"{" 0 0 0 0 0 0 0":^40}")
    time.sleep(6)  # 3초후 넘어감

os.system("clear")
waiting_number = waiting_number + 1
order_number = order_number + 1
# 시작지점 실행 시키기