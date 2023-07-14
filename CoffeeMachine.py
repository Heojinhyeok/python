import sys

avail_coffee = 10
coffee = 300
money = 10000

while True:
    if not avail_coffee :
        sys.exit("품절! 재고 준비중입니다")

    coffee_num = int(input("커피 몇 개를 드릴까요 : "))
    if coffee_num > avail_coffee :
        print("수량이 부족합니다. %d개까지 구입 가능합니다." %avail_coffee) ; print()
        continue
    else :
        price = coffee_num * coffee
        print("금액은 %d 원 입니다." %price) ; print()

        ask = int(input("금액을 넣어주세요 : "))
        if ask < price :
            print("%d원이 부족합니다." % (price - ask)) ; print()
            continue

        elif ask > price :
            avail_coffee -= coffee_num
            print("%d원을 받았습니다.\n\n[+] 커피 %d개가 나왔습니다.\n거스름돈은 %d원 입니다.\n" %(ask, coffee_num, price-ask))
            print ("[*] 커피 재고 %d개" % avail_coffee) ; print()

        elif ask == price :
            avail_coffee -= coffee_num
            print("커피 %d개가 나왔습니다. 감사합니다.\n[*] 커피 재고 %d개" %(coffee_num, avail_coffee)) ; print()