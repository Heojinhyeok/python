import Fridge

LG = Fridge.Fridge()
apple = Fridge.Food()
elephant = Fridge.Food()

LG.open()
LG.put(apple)
LG.put(elephant)
LG.close()
print("냉장고 안에 음식은: ", LG.foods)
