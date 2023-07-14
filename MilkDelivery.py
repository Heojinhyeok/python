milk_orders = {'101': {'milk': 1, 'yogurt': 5},
               '102': {'milk': 2},
               '103': {'milk': 1, 'yogurt': 10},
               '104': {'yogurt': 15}}

for house, order in milk_orders.items():
    if order.get('milk') :
        print(house, order['milk'])
