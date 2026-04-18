# hiding internal details and showing only essential features 
# diff bw encapsulation and abs 
# in encapsulation we give access which is protected privatye 
# kaunse data ko show krna hai hide krna hai 
# abstract class voh class hai which is a blueprint for other classes 
# abstract classes are a part of abc module 
# directly imported and we create abstract class 

from abc import ABC,abstractmethod

class Animal(ABC):# abstract bnane k liye ABS ko inherit 
    @abstractmethod
    def make_sound(self):
        pass 
        
class Lion(Animal):
        def make_sound(self):
            print("roar")
            
class Cow(Animal):
        def make_sound(self):
            print("mooo")
            
lion=Lion()
lion.make_sound()

cow=Cow()
cow.make_sound()