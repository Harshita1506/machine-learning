#static method has no compulsory paramter 
#cannot access instance attr and even the class attr
#special decorator is used which is the static decorator 
#@staticmethod
#it is tied up with classes and we need to make a normal function 
#example calculation price on the basis of discount 

class Laptop:
    storage_type="ssd"
    
    def __init__(self,Ram,storage):
        self.Ram=Ram
        self.storage=storage
    @staticmethod 
    def calculate(price,discount):
        final_price=price-(discount*price/100)
        print("final price is ",final_price)
    
l1=Laptop("16gb","526gb")
l1.calculate(40_000,15)

