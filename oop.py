class fruits:
    def __init__(self, type, price, color):
        self.type = type
        self.price = price
        self.color = color
    def pindua(self):
        print(f"I like eating {self.type} and it costs {self.price}, color being {self.color}")

#creating an object

myobj =fruits("Banana","50 ksh","Yellow")
myobj2 =fruits("Mangoes","60 ksh","Red")

myobj.pindua()
myobj2.pindua()
