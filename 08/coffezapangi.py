import math
import sys

class Coffee:

    # 커피 자판기 기본 속성
    left_coffee = 10  # 남은 커피 개수
    left_money = 5000  # 남은 돈
    coffee_price = 300  # 커피 한개의 가격
    input_money = 0  # 사용자가 넣은 돈
    input_coffee_num = 0  # 사용자가 원하는 커피 개수
    output_money = 0  # 사용자가에 돌려줄 돈

    def requtest(self):
        self.input_money = int(input('돈을 넣으시오: '))
        self.input_coffee_num = int(input('원하는 커피 개수는: '))

    def get(self, input_money, input_coffee_num):
        price = input_coffee_num * self.coffee_price
        if input_money >= price:
            output_money = input_money - price
            if self.output_money == 0:
                print("커피 %d개를 드립니다." % input_coffee_num)
                print('거스름돈은 없습니다.')
            else:
                print("커피 %d개를 드립니다." % input_coffee_num)
                print("거스름돈 %d을 드립니다." % self.output_money)
                self.left_money -= self.output_money
            self.left_coffee -= input_coffee_num
        elif self.coffee_price <= input_money < price:
            num = math.trunc(input_money / self.coffee_price)
            self.output_money = input_money - (self.coffee_price * num)
            if self.output_money == 0:
                print("커피 %d개를 드립니다. " % num)
                print('거스름돈은 없습니다.')
            else:
                print("커피 %d개를 드립니다." % num)
                print("거스름돈 %d을 드립니다." % self.output_money)
                self.left_money -= self.output_money
            self.left_coffee -= num
        else:
            print('돈이 충분하지 못합니다. 돈을 더 넣어 주세요.')

    def info(self):
        print('-' * 30)
        print('자판기가 보유한 총 금액: ', self.left_money)
        print('자판기가 보유한 커피 개: ', self.left_coffee)
        print('-' * 30)
    def check_amount(self):
        if self.left_coffee <= 0 or self.left_money <= 0:
            return False
        else:
            return True

c = Coffee()

while True:

    c.requtest()
    if c.check_amount():
        c.get(c.input_money, c.input_coffee_num)
        c.info()
    else:
        sys.exit("자판기 커피 개수 또는 자판기 보유 잔액이 부족함.")
    input("Press any key ...")