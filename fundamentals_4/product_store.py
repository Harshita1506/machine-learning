class Products:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        # dont write count+=1 or self.count+=1 as self creates another variable 
        Products.count+=1
        
        
    def get_info(self):
        print(f"the price of the product {self.name} is {self.price} ")
   
   
    @classmethod
    def get_count(cls):
       print(f"total product in store ={cls.count}") 
    
    @staticmethod
    def disc_Calc(price,disc):
        final_price=(price-price*disc/100)
        print(f"final price is {final_price}")
        
        
        
p1=Products("VIVO BOOK",40_000)
p2=Products("i phone",60_000)
Products.get_count()
p1.disc_Calc(10_000,10) #we can simply pass the value of price dynamically by p1.price
