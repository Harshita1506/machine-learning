''' ATTRIBUTES
2 TYPES- CLASS(belong to class common ) AND INSTANCE(belong to object unique ) 
student- instance (name,suvject,cgpa)
class obj( school name)

'''
class Student:
    college_name="ABC " #class attribute
    PI=3.1
    def __init__(self,name,gpa):
        self.name=name #instance attribute 
        self.gpa=gpa
        self.PI=3.14
        
stu1=Student("Rahul",9.2)
print(stu1.name)# this prints the name of stu1
#print(Student.name)# this will give error as the class student doesnt have any name attribute 
print(stu1.college_name)#this will also work 
print(Student.college_name)#this will also work 
print(Student.PI)# will give 3.1 as it is a class attribute
print(stu1.PI) # gives value 3.14

''' hum object se dono types k attributes ko access kr sakte hain'''
''' hum class se bus class object ko access kr sakte hain'''
'''if same attribute is there in class att and instance then instance will be called (when called by object) '''

