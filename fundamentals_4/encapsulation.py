#encapsulation is wrapping up of data into a single unit
#creating a capsule of two things 
#there is another concept of data hiding 
#when we want to keep some parameters private 
# that is why we make attributes public,protected,private

class BankAccount:
    
    def __init__(self,name,balance):
        self.name=name #public attr
      #  self._balance=balance #protected attr
        self.__balance=balance #private attr -> data mangling
        
        #private cant be accessed outside class 
        #getter and setter functions for pvt attributes
    
    
    def get_balance(self): # getter 
        return self.__balance 
        
    def set_balance(self,new_balance):# setter
        self.__balance=new_balance
        
acc1=BankAccount("Rahul",1_00_000)

print(acc1.name,acc1.get_balance())#we cant use acc1.__balnce
   # we can access private members through another way     
   # they are not entirely private
   # by objname._class name__ attr name
print(acc1.name,acc1._BankAccount__balance) 




