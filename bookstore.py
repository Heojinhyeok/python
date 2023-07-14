class Book:
    books = {}
    def __init__(self):
        print("책방이 새로 만들어졌습니다.")

    def setData(self, title, price, author):
        self.books[title] = [price, author]

    def printData(self, title):
        if title in self.books:
            print(title, self.books[title])
        else:
            print("책이 없습니다.")

