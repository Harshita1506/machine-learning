#instance class and static methods 
#instance method has self paramter and it can access both types of attributes
class Laptop:
    storage_type="ssd"
    
    def __init__(self,Ram,storage):
        self.Ram=Ram
        self.storage=storage
        
    def get_info(self):#instance method can access class attr and isntance with self
        print("laptop has this ram and storage and storage type",self.Ram,self.storage,self.storage_type)
        
l1=Laptop("16gb","512gb")        
l2=Laptop("32gb","256gb")  
l2.get_info()     
        