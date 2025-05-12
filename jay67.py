class library:
    def __init__(self):
        self.nobooks=0
        self.books=[]

    def addbooks(self , books):
        self.books.append(books)
        self.nobooks=len(self.books)
    
    def showinfo(self):
        print(f"the library has {self.nobooks} books. The book are :   ")
        for books in self.books:
            print(books)


l1=library()
l1.addbooks("jay books1")
l1.addbooks("jay books2")
l1.addbooks("jay books3")
l1.showinfo()

    