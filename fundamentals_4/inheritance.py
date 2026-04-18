#eg ek class ki props being used in some other class 
# parent class/ base class k attributes/methods to child class/derived class 
class Employee():
    start_time="10am"
    end_time="6pm"
    
    def change_time(self,new_end_time):
        self.end_time=new_end_time
        
class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject 
        
class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role

t1=Teacher("Math")
print(t1.subject,t1.end_time,t1.start_time)
staff1=AdminStaff("manager")
print(staff1.role,staff1.start_time,staff1.end_time)


#protected k case mein attribite will be accessible to sub class 
#private k case mein nahi hogi 

''' TYPES OF INHERITANCE 
1) SINGLE LEVEL
2) MULTI LEVER 
3) 
'''
class Employee():
    start_time="10am"
    end_time="6pm"
    
    def change_time(self,new_end_time):
        self.end_time=new_end_time
class AdminStaff(Employee):
    def __init__(self,role):
        self.role=role
        
class Accountant(AdminStaff)   :
    def __init__(self,salary,role):# here we need to pass role (attr of parent class )
        super().__init__(role)#here we have invoked the constructor of the parents class 
        self.salary = salary 

acc1= Accountant(25_000,"CA")
print(acc1.role,acc1.salary,acc1.end_time,acc1.start_time)
     
''' MULTIPLE INHERITANCE
ek class jo more than 1 class se properties inherit krri ho '''   

class Teacher:
    def __init__(self,salary):
        self.salary=salary
class Student:
    def __init__(self,gpa):
        self.gpa=gpa
    
class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary)# no self here as bus object reference reqd 
        Student.__init__(self,gpa)
        self.name=name
        
        
ta1=TA(15_000,9.3,"Harhsita")
print(ta1.name,ta1.gpa,ta1.salary)



    
