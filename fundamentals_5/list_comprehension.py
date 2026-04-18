square=[]
for i in range(6):
    square.append(i*i)
    
    
print (square)

# output    iterable  condition in square brackets 
# i*i     for i in range(6)

sq=[ i*i for i in range(6)]
print(sq)

sq=[ i*i for i in range(6) if i%2!=0]# odd number sqaure only 
print(sq)

# wap to replace all negative numbers with 0 using list comprehension
l=[-2,-4,3,5,2,-1]

l=[0 if val<0 else val for val in l ] #output if one condition 
print(l)# else for next output 

words=["hello","python"]
words=[val.upper() for val in words ]# we can use a function as well 
print(words)



