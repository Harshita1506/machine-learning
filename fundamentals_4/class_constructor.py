class Student: 
    subject ="Maths" # parameter in class 
    college="ABC college"  
    year="4th year"
    def __init__(self,name,cgpa):  
        self.name=name
        self.cgpa=cgpa
        print("constructor was called")
        
    def get_cgpa(self):
        return self.cgpa
#constructor in python also known as init method 

a=10
stu1=Student("Harshita",9.2) 
stu2=Student("Yukti",9.6)# jitne objects banenge utne hi baar the constructor will be called 
print(stu1.name,stu1.subject,stu1.year,stu1.college,)
print(stu1.get_cgpa())

''' this is basicaly increasing the code reusability since we sont have to give properties to these 2 studeents differently and also
that we can simply create 3000 students and just using one loop we can do that 
a list of 3000 students can be maintained list=[stu1,stu2,stu3....]
'''
s=set() # using class set we have create an object s 

