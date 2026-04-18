#this means many forms 
# we create multiple functions with same name 
# similar work 
# but these are all diff functions 
# example operator overlaoding 
# + is used to concat and add 
# context k hisaab se usi implementation change hojana 
# OOPS k context mein two types 1) FUNCTION OVERRIDING 2) DUCK TYPING

#function overriding only where inheritance is involved 
# when we redefining the parent's classes function in child class 

class Employee:
    def get_designation(self):
        print ("designation is employee")
        
class teacher(Employee):
    def get_designation(self):
        print ("designation is teacher")
        
t1=teacher()
t1.get_designation()


# DUCK TYPING 
# if something walks like a duck and quacks like a duck then we call it a duck
# when classes are NOT related to each other but have a function which is similar to each other 

class teacher():
    def get_designation(self):
        print ("designation is teacher")
        
class Accountant():
    def get_designation(self):
        print ("designation is Accountant")

t1=teacher()
t1.get_designation()

acc1=Accountant()
acc1.get_designation()

