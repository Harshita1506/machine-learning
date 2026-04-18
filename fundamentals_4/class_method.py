#class method has paramter class and it can only access class attrclass
#we also have a decorator 
#which is @classmethod jo ki function k upar likhte hain
#class method decorator behaviour chnage krta hai and class method bnadeta hai for that class
class Laptop:
    storage_type="ssd"
    
    def __init__(self,Ram,storage):
        self.Ram=Ram
        self.storage=storage
     
    @classmethod    
    def get_storage_type(cls):
        print("storage type is ",cls.storage_type,cls.Ram)#cls.Ram wont work as it is not a class attribute
    #even if this function is called by an object then also it wont work
    
    
     
l1=Laptop("16gb","526gb")
l1.get_storage_type()
Laptop.get_storage_type()#both works 
