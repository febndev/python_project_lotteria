import os
os.system("clear")
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
    print("-----------------------------------------------")
print_logo()
total_price = 14700
print("금액을 확인하신 후 결제수단을 선택해 주세요.")
print_line()
print("주문금액:", total_price)
print("결제할 금액:", total_price)
print_line()

while True:
    print("1.신용/체크카드(삼성페이, LG페이, 애플페이)")
    print("2.간편결제(카카오페이, 네이버페이")
    print("3.교환권")
    print("4.L.pay")
    print("5.페이코")
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
        print("취소하시려면 0을 입력하세요.")
        card_number = int(input("카드번호: "))
        if card_number != 0:
            os.system("clear")
            print_logo()
            print("카드 데이터 로딩 완료")
            print_line()
            print("결제가 완료되었습니다.")
            print_line()
            break
        if card_number == 0:
            os.system("clear")
            print_logo()
            print("취소하셨습니다.")
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    elif payment_method == 2:
        os.system("clear")
        print_logo()
        print("바코드를 스캔해주세요.")
        print_line()
        # 바코드 그림
        print()
        b = "간편결제"
        print(f"{b:^12}")
        print("║█║▌║█║▌│║▌║▌█║")
        a = "1234567"
        print(f"{a:^15}")
        print_line()
        print("취소하시려면 0을 입력하세요.")
        barcode_number = int(input("바코드번호:"))
        if barcode_number != 0:
            os.system("clear")
            print_logo()
            print("결제가 완료되었습니다.")
            print_line()
            break
        if barcode_number == 0:
            os.system("clear")
            print_logo()
            print("취소하셨습니다.")
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    elif payment_method == 3:
        os.system("clear")
        print_logo()
        print("교환권 바코드를 스캔해주세요.")
        print_line()
        # 바코드 그림
        print()
        b = "교환권"
        print(f"{b:^13}")
        print_line()
        print("║█║▌║█║▌│║▌║▌█║")
        a = "1234567"
        print(f"{a:^15}")
        print("취소하시려면 0을 입력하세요.")
        exchange_coupon = int(input("바코드번호:"))
        if exchange_coupon != 0:
            os.system("clear")
            print_logo()
            print("결제가 완료되었습니다.")
            print_line()
            break
        if exchange_coupon == 0:
            os.system("clear")
            print_logo()
            print("취소하셨습니다.")
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    elif payment_method == 4:
        os.system("clear")
        print_logo()
        print("바코드를 스캔해주세요.")
        print_line()
        # 바코드 그림
        print()
        b = "L.pay"
        print(f"{b:^15}")
        print_line()
        print("║█║▌║█║▌│║▌║▌█║")
        a = "1234567"
        print(f"{a:^15}")
        print("취소하시려면 0을 입력하세요.")
        L_pay = int(input("바코드번호:"))
        if L_pay != 0:
            os.system("clear")
            print_logo()
            print("결제가 완료되었습니다.")
            print_line()
            break
        if L_pay == 0:
            os.system("clear")
            print_logo()
            print("취소하셨습니다.")
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    elif payment_method == 5:
        os.system("clear")
        print_logo()
        print("바코드 읽는 곳에 PAYCO 바코드를 인식해주세요.")
        print_line()
        # 바코드 그림
        print()
        b = "PAYCO"
        print(f"{b:^15}")
        print_line()
        print("║█║▌║█║▌│║▌║▌█║")
        a = "1234567"
        print(f"{a:^15}")
        print("취소하시려면 0을 입력하세요.")
        payco_barcode = int(input("바코드번호:"))
        if payco_barcode != 0:
            os.system("clear")
            print_logo()
            print("결제가 완료되었습니다.")
            print_line()
            break
        if payco_barcode == 0:
            os.system("clear")
            print_logo()
            print("취소하셨습니다.")
            print("결제방법을 다시 선택해 주세요.")
            print_line()
    else:
        os.system("clear")
        print_logo()
        print("결제방법을 다시 선택해 주세요.")
        print_line()